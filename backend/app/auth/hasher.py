from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hasher:

    @classmethod
    def get_hashed_password(cls, password: str) -> str:
        """
            Get hash from password
        """
        return pwd_context.hash(password)

    @classmethod
    def verify_password(cls, plain_password: str, input_password: str) -> bool:
        """
            Verifying the entered password
        """
        return pwd_context.verify(plain_password, input_password)
