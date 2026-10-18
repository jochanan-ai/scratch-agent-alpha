"""Deployment probe for the devcycle pipeline.

Reports the current probe status consumed by deployment checks.
"""

PROBE_STATUS = 'ready'


def get_probe():
    """Return the probe status."""
    return PROBE_STATUS


def _format_status():
    """Return the formatted probe status string for reuse by call sites."""
    return get_probe()


if __name__ == '__main__':
    print(_format_status())
