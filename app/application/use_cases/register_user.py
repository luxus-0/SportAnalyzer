from dataclasses import dataclass

from app.application.interfaces.password_hasher import PasswordHasher
from app.domain.user import User
from app.domain.user_repository import UserRepository

@dataclass
class RegisterUserRequest:
    email: str
    username: str
    password: str


class RegisterUser:

    def __init__(self, user_repository: UserRepository, password_hasher: PasswordHasher):
        self.user_repository = user_repository
        self.password_hasher = password_hasher

    def execute(self, request: RegisterUserRequest) -> None:

        if self.user_repository.exists_by_email(request.email):
            raise ValueError("Email already exists")

        if self.user_repository.exists_by_username(request.username):
            raise ValueError("Username already exists")

        hashed_password = self.password_hasher.hash(request.password)

        new_user = User.create(
            email=request.email,
            username=request.username,
            password_hash=hashed_password
        )

        self.user_repository.save(new_user)