"""This module focuses on session manage
"""

import time
import uuid
import hashlib
from dataclasses import dataclass
from readerwriterlock import rwlock


@dataclass
class SessionUserInfo:
    name: str = None
    is_admin: bool = False
    login_time: int = 0
        

class SessionManager:
    """Record logged-in user data, the session timeout will be 3600 seconds.
    Calling add() can extend session expire time.
    """

    def __init__(self, session_timeout):
        self._rwlock = rwlock.RWLockFairD()
        self._sessions = {}
        self._timeout = session_timeout

    def add(self, user):
        """Add user to the cache and get an unique id as session.
        if user has been there, it will extend the session expire time.
        user: obj as a login user
        
        """
        
        with self._rwlock.gen_wlock():  # write lock
            for session, user_info in self._sessions.items():
                if user.user_name == user_info.name:
                    # just extend the session live time
                    user_info.login_time =int(time.time())
                    return session

            # new user case
            login_time = int(time.time())
            name_with_salt = uuid.uuid4().hex + user.user_name + r":" + str(login_time)
            session = hashlib.sha256(name_with_salt.encode()).hexdigest()
            is_admin = False
            if user.admin != 0:
                is_admin = True
            new_user_info = SessionUserInfo(user.user_name, is_admin, login_time)
            self._sessions[session] = new_user_info
            print(f"user: {self._sessions[session]}")
            return session

    def get(self, session):
        """Query user data from session, return user info or None if session has no record

        :param str session: a string as session
        :return [namedtuple_userInfo, None]: a valid user info or None
        """
         
        with self._rwlock.gen_rlock():  # read lock
            user_info = self._sessions.get(session)
            now_time = int(time.time())
            if user_info and ((now_time - user_info.login_time) < self._timeout):
                # session timeout is 3600 seconds
                return user_info
            return None


session_manager_singleton = SessionManager(3600)
