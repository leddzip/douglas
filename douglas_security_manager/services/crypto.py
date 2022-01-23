import base64
import secrets
from base64 import urlsafe_b64encode as b64e, urlsafe_b64decode as b64d

from cryptography.fernet import Fernet
from cryptography.hazmat.backends import Backend, default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from deafadder_container.MetaTemplate import Component

from douglas_security_manager.config.context import ContextComponent


ITERATION = 100_000


class CryptographyService(metaclass=Component):

    _context: ContextComponent
    _backend: Backend
    _iterations: int

    def __init__(self, iteration: int = ITERATION):
        self._iterations = iteration
        self._backend = default_backend()

    def _derive_key(self, salt: bytes) -> bytes:
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=self._iterations,
            backend=self._backend)
        return b64e(kdf.derive(self._context.password.encode()))

    def encrypt(self, message: str) -> str:
        """
        Encrypt a given message using the user password from the context.

        :param message: the message to encrypt.
        :return: a token (str) containing the encrypted message.
        """
        salt = secrets.token_bytes(16)
        key = self._derive_key(salt)
        return b64e(
            b'%b%b%b' % (
                salt,
                self._iterations.to_bytes(4, 'big'),
                b64e(Fernet(key).encrypt(message.encode()))
            )
        ).decode()

    def decrypt(self, token: str) -> str:
        """
        Decrypt a given token (encrypted message) using hte user password
        from teh context.

        :param token: a string containing the encrypted message
        :return: the original message (str)
        """
        decoded = b64d(token.encode())
        salt, iter_temp, token = decoded[:16], decoded[16:20], b64e(decoded[20:])
        key = self._derive_key(salt)
        return Fernet(key).decrypt(token).decode()
