from random import randint


def generate_secret_key(n: int = 30) -> str:
    """Generate secret key function."""
    return "".join(chr(randint(49, 123)) for _ in range(n))
