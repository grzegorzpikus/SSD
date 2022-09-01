"""Unittests for Authentication part of the software. To run the tests, this
file (unittests.py) has to be executed."""


import unittest
import Input_checker as Ic
import Classes as C
import Authentication_checker as Ac
import database_managment as dbm
import Authentication as A


class TestInputChecker(unittest.TestCase):
    """The class collects all tests for functions in Input_checker.py file."""

    def test_amidn_log_in(self):
        """The test checks admin's input for log_in function."""
        input_test = Ic.log_in("admin2022", "Thisisanadminpassword1!")
        expected = C.Administrator("Admin Admin", "admin@cern.ch", "admin2022",
                                   str(Ac.hashing("Thisisanadminpassword1!")))
        self.assertEqual(input_test, expected)

    def test_user_log_in(self):
        """The test checks user's input for log_in function."""
        input_test = Ic.log_in("grzegorzpikus", "Grzegorzpikus1987!")
        expected = C.User("Grzegorz Pikus", "grzegorzpikus@cern.ch",
                                   "grzegorzpikus",
                                   str(Ac.hashing("Grzegorzpikus1987!")))
        self.assertEqual(input_test, expected)

    def test_no_user_log_in(self):
        """The test tries to log in tho the system using user's data that do
        no exist in the database"""
        self.assertRaises(RuntimeError, Ic.log_in, "joanosborn", "weakpassword")

    def test_wrong_password_log_in(self):
        """The test tries to log in tho the system using an invalid password."""
        self.assertRaises(RuntimeError, Ic.log_in, "amin2022", "weakpassword")

    def test_wrong_username_log_in(self):
        """The test tries to log in tho the system using an invalid username."""
        self.assertRaises(RuntimeError, Ic.log_in, "amin",
                          "Thisisanadminpassword1!")

    def test_sign_up(self):
        """
        The test adds a user to the database and checks it if it has been
        added successfully. Afterwards the user is removed to make it work
        each time.
        """
        Ic.sing_up("User Test", "usertest@cern.ch", "usertest",
                   "Usertest2022!@")
        input_test = dbm.sql_user_exist("usertest")
        expected = 1
        self.assertEqual(input_test, expected)
        dbm.sql_delete_user("usertest")

    def test_user_exist_sign_up(self):
        """The test checks if an error is risen if an extisting user is added
        to the database."""
        self.assertRaises(RuntimeError, Ic.sing_up, "Admin Admin",
                          "admin@cern.ch", "admin2022",
                          "Thisisanadminpassword1!")

    def test_user_wrong_name_sign_up(self):
        """The test checks is an error is risen if a wrong username is
        passed."""
        self.assertRaises(RuntimeError, Ic.sing_up, "UserTest",
                          "usertest@cern.ch", "usertest", "Usertest2022!@")

    def test_user_wrong_email_sign_up(self):
        """The test checks is an error is risen if a wrong email address is
        passed."""
        self.assertRaises(RuntimeError, Ic.sing_up, "User Test",
                          "usertest@gmail.com", "usertest", "Usertest2022!@")

    def test_user_wrong_username_sign_up(self):
        """The test checks is an error is risen if a wrong username is
        passed."""
        self.assertRaises(RuntimeError, Ic.sing_up, "User Test",
                          "usertest@gmail.com", "user test", "Usertest2022!@")

    def test_user_wrong_password_sign_up(self):
        """The test checks is an error is risen if a wrong username is
        passed."""
        self.assertRaises(RuntimeError, Ic.sing_up, "User Test",
                          "usertest@cern.ch", "user test", "Usertest2022")


class TestAuthenticationChecker(unittest.TestCase):
    """The class collects all tests for functions in Authentication_checker.py
    file."""

    def test_hashing(self):
        """The test checks if hashing function works correctly"""
        input = Ac.hashing("Thisisanadminpassword1!")
        expected = "7f54caf81b9cdfa9f70dcab80ccdf705f0e54316f6" \
                   "7740d37163ac3e4db578c3"
        self.assertEqual(input, expected)

    def test_user_exist1(self):
        """This test if the function returns 1 by passing details of
        an existing user."""
        input = Ac.user_exists("admin2022")
        expected = 1
        self.assertEqual(input, expected)

    def test_user_exist2(self):
        """This test if the function returns 0 by passing details of
        q user that does not exist in the database."""
        input = Ac.user_exists("usertest")
        expected = 0
        self.assertEqual(input, expected)

    def test_password_correct1(self):
        """This test checks if the function returns True by checking an valid
        password of an existing user in the database."""
        input = Ac.password_correct("admin2022", "Thisisanadminpassword1!")
        expected = True
        self.assertEqual(input, expected)

    def test_password_correct2(self):
        """This test checks if the function returns False by checking an invalid
        password of an existing user in the database."""
        input = Ac.password_correct("admin2022", "XXThisisanadminpassword1!")
        expected = False
        self.assertEqual(input, expected)


class TestAuthentication(unittest.TestCase):
    """The class collects all tests for functions in Authentication.py
    file."""

    def test_add_user(self):
        """
        This test if a function adds a user to the database correctly.
        The user data are removed afterwards, to make this test working each
        time.
        """
        details = ["testinguser", "Verywaekpassword123!!", "Testing User",
                   "testinguser@cern.ch", 0]
        A.add_user(details)
        input_test = dbm.sql_user_exist("testinguser")
        expected = 1
        self.assertEqual(input_test, expected)
        dbm.sql_delete_user("testinguser")

    def test_create_user_object1(self):
        """
        This test checks if a user object is created properly by providing
        a username of an existing user in the database. This test is dedicated
        for Administrator Class.
        """
        input = A.create_user_object("admin2022")
        expected = C.Administrator("Admin Admin", "admin@cern.ch", "admin2022",
                                   str(Ac.hashing("Thisisanadminpassword1!")))
        self.assertEqual(input, expected)

    def test_create_user_object2(self):
        """
        This test checks if a user object is created properly by providing
        a username of an existing user in the database. This test is dedicated
        for Administrator Class.
        """
        input = A.create_user_object("grzegorzpikus")
        expected = C.User("Grzegorz Pikus", "grzegorzpikus@cern.ch",
                                   "grzegorzpikus",
                                   str(Ac.hashing("Grzegorzpikus1987!")))
        self.assertEqual(input, expected)


class TestDatabaseManagment(unittest.TestCase):
    """The class collects all tests for functions in data_managment.py file."""

    def test_sql_add_user(self):
        """This test checks is a user is added correctly to the database."""
        details = ["testinguser", "Verywaekpassword123!!", "Testing User",
                   "testinguser@cern.ch", 0]
        dbm.sql_add_user(details)
        input_test = dbm.sql_user_exist("testinguser")
        expected = 1
        self.assertEqual(input_test, expected)
        dbm.sql_delete_user("testinguser")

    def test_sql_user_exist1(self):
        """This test checks if a function returns 1 if a username of an
        existing user is passed through."""
        input_test = dbm.sql_user_exist("admin2022")
        expected = 1
        self.assertEqual(input_test, expected)

    def test_sql_user_exist2(self):
        """This test checks if a function returns 0 if a username of a user
        that does not exist in the database is passed through."""
        input_test = dbm.sql_user_exist("testinguser")
        expected = 0
        self.assertEqual(input_test, expected)

    def test_sql_password_correct1(self):
        """This function checks if a correct hashed password is returned by
        providing a username."""
        input_test = dbm.sql_password_correct("admin2022")
        expected = '7f54caf81b9cdfa9f70dcab80ccdf705f0e54316f67740' \
                   'd37163ac3e4db578c3'
        self.assertEqual(input_test, expected)

    def test_sql_password_correct2(self):
        """This function checks if a correct hashed password is returned by
        providing a username."""
        try:
            input_test = dbm.sql_password_correct("Testinguser")
        except TypeError:
            input_test = None
        expected = None
        self.assertEqual(input_test, expected)
















if __name__ == '-__main__':
    unittest.main()