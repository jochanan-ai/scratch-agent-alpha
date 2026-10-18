"""Multi-repo parallel-cycle probe for the gateway-infra factory.

This module is the probe shipped with the alpha repo; it is executed
concurrently with the probes from the other repos to prove the factory
can build each one in parallel within a single cycle.
"""


def repo_slug():
    """Return this repo's slug in the multi-repo cycle.

    Returns:
        str: The slug "alpha".
    """
    return "alpha"
