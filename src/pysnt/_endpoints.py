"""
Maven endpoints used by pysnt.initialize() when no Fiji installation is requested.

PySNT versions map to SNT versions by major.minor (PySNT 5.1.x targets SNT 5.1.x);
patch levels are independent. Bump DEFAULT_SNT_VERSION when cutting a PySNT release.
"""

import os
from typing import List, Optional

SNT_GROUP_ARTIFACT = "org.morphonets:SNT"

# SNT version resolved from Maven Central/SciJava when none is requested.
DEFAULT_SNT_VERSION = "5.0.24-SNAPSHOT"

# Optional runtime dependencies that are not declared by SNT's pom (provided by
# Fiji when running against a Fiji install). Bvv/Bdv curated classes need them.
# NB: verify coordinates/versions with `mvn dependency:tree` before release.
DEFAULT_EXTRA_ENDPOINTS: List[str] = [
    "sc.fiji:bigvolumeviewer",
]

ENV_SNT_VERSION = "SNT_VERSION"


def resolve_snt_version(snt_version: Optional[str] = None) -> str:
    """Explicit argument > SNT_VERSION environment variable > DEFAULT_SNT_VERSION."""
    return snt_version or os.environ.get(ENV_SNT_VERSION) or DEFAULT_SNT_VERSION


def build_endpoints(snt_version: Optional[str] = None,
                    extras: Optional[List[str]] = None) -> List[str]:
    """
    Return the Maven endpoint list for pyimagej: SNT (pinned) plus extras.

    extras=None adds DEFAULT_EXTRA_ENDPOINTS; extras=[] adds nothing; any other
    list replaces the defaults.
    """
    endpoints = [f"{SNT_GROUP_ARTIFACT}:{resolve_snt_version(snt_version)}"]
    endpoints.extend(DEFAULT_EXTRA_ENDPOINTS if extras is None else extras)
    return endpoints
