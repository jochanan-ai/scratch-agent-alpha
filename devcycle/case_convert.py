"""Convert strings between snake_case and camelCase."""

import re


def snake_to_camel(text):
    """Convert a ``snake_case`` string to ``camelCase``."""
    first, *rest = text.split("_")
    return first + "".join(word.capitalize() for word in rest)


def camel_to_snake(text):
    """Convert a ``camelCase`` string to ``snake_case``.

    The inverse of :func:`snake_to_camel`: an underscore is inserted
    before each capital letter (except a leading one) and the result
    is lowercased.
    """
    return re.sub(r"(?<!^)(?=[A-Z])", "_", text).lower()
