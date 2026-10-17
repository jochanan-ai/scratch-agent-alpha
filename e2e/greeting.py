"""Minimal greeting helper for gateway-infra end-to-end checks."""


def greet(name):
    """Return a friendly greeting for *name*.

    Args:
        name: The name of the person or service to greet.

    Returns:
        A string of the form "Hello, <name>!".
    """
    return f"Hello, {name}!"


if __name__ == '__main__':
    print(greet("gateway-infra"))
