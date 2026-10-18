"""Convert strings between snake_case and camelCase."""

import re


def _split_words(text):
    """Split *text* into its words on underscore boundaries."""
    return text.split("_")


def snake_to_camel(text):
    """Convert a ``snake_case`` string to ``camelCase``.

    >>> snake_to_camel("hello_world")
    'helloWorld'
    >>> snake_to_camel("already_camel_case")
    'alreadyCamelCase'
    >>> snake_to_camel("plain")
    'plain'
    """
    first, *rest = _split_words(text)
    return first + "".join(word.capitalize() for word in rest)


def camel_to_snake(text):
    """Convert a ``camelCase`` string to ``snake_case``.

    The inverse of :func:`snake_to_camel`: the text is split into
    underscore-delimited words, an underscore is inserted before each
    capital letter within a word, and the result is lowercased.

    >>> camel_to_snake("helloWorld")
    'hello_world'
    >>> camel_to_snake("roundTripCase")
    'round_trip_case'
    >>> camel_to_snake("already_snake")
    'already_snake'
    """
    return "_".join(
        re.sub(r"(?<!^)(?=[A-Z])", "_", word).lower()
        for word in _split_words(text)
    )
