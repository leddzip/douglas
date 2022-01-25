import abc
from dataclasses import dataclass


DEFAULT_REFERENCE = "reference_token"


class Model(abc.ABC):

    def to_dict(self):
        return self.__dict__


@dataclass
class Profile(Model):

    username: str
    password: str
    description: str = "<none>"


class EncryptedProfile(Profile):
    pass


@dataclass
class Setup(Model):

    reference: str
    encrypted_reference: str
