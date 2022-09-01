import database_managment as dbm


class User:
    """This class stores users details. After log-in the information about
    an user are kept in the object of this class."""

    def __init__(self, __name, __email, __user_name, __password, admin=0):
        self.__name = __name
        self.__email = __email
        self.user_name = __user_name
        self.__password = __password
        self.admin = admin

    def __str__(self):
        """It represents a object as a string if the string is printed."""
        return f"{self.__name}"

    def __repr__(self):
        """This is a graphical representation of an object"""
        return f"{self.user_name}"

    def __eq__(self, other):
        return self.__name == other.__name and self.__email == other.__email \
               and self.user_name == other.user_name \
               and self.__password == other.__password \
               and self.admin == other.admin


class Administrator(User):

    def __init__(self, __name, __email, __user_name, __password, admin=1):
        super().__init__(__name, __email, __user_name, __password, admin)

    def delete_user(self, selected_user):
        dbm.sql_delete_user(selected_user)

    def change_user_status(self, selected_user):
        dbm.sql_change_user_status(selected_user)


class Experiment:
    """This class represents a created or loaded experiment"""

    def __init__(self, id, name, date, owner):
        self.__id = id
        self.__name = name
        self.__date = date
        self.__owner = owner

    def __str__(self):
        """It represents a object as a string if the string is printed."""
        return f"Experiment {self.__name}"

    def __repr__(self):
        """This is a graphical representation of an object"""
        return f"Experiment Class, name: {self.__name}"
