from deafadder_container.MetaTemplate import Component

from douglas_security_manager.config.datastore import DataStoreComponent
from douglas_security_manager.model.profile import EncryptedProfile


class ProfileRepository(metaclass=Component):

    _datastore: DataStoreComponent

    def insert(self, profile: EncryptedProfile) -> None:
        self._datastore.connect().insert(profile.to_dict())
