import bcrypt

from app.application.interfaces.password_hasher import PasswordHasher


class BcryptPasswordHasher(PasswordHasher):

    def hash(self, plain_password: str) -> str:
        password_bytes = plain_password.encode('utf-8')

        salt = bcrypt.gensalt()
        hashed_bytes = bcrypt.hashpw(password_bytes, salt)

        return hashed_bytes.decode('utf-8')

    def verify(self, plain_password: str, hashed_password: str) -> bool:
        password_bytes = plain_password.encode('utf-8')
        hashed_bytes = hashed_password.encode('utf-8')

        return bcrypt.checkpw(password_bytes, hashed_bytes)
