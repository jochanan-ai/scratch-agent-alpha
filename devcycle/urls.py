def normalize_url(url):
    """Strip a trailing '/' from an http(s) URL.

    URLs with an ``http://`` or ``https://`` scheme have a single
    trailing '/' removed; the scheme itself is never touched. Any
    other value -- a non-http(s) URL, a bare scheme like ``http://``,
    or a non-string -- is returned unchanged.
    """
    if not isinstance(url, str) or not url.startswith(("http://", "https://")):
        return url
    scheme, _, rest = url.partition("://")
    if rest == "/" or not rest.endswith("/"):
        return url
    return scheme + "://" + rest[:-1]
