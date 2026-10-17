def count_words(text):
    """Return the number of whitespace-separated words in *text*.

    Runs of consecutive whitespace (spaces, tabs, newlines) count as a
    single separator, and leading/trailing whitespace is ignored.

    >>> count_words("hello world")
    2
    >>> count_words("  a\\tb\\n\\nc ")
    3
    >>> count_words("")
    0
    """
    return len(text.split())
