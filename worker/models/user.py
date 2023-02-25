class User:
    def __init__(self, username: str, name: str, surname: str, age: int, email: str):
        """
        User class for db model
        :param username: str
        :param name: str
        :param surname: str
        :param age: int
        :param email: str
        """
        self.username = username
        self.name = name
        self.surname = surname
        self.age = age
        self.email = email

    def get_user(self):
        """
        :return: User dict
        """
        return {
            "username": self.username,
            "name": self.name,
            "surname": self.surname,
            "age": self.age,
            "email": self.email,
        }
