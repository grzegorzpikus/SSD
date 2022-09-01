import sys
import os
import json
import unittest
from unittest.mock import Mock

sys.path.append(os.path.dirname(__file__)+ r"/../")
from AuthorisationDataBase import AuthorisationDataBase  # NOQA


class TestAuthorisationDataBase(unittest.TestCase):
    def _init_data(self):
        config_str = r"""
            {
                "FileRepository":
                {
                    "uploading": ["userA"]
                },

                "testA.pdf":
                {
                    "reading": ["userA", "userB", "userZ"],
                    "writing": ["userA", "userB"],
                    "deleting": ["userA"],
                    "downloading": ["userA", "userB", "userX"]
                },

                "testB.txt":
                {
                    "reading": ["userA", "userB", "userZ"],
                    "writing": ["userA", "userB"],
                    "deleting": ["userA"],
                    "downloading": ["userA", "userB", "userX"]
                }
            }
        """
        self._authorisationDataBase = AuthorisationDataBase(json.loads(config_str))

    def test_query(self):
        self._init_data()
        user_list = self._authorisationDataBase.get_reading(r"testA.pdf")
        self.assertEqual(user_list, ["userA", "userB", "userZ"])
        user_list = self._authorisationDataBase.get_writing(r"testA.pdf")
        self.assertEqual(user_list, ["userA", "userB"])
        user_list = self._authorisationDataBase.get_deleting(r"testA.pdf")
        self.assertEqual(user_list, ["userA"])
        user_list = self._authorisationDataBase.get_uploading(r"testA.pdf")
        self.assertEqual(user_list, None)
        user_list = self._authorisationDataBase.get_uploading(r"FileRepository")
        self.assertEqual(user_list, ["userA"])
        user_list = self._authorisationDataBase.get_downloading(r"testA.pdf")
        self.assertEqual(user_list, ["userA", "userB", "userX"])

    def test_updating(self):
        self._init_data()
        file_name = r"testB.txt"
        # update_reading
        self._authorisationDataBase.update_reading(file_name, ["userX", "userY"], True)
        user_list = self._authorisationDataBase.get_reading(file_name)
        self.assertEqual(user_list, ["userA", "userB", "userZ", "userX", "userY"])
        self._authorisationDataBase.update_reading(file_name, ["userZ"], True)
        user_list = self._authorisationDataBase.get_reading(file_name)
        self.assertEqual(user_list, ["userA", "userB", "userZ", "userX", "userY"])
        self._authorisationDataBase.update_reading(file_name, ["userX", "userY"], False)
        user_list = self._authorisationDataBase.get_reading(file_name)
        self.assertEqual(user_list, ["userA", "userB", "userZ"])
        self._authorisationDataBase.update_reading(file_name, ["NotExist"], False)
        user_list = self._authorisationDataBase.get_reading(file_name)
        self.assertEqual(user_list, ["userA", "userB", "userZ"])

        # update_writing
        self._authorisationDataBase.update_writing(file_name, ["userX", "userY"], True)
        user_list = self._authorisationDataBase.get_writing(file_name)
        self.assertEqual(user_list, ["userA", "userB", "userX", "userY"])
        self._authorisationDataBase.update_writing(file_name, ["userZ"], True)
        user_list = self._authorisationDataBase.get_writing(file_name)
        self.assertEqual(user_list, ["userA", "userB", "userX", "userY", "userZ"])
        self._authorisationDataBase.update_writing(file_name, ["userX", "userY"], False)
        user_list = self._authorisationDataBase.get_writing(file_name)
        self.assertEqual(user_list, ["userA", "userB", "userZ"])
        self._authorisationDataBase.update_writing(file_name, ["NotExist"], False)
        user_list = self._authorisationDataBase.get_writing(file_name)
        self.assertEqual(user_list, ["userA", "userB", "userZ"])

        # update_deleting
        self._authorisationDataBase.update_deleting(file_name, ["userX", "userY"], True)
        user_list = self._authorisationDataBase.get_deleting(file_name)
        self.assertEqual(user_list, ["userA", "userX", "userY"])
        self._authorisationDataBase.update_deleting(file_name, ["userZ"], True)
        user_list = self._authorisationDataBase.get_deleting(file_name)
        self.assertEqual(user_list, ["userA", "userX", "userY", "userZ"])
        self._authorisationDataBase.update_deleting(file_name, ["userX", "userY"], False)
        user_list = self._authorisationDataBase.get_deleting(file_name)
        self.assertEqual(user_list, ["userA", "userZ"])
        self._authorisationDataBase.update_deleting(file_name, ["NotExist"], False)
        user_list = self._authorisationDataBase.get_deleting(file_name)
        self.assertEqual(user_list, ["userA", "userZ"])

        # update_downloading
        self._authorisationDataBase.update_downloading(file_name, ["userX", "userY"], True)
        user_list = self._authorisationDataBase.get_downloading(file_name)
        self.assertEqual(user_list, ["userA", "userB", "userX", "userY"])
        self._authorisationDataBase.update_downloading(file_name, ["userZ"], True)
        user_list = self._authorisationDataBase.get_downloading(file_name)
        self.assertEqual(user_list, ["userA", "userB", "userX", "userY", "userZ"])
        self._authorisationDataBase.update_downloading(file_name, ["userX", "userY"], False)
        user_list = self._authorisationDataBase.get_downloading(file_name)
        self.assertEqual(user_list, ["userA", "userB", "userZ"])
        self._authorisationDataBase.update_downloading(file_name, ["NotExist"], False)
        user_list = self._authorisationDataBase.get_downloading(file_name)
        self.assertEqual(user_list, ["userA", "userB", "userZ"])

        # update_uploading
        folder_name = r"FileRepository"
        self._authorisationDataBase.update_uploading(folder_name, ["userX", "userY"], True)
        user_list = self._authorisationDataBase.get_uploading(folder_name)
        self.assertEqual(user_list, ["userA", "userX", "userY"])
        self._authorisationDataBase.update_uploading(folder_name, ["userZ"], True)
        user_list = self._authorisationDataBase.get_uploading(folder_name)
        self.assertEqual(user_list, ["userA", "userX", "userY", "userZ"])
        self._authorisationDataBase.update_uploading(folder_name, ["userX", "userY"], False)
        user_list = self._authorisationDataBase.get_uploading(folder_name)
        self.assertEqual(user_list, ["userA", "userZ"])
        self._authorisationDataBase.update_uploading(folder_name, ["NotExist"], False)
        user_list = self._authorisationDataBase.get_uploading(folder_name)
        self.assertEqual(user_list, ["userA", "userZ"])


if __name__ == "__main__":
    unittest.main()
