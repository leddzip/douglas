from deafadder_container.MetaTemplate import Component
from tinydb import TinyDB

from douglas_security_manager.config.context import ContextComponent


class DataStoreComponent(metaclass=Component):

    _context: ContextComponent

    def connect(self) -> TinyDB:
        return TinyDB(self._context.data_file_path)
