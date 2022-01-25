from contextlib import contextmanager

from deafadder_container.MetaTemplate import Component
from tinydb import Query, TinyDB

from douglas_security_manager.config.datastore import DataStoreComponent
from douglas_security_manager.model import Setup
from douglas_security_manager.exceptions import ApplicationAlreadySetup, ApplicationNotAlreadySetup


class SetupRepository(metaclass=Component):

    _datastore: DataStoreComponent

    def setup_already_exist(self) -> bool:
        with self.connection() as conn:
            return self._setup_already_set(conn)

    @staticmethod
    def _setup_already_set(conn: TinyDB) -> bool:
        return len(conn.all()) == 1

    def _get_setup(self, conn: TinyDB) -> Setup:
        if not self._setup_already_set(conn):
            raise ApplicationNotAlreadySetup("There is not record in the setup table")
        pass

    def add_new_setup(self, setup: Setup) -> None:
        with self.connection() as conn:
            self._add_new_setup(setup, conn)

    def _add_new_setup(self, setup: Setup, conn: TinyDB) -> None:
        if self._setup_already_set(conn):
            raise ApplicationAlreadySetup("An entry already exist in the setup table")
        conn.insert(setup.to_dict())

    @contextmanager
    def connection(self):
        conn = self._datastore.connect()
        table = conn.table('setup')
        try:
            yield table
        finally:
            conn.close()
