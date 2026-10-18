import os

PIN_ENV_VAR = 'DEVCYCLE_PIN'


def get_pin():
    """Return the deployment PIN.

    The PIN is read from the DEVCYCLE_PIN environment variable and is
    never hardcoded in source. Returns an empty string when the variable
    is unset or empty.
    """
    return os.environ.get(PIN_ENV_VAR, '')


if __name__ == '__main__':
    print(get_pin())
