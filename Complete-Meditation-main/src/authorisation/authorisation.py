from enum import Enum, auto
from os.path import exists, isfile, isdir
import os
import sys

sys.path.append(os.path.dirname(__file__) + r"/../")
from session import session_manager_singleton  # NOQA

from AuthorisationDataBase import authorisation_database_singleton


class AuthorisationType(Enum):
    READING = auto()
    WRITING = auto()
    UPLOADING = auto()
    DOWNLOADING = auto()
    DELETING = auto()


class Authorisation:
    def __init__(self, session_manager, authorisationDataBase):
        self._permissions = {
            AuthorisationType.READING: self._reading_permission,
            AuthorisationType.WRITING: self._writing_permission,
            AuthorisationType.UPLOADING: self._uploading_permission,
            AuthorisationType.DOWNLOADING: self._downloading_permission,
            AuthorisationType.DELETING: self._deleting_permission,
        }
        self._session_manager = session_manager
        self._authorisationDataBase = authorisationDataBase

    def has_permission(self, session, permission_type: AuthorisationType, **kwargs) -> bool:
        # query user login status
        if user_info := self._session_manager.get(session):
            if _f := self._permissions.get(permission_type):
                return _f(user_info, **kwargs)


        return False

    def _common_file_checking(self, f, user_info, **kwargs):
        file = kwargs.get("file")
        print(f"file {file}, {type(file)}")
        if not file or not exists(file) or not isfile(file):
            # no file parameters or file not exists or not a file
            return False

        user_list = f(file)
        if user_info.name in user_list or user_info.is_admin:
            return True
        
        return False

    def _reading_permission(self, user_info, **kwargs):
        return self._common_file_checking(self._authorisationDataBase.get_reading, user_info, **kwargs)

    def _writing_permission(self, user_info, **kwargs):
        return self._common_file_checking(self._authorisationDataBase.get_writing, user_info, **kwargs)

    def _downloading_permission(self, user_info, **kwargs):
        return self._common_file_checking(self._authorisationDataBase.get_downloading, user_info, **kwargs)

    def _deleting_permission(self, user_info, **kwargs):
        return self._common_file_checking(self._authorisationDataBase.get_deleting, user_info, **kwargs)

    def _uploading_permission(self, user_info, **kwargs):
        folder = kwargs.get("file")
        if not folder or not exists(folder) or not isdir(folder):
            # no file parameters or file not exists
            return False

        user_list = self._authorisationDataBase.get_uploading(folder)
        if user_info.name in user_list or user_info.is_admin:
            return True

        return False


authorisation_singleton = Authorisation(session_manager_singleton, authorisation_database_singleton)
