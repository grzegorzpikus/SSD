import pathlib
import os
import sys

from flask import send_file
from readerwriterlock import rwlock

sys.path.append(os.path.dirname(__file__) + r"/../authorisation")
from authorisation import authorisation_singleton, AuthorisationType  # NOQA

from common_cfg import file_repository


_crud_lock = rwlock.RWLockFairD()


def user_download(session=None, file_name=None):
    file_path = file_repository + f"/{file_name}"
    if not authorisation_singleton.has_permission(session, AuthorisationType.DOWNLOADING, file=file_path):
        # file permission check failed
        raise Exception("no permission to download file")

    with _crud_lock.gen_rlock():
        return send_file(file_path, as_attachment=True)


def user_upload(file_data=None, session=None, file_name=None):
    if not file_data:
        raise Exception("Empty file to upload")

    if not authorisation_singleton.has_permission(session, AuthorisationType.UPLOADING, file=file_repository):
        # folder permission check failed
        raise Exception("no permission to upload file")

    # check file_name size to avoid too long
    if len(file_name) > 100:
        raise Exception("The file name can't exceed 100 characters")

    # sanitize file's name
    good_name = ""
    for c in file_name:
        if c in "._-()" or "A" <= c <= "Z" or "a" <= c <= "z" or "0" <= c <= "9":
            # remove danger character
            good_name += c
    valid_suffix = [".pdf", ".txt", ".zip", ".jpg"]
    if "." not in good_name or pathlib.Path(good_name).suffix.lower() in valid_suffix:
        save_file = file_repository + f"/{good_name}"
        with _crud_lock.gen_wlock():
            file_data.save(save_file)
        return
    raise Exception("Invalid file type")


def user_list_files(session=None):
    all_files = os.listdir(file_repository)
    user_list_files = []
    for file in all_files:
        if authorisation_singleton.has_permission(session, AuthorisationType.READING, file=file):
            user_list_files.append(file)
    return f"files: {str(user_list_files)}"


def user_delete_file(session=None, file_name=None):
    if authorisation_singleton.has_permission(session, AuthorisationType.DELETE, file=file_name):
        file_path = file_repository + f"/{file_name}"
        with _crud_lock.gen_wlock():
            os.remove(file_path)
            return
    raise Exception("Can't delete file")
