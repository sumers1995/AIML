from datetime import datetime, timedelta
import jwt
from config import sec_settings


def generate_token(emp) -> str:
    return jwt.encode(payload={
            "employee":{"name": emp.name, "email": emp.email},
            "exp": datetime.now() + timedelta(minutes=15)},
            algorithm=sec_settings.JWT_ALGORITHM,
            key=sec_settings.JWT_SECRET)

def decode_token(token: str) -> dict | None:
    try:
        return jwt.decode(
            jwt=token,
            algorithms=[sec_settings.JWT_ALGORITHM],
            key=sec_settings.JWT_SECRET
        )
    except jwt.PyJWTError:
        return None