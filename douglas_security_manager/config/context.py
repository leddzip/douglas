from deafadder_container.MetaTemplate import Component


class ContextComponent(metaclass=Component):

    password: str
    data_file_path: str

    def __init__(self):
        """
        Empty method to avoid confusion with the setup method.
        We do not want the initialisation to be done at init time of the
        instance but later on, by explicitly invoking the setup method.
        """
        pass

    def setup(self, password: str, data_file_path: str):
        self.password = password
        self.data_file_path = data_file_path
