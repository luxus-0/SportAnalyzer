from datetime import datetime, UTC
from uuid import UUID, uuid4


class User:
    def __init__(
            self,
            user_id: UUID,
            email: str,
            username: str,
            password_hash: str,
            created_at: datetime,
            bio: str = ""
    ):
        self._id = user_id
        self._email = email
        self._username = username
        self._password_hash = password_hash
        self._created_at = created_at
        self._bio = bio

    @classmethod
    def create(cls, email: str, username: str, password_hash: str) -> 'User':
        return cls(
            user_id=uuid4(),
            email=email,
            username=username,
            password_hash=password_hash,
            created_at=datetime.now(UTC),
            bio=""
        )

    @property
    def id(self) -> UUID:
        return self._id

    @property
    def email(self) -> str:
        return self._email

    @property
    def username(self) -> str:
        return self._username

    @property
    def password_hash(self) -> str:
        return self._password_hash

    @property
    def created_at(self) -> datetime:
        return self._created_at

    @property
    def bio(self) -> str:
        return self._bio

    def update_bio(self, new_bio: str) -> None:
        if new_bio is None:
            raise ValueError("Bio is empty.")

        cleaned_bio = new_bio.strip()
        if len(cleaned_bio) > 500:
            raise ValueError("Bio should be max 500 characters.")

        self._bio = cleaned_bio

    def change_password(self, new_password_hash: str) -> None:
        if not new_password_hash:
            raise ValueError("Password is empty.")
        self._password_hash = new_password_hash
