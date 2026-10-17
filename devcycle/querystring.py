from urllib.parse import urlencode


def build_query(params: dict) -> str:
    """Return a urlencoded query string built from *params*.

    The result has no leading ``?``. Parameters whose value is
    ``None`` are skipped, and pairs are emitted sorted by key so the
    output is deterministic. Sequence values (e.g. lists) are encoded
    as repeated keys via ``doseq=True``.
    """
    filtered = {key: value for key, value in params.items() if value is not None}
    return urlencode(sorted(filtered.items()), doseq=True)
