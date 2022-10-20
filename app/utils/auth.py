import jwt
from fastapi import HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from passlib.context import CryptContext
from datetime import datetime, timedelta

class AuthHandler():
    security = HTTPBearer()
    pass_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    secret = "SECRET"

    def get_password_hash(self, password):
        return self.pass_context.hash(password)

    def verify_password(self, plain_password, hashed_password):
        return self.pass_context.verify(plain_password, hashed_password)

    def encode_token(self, user_id):
        payload = {
            'exp' : datetime.utcnow() + timedelta(days=0, minutes=5),
            'iat' : datetime.utcnow(),
            'sub' : user_id
        }
        return jwt.encode(
            payload,
            self.secret,
            algorithm='HS256'
        )

    def decode_token(self, token):
        try:
            payload = jwt.decode(token, self.secret, algorithms=['HS256'])
            return payload['sub']
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail='Token Expirado.')
        except jwt.InvalidTokenError as e:
            raise HTTPException(status_code=401, detail="Token Ivalido.")

    
    def auth_wrapper(self, auth:HTTPAuthorizationCredentials = Security(security)):
        return self.decode_token(auth.credentials)
