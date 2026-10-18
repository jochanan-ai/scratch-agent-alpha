"""Flatten a nested dict one level deep, joining keys with a dot."""


def flatten_one_level(mapping):
    """Return a copy of ``mapping`` flattened one level deep.

    Dict values are expanded so each child appears as ``"<key>.<child>"``;
    every non-dict value (including empty dicts) passes through unchanged.
    """
    flattened = {}
    for key, value in mapping.items():
        if isinstance(value, dict) and value:
            for child_key, child_value in value.items():
                flattened[f"{key}.{child_key}"] = child_value
        else:
            flattened[key] = value
    return flattened
