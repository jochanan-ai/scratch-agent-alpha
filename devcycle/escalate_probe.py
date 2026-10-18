"""Deployment probe for the devcycle pipeline.

Reports the current probe status consumed by deployment checks.
"""

PROBE_STATUS = 'ready'


def get_probe():
    """Return the probe status."""
    return PROBE_STATUS


if __name__ == '__main__':
    print(get_probe())
