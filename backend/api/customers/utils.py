import bcrypt


def hash_password(password: str) -> tuple[str, str]:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    password_hash = hashed.replace(salt, b"")
    return salt.decode(), password_hash.decode()


def check_password(password: str, salt: str, password_hash: str) -> bool:
    return bcrypt.checkpw(password.encode(), (salt + password_hash).encode())
