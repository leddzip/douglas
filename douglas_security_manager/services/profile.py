from deafadder_container.MetaTemplate import Component

from douglas_security_manager.repositories.profile import ProfileRepository
from douglas_security_manager.model.profile import Profile, EncryptedProfile
from douglas_security_manager.services.crypto import CryptographyService


class ProfileService(metaclass=Component):

    _profile_repository: ProfileRepository
    _crypto_service: CryptographyService

    def create_new_profile(self, profile: Profile):
        print(profile)
        encrypted_profile = EncryptedProfile(
            username=self._crypto_service.encrypt(profile.username),
            password=self._crypto_service.encrypt(profile.password),
            description=self._crypto_service.encrypt(profile.description)
        )
        self._profile_repository.insert(encrypted_profile)
