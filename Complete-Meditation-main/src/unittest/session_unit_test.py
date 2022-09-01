import os
import sys
import time
import unittest
from unittest.mock import Mock


sys.path.append(os.path.dirname(__file__) + r"/../")
from session import SessionManager


class TestSessionManager(unittest.TestCase):
    _session_manager = SessionManager(2)
    
    def test_add_session(self):
        cls = self.__class__
        user_mock = Mock()
        user_mock.user_name = "fake user A"
        user_mock.admin = 0
        session = cls._session_manager.add(user_mock)
        self.assertNotEqual(session, None)
        user_info = cls._session_manager.get(session)
        self.assertEqual(user_info.name, user_mock.user_name)
        time.sleep(2)
        timeout_user_info = cls._session_manager.get(session)
        self.assertEqual(timeout_user_info, None)
        session_2 = cls._session_manager.add(user_mock)
        self.assertEqual(session, session_2)
        user_info_2 = cls._session_manager.get(session_2)
        self.assertEqual(user_info_2.name, user_mock.user_name)
        fake_session = "asdfqwervxcsvae6f4qw65er486q7wer"
        self.assertEqual(cls._session_manager.get(fake_session), None)

if __name__ == "__main__":
    unittest.main()
