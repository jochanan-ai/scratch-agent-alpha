"""Convert snake_case strings to camelCase."""


def snake_to_camel(text):
    """Convert a ``snake_case`` string to ``camelCase``."""
    first, *rest = text.split("_")
    return first + "".join(word.capitalize() for word in rest)
