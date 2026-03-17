import uuid
from dataclasses import dataclass

from app.application.interfaces.password_hasher import PasswordHasher
from app.domain.email import Email
from app.domain.exceptions.UserAlreadyExistsException import UserAlreadyExistsException
from app.domain.password_hash import EventBus
from app.domain.user import User
from app.domain.user_id import UserId
from app.domain.user_repository import UserRepository
from app.domain.username import Username


@dataclass
class RegisterUserCommand:
    email: str
    username: str
    password: str


class RegisterUser:

    def __init__(self,
                 user_repository: UserRepository,
                 password_hasher: PasswordHasher,
                 event_bus: EventBus):
        self.user_repository = user_repository
        self.password_hasher = password_hasher,
        self.event_bus = event_bus


    def register(self, user_command: RegisterUserCommand) -> UserId:
        email = Email(user_command.email)
        username = Username(user_command.username)

        if self.user_repository.get_by_email(email):
            raise UserAlreadyExistsException(f"Email {email} already exists.")

        password_hash = self.password_hasher.hash(user_command.password)

        user = self.register_user(email, password_hash, username)

        self.save_user_to_database(user, username)

        events = user.pull_events()
        self.event_bus.publish(events)

        return user.id

    def register_user(self, email, password_hash, username):
        user = User.register(
            user_id=UserId(uuid.uuid4()),
            email=email,
            username=username,
            password_hash=password_hash
        )
        return user

    def save_user_to_database(self, user, username):
        try:
            self.user_repository.save(user)
        except UserAlreadyExistsException:
            raise UserAlreadyExistsException(f'User {username} already exists')
