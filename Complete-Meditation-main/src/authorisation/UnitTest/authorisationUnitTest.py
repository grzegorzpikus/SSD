import sys, os
import unittest
from unittest.mock import Mock
from collections import namedtuple
import time

sys.path.append(os.path.dirname(__file__) + r"/../")
from authorisation import Authorisation, AuthorisationType

class TestAuthorisation(unittest.TestCase):

    def _init_data(self, user_list, AuthorisationDataBaseMock):
        AuthorisationDataBaseMock.get_reading.return_value = user_list
        AuthorisationDataBaseMock.get_writing.return_value = user_list
        AuthorisationDataBaseMock.get_downloading.return_value = user_list
        AuthorisationDataBaseMock.get_deleting.return_value = user_list
        AuthorisationDataBaseMock.get_uploading.return_value = user_list

    def test_has_permission_true(self):
        sessionManagerMock = Mock()
        sessionManagerMock.get.return_value = namedtuple("UserInfo", "name is_admin, login_time", defaults=["test", False, time.time()])()
        AuthorisationDataBaseMock = Mock()
        user_list = {"test", "william", "john"}
        self._init_data(user_list, AuthorisationDataBaseMock)

        auth = Authorisation(sessionManagerMock, AuthorisationDataBaseMock)
        self.assertTrue(auth.has_permission("test", AuthorisationType.READING, file=os.path.dirname(__file__)+r"/testFile.txt"))
        self.assertTrue(auth.has_permission("test", AuthorisationType.WRITING, file=os.path.dirname(__file__)+r"/testFile.txt"))
        self.assertTrue(auth.has_permission("test", AuthorisationType.DOWNLOADING, file=os.path.dirname(__file__)+r"/testFile.txt"))
        self.assertTrue(auth.has_permission("test", AuthorisationType.DELETING, file=os.path.dirname(__file__)+r"/testFile.txt"))
        self.assertTrue(auth.has_permission("test", AuthorisationType.UPLOADING, file=os.path.dirname(__file__)))

    def test_has_permission_false(self):
        sessionManagerMock = Mock()
        sessionManagerMock.get.return_value = namedtuple("UserInfo", "name is_admin, login_time", defaults=["test", False, time.time()])()
        AuthorisationDataBaseMock = Mock()
        user_list = {"william", "john"}
        self._init_data(user_list, AuthorisationDataBaseMock)

        auth = Authorisation(sessionManagerMock, AuthorisationDataBaseMock)
        self.assertFalse(auth.has_permission("test", AuthorisationType.READING, file=os.path.dirname(__file__)+r"/testFile.txt"))
        self.assertFalse(auth.has_permission("test", AuthorisationType.WRITING, file=os.path.dirname(__file__)+r"/testFile.txt"))
        self.assertFalse(auth.has_permission("test", AuthorisationType.DOWNLOADING, file=os.path.dirname(__file__)+r"/testFile.txt"))
        self.assertFalse(auth.has_permission("test", AuthorisationType.DELETING, file=os.path.dirname(__file__)+r"/testFile.txt"))
        self.assertFalse(auth.has_permission("test", AuthorisationType.UPLOADING, file=os.path.dirname(__file__)))

    def test_has_permission_without_login(self):
        sessionManagerMock = Mock()
        sessionManagerMock.get.return_value = None
        AuthorisationDataBaseMock = Mock()
        user_list = {"test", "william", "john"}
        self._init_data(user_list, AuthorisationDataBaseMock)

        auth = Authorisation(sessionManagerMock, AuthorisationDataBaseMock)
        self.assertFalse(auth.has_permission("test", AuthorisationType.READING, file=os.path.dirname(__file__)+r"/testFile.txt"))
        self.assertFalse(auth.has_permission("test", AuthorisationType.WRITING, file=os.path.dirname(__file__)+r"/testFile.txt"))
        self.assertFalse(auth.has_permission("test", AuthorisationType.DOWNLOADING, file=os.path.dirname(__file__)+r"/testFile.txt"))
        self.assertFalse(auth.has_permission("test", AuthorisationType.DELETING, file=os.path.dirname(__file__)+r"/testFile.txt"))
        self.assertFalse(auth.has_permission("test", AuthorisationType.UPLOADING, file=os.path.dirname(__file__)))

    def test_has_permission_admin(self):
        sessionManagerMock = Mock()
        sessionManagerMock.get.return_value = namedtuple("UserInfo", "name is_admin, login_time", defaults=["test", True, time.time()])()
        AuthorisationDataBaseMock = Mock()
        user_list = { }
        self._init_data(user_list, AuthorisationDataBaseMock)

        auth = Authorisation(sessionManagerMock, AuthorisationDataBaseMock)
        self.assertTrue(auth.has_permission("test", AuthorisationType.READING, file=os.path.dirname(__file__)+r"/testFile.txt"))
        self.assertTrue(auth.has_permission("test", AuthorisationType.WRITING, file=os.path.dirname(__file__)+r"/testFile.txt"))
        self.assertTrue(auth.has_permission("test", AuthorisationType.DOWNLOADING, file=os.path.dirname(__file__)+r"/testFile.txt"))
        self.assertTrue(auth.has_permission("test", AuthorisationType.DELETING, file=os.path.dirname(__file__)+r"/testFile.txt"))
        self.assertTrue(auth.has_permission("test", AuthorisationType.UPLOADING, file=os.path.dirname(__file__)))


if __name__ == "__main__":
    unittest.main()