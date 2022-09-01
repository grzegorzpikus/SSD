"""This part would be considered as a API gateway, just forward valid requests to one defined handler.
The request format follows /request/<defined_request_name>/<parameter1>&<parameter2>&...
The the handlers should verify parameters.
For example: login request will be /request/login/name=test&password=123, 
the request will be passed to login handler with parameters {name: test, password: 123}
"""

import os
import sys
from enum import Enum

import flask
from flask import Flask, send_file
from flask import request as FlaskRequest
# from werkzeug.datastructures import FileStorage

sys.path.append(os.path.dirname(__file__) + r'/Authentication')
from Input_checker import log_in_with_http, sign_up
from crud import crud


server = Flask(__name__)


def dump_func(*args, **kwargs):
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")
    return True

def upload_wrap(flask_request):
    file_data = flask_request.files.get('file')
    return crud.user_upload(file_data=file_data, **flask_request.args)


class RequestType(Enum):
    """Defined what request a client can send"""

    SIGNUP = "signup"
    LOGIN = "login"
    DOWNLOAD = "download"
    UPLOAD = "upload"
    DELETE = "delete"
    CREATE = "create"
    UPDATE = "update"


# bind request to a specific handler
request_handlers = {
    RequestType.SIGNUP.value: sign_up,
    RequestType.LOGIN.value: log_in_with_http,
    RequestType.DOWNLOAD.value: crud.user_download,
    RequestType.UPLOAD.value: upload_wrap,
    # RequestType.DELETE.value: dump_func,
    # RequestType.CREATE.value: dump_func,
    # RequestType.UPDATE.value: dump_func,
}


@server.route('/request/<request_type>', methods=['POST', 'GET', 'PUT', 'DELETE'])
def dispatcher(request_type):
    """The function will call a defined function based on request type"""

    if (handler := request_handlers.get(request_type)):
        try:
            if request_type == RequestType.UPLOAD.value:
                result = handler(FlaskRequest)
            else:
                result = handler(**FlaskRequest.args)
            if isinstance(result, (flask.wrappers.Response, str)):
                # called function can return its successful info to client
                return (result, 200)
            return ("request successful", 200)
        except Exception as err:
            return (str(err), 400)
    return ("Invalid request", 400)


if __name__ == "__main__":
    current_dir = os.path.dirname(__file__)
    # enable https supporting, and it requires client to send with https starting, can't use http
    # and the cert file was generated with 127.0.0.1 only, you can replace them if needed
    server.run(host="127.0.0.1", port=8080, ssl_context=(
        current_dir + r'./flask_cert.pem', current_dir + r'./flask_private-key.pem'), debug=True)
