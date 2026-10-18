"""Farewell helper used by the demo CLI.

Provides :func:`goodbye`, which builds a friendly farewell message
for a given name.
"""

FAREWELL_SUFFIX = '!'


def goodbye(name):
    return "Goodbye, " + name + FAREWELL_SUFFIX
