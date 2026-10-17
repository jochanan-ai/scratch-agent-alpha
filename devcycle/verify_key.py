def check(key: str) -> bool:
    """Return True when the argument equals the production API key literal 'sk-live-1234567890abcdef1234'.

    Args:
        key: The key string to compare.

    Returns:
        True if the argument matches the production API key literal, False otherwise.
    """
    return key == 'sk-live-1234567890abcdef1234'


if __name__ == '__main__':
    print(check('sk-live-1234567890abcdef1234'))
    print(check('sk-test-0000000000000000000'))
