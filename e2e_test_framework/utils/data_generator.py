"""
Utility for generating random user data and test payloads.
"""
import random
import string

def random_email() -> str:
    """Generate a random email address."""
    user = ''.join(random.choices(string.ascii_lowercase, k=8))
    domain = ''.join(random.choices(string.ascii_lowercase, k=5))
    return f"{user}@{domain}.com"

def random_password(length: int = 12) -> str:
    """Generate a random password."""
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(chars, k=length))
