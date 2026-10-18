"""Escalation probe for the devcycle pipeline.

Determines whether a deployment failure needs to be escalated to the
on-call owner. ``get_probe()`` exposes the current probe status, which
deployment checks consume to decide whether to escalate an incident or
let the pipeline proceed.
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
