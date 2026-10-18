"""Escalation probe for the devcycle pipeline.

This module decides whether a deployment failure needs to be escalated
to the on-call owner or can be left for the pipeline to retry on its
own. Deployment checks consume the probe's status — exposed through
``get_probe()`` — to decide whether to escalate an incident or let the
pipeline proceed.

The status lives in the module-level constant ``PROBE_STATUS`` and is
returned unchanged by ``get_probe()``; ``_format_status()`` wraps that
accessor for call sites that want a display-ready string. Running the
module directly prints the current status to stdout:

    $ python -m devcycle.escalate_probe
    ready
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
