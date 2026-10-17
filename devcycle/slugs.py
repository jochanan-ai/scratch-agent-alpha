import re


def slugify(text):
    """Return a URL-friendly slug for *text*.

    Lowercases the input and replaces every run of one or more
    non-alphanumeric characters with a single hyphen, then strips
    leading and trailing hyphens.
    """
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
