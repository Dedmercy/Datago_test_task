from fastapi import Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordBearer
from jose import jwt

from app.config import settings
from app.schemas.auth import ClaimSchema

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login",
    scheme_name="JWT"
)


class JWTAuth:

    @classmethod
    def create_access_token(cls, account: ClaimSchema):
        """
            Creating access token
        """
        try:
            claims = jsonable_encoder(account)

            return jwt.encode(claims=claims, key=settings.jwt_secret, algorithm=settings.jwt_algorithm)

        except Exception:
            raise

    @classmethod
    def verify_access_token(cls, token: str = Depends(oauth2_scheme)):
        """
            Verifying access token
        """
        try:
            payload = jwt.decode(token, key=settings.jwt_secret)
            return payload
        except Exception:
            raise HTTPException(
                status_code=403,
                detail=f"Wrong authentication"
            )
