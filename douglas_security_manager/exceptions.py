class DouglasException(Exception):
    pass


class ProfileAlreadyExistWithSameName(DouglasException):
    pass


class ApplicationAlreadySetup(DouglasException):
    pass


class ApplicationNotAlreadySetup(DouglasException):
    pass
