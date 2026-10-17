import hmac
import os

ENV_VAR = 'DEVCYCLE_API_KEY'


def check(key: str) -> bool:
    """Return True when the argument matches the expected API key.

    The expected key is read from the DEVCYCLE_API_KEY environment variable
    and is never hardcoded in source or written to output.

    Args:
        key: The key string to verify.

    Returns:
        True if the argument matches the expected key, False otherwise
        (including when the environment variable is unset or empty).
    """
    expected = os.environ.get(ENV_VAR)
    if not expected:
        return False
    return hmac.compare_digest(key, expected)
