from contextlib import contextmanager

from deafadder_container.MetaTemplate import Component
from tinydb import Query

from douglas_security_manager.config.datastore import DataStoreComponent
from douglas_security_manager.model import EncryptedProfile
from douglas_security_manager.exceptions import ProfileAlreadyExistWithSameName


class ProfileRepository(metaclass=Component):

    _datastore: DataStoreComponent

    def insert(self, profile: EncryptedProfile) -> None:
        with self.connection() as conn:
            profile_query = Query()
            if conn.search(profile_query.username == profile.username):
                raise ProfileAlreadyExistWithSameName(f"Another profile with user name '{profile.username}' already exist")
            conn.insert(profile.to_dict())

    @contextmanager
    def connection(self):
        conn = self._datastore.connect()
        table = conn.table('profile')
        try:
            yield table
        finally:
            conn.close()

