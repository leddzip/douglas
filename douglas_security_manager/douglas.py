import click
from deafadder_container.MetaTemplate import Component

from douglas_security_manager.config.datastore import DataStoreComponent
from douglas_security_manager.config.context import ContextComponent
from douglas_security_manager.repositories.profile import ProfileRepository
from douglas_security_manager.services.crypto import CryptographyService
from douglas_security_manager.services.profile import ProfileService
from douglas_security_manager.model import Profile
from douglas_security_manager.repositories.setup import SetupRepository


def deafadder_init():
    # Configuration component
    ContextComponent()
    DataStoreComponent()
    # Repository component
    SetupRepository()
    ProfileRepository()
    # Service component
    CryptographyService()
    ProfileService()


@click.group()
@click.option("-d", "--db", "db_file", required=True, type=click.Path(exists=True, dir_okay=False))
@click.option("-p", "--password", "password", required=True, prompt="Master Password", hide_input=True, confirmation_prompt=False)
def douglas(db_file, password):
    context: ContextComponent = Component.get(ContextComponent)
    context.setup(password=password, data_file_path=db_file)


@douglas.command()
@click.option("-u", "--username", "profile_username", required=True, prompt="Profile username")
@click.option("-P", "--profile-password", "profile_password", required=True, prompt="Profile password", hide_input=True, confirmation_prompt=False)
@click.option("-D", "--description", "profile_description", required=False, prompt="Profile description", default="<none>")
def insert(profile_username, profile_password, profile_description):
    profile_service: ProfileService = Component.get(ProfileService)
    profile_service.create_new_profile(Profile(
        username=profile_username,
        password=profile_password,
        description=profile_description
    ))


if __name__ == "__main__":
    deafadder_init()
    douglas()
