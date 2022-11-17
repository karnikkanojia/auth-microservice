import jwt
import datetime
import os

def createJWT(username, secret, authz):
    return jwt.encode(
        {
            "username": username,
            "exp": datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(days=1),
            "iat": datetime.datetime.utcnow(),
            "admin": authz
        },
        secret,
        algorithm="HS256",
    )

def decodeJWT(encoded_jwt, algorithms):
    return jwt.decode(
        encoded_jwt, os.environ.get("JWT_SECRET"), algorithms=algorithms
    )
