from dataclasses import dataclass


@dataclass
class Profile:

    username: str
    password: str
    description: str = "<none>"

    def to_dict(self):
        return self.__dict__


@dataclass
class EncryptedProfile(Profile):
    pass
