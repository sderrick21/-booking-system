from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name

    @abstractmethod
    def get_role(self):
        pass

class Member(User):
    def get_role(self):
        return "Member"

class Librarian(User):
    def get_role(self):
        return "Librarian"
