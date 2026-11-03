"""
Maven endpoints used by pysnt.initialize() when no Fiji installation is requested.

PySNT versions map to SNT versions by major.minor (PySNT 5.1.x targets SNT 5.1.x);
patch levels are independent. Bump DEFAULT_SNT_VERSION when cutting a PySNT release.
"""

import os
import platform
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

# JogAmp (jogl/gluegen) natives, needed by Viewer3D. Maven resolution does not
# add them on its own (Fiji ships them in jars/), so we request the ones for the
# running platform. Keep JOGAMP_VERSION equal to the version managed by SNT's pom
JOGAMP_VERSION = "2.6.0"
_JOGAMP_ARTIFACTS = ("org.jogamp.gluegen:gluegen-rt", "org.jogamp.jogl:jogl-all")


def _jogamp_natives_classifier() -> Optional[str]:
    """JogAmp natives classifier for this platform, or None if none is published."""
    system = platform.system()
    machine = platform.machine().lower()
    if system == "Darwin":
        return "natives-macosx-universal"  # arm64 and x86_64 share one jar
    if system == "Linux":
        if machine in ("x86_64", "amd64"):
            return "natives-linux-amd64"
        if machine in ("aarch64", "arm64"):
            return "natives-linux-aarch64"
    if system == "Windows" and machine in ("amd64", "x86_64"):
        return "natives-windows-amd64"
    return None


def jogamp_natives_endpoints() -> List[str]:
    """Maven endpoints for the JogAmp natives of this platform (empty if unsupported)."""
    classifier = _jogamp_natives_classifier()
    if classifier is None:
        return []
    return [f"{ga}:{JOGAMP_VERSION}:{classifier}" for ga in _JOGAMP_ARTIFACTS]


def resolve_snt_version(snt_version: Optional[str] = None) -> str:
    """Explicit argument > SNT_VERSION environment variable > DEFAULT_SNT_VERSION."""
    return snt_version or os.environ.get(ENV_SNT_VERSION) or DEFAULT_SNT_VERSION


def build_endpoints(snt_version: Optional[str] = None,
                    extras: Optional[List[str]] = None) -> List[str]:
    """
    Return the Maven endpoint list for pyimagej: SNT (pinned) plus extras and
    the JogAmp natives of this platform.

    extras=None adds DEFAULT_EXTRA_ENDPOINTS; extras=[] adds nothing; any other
    list replaces the defaults. The natives are always added.
    """
    endpoints = [f"{SNT_GROUP_ARTIFACT}:{resolve_snt_version(snt_version)}"]
    endpoints.extend(DEFAULT_EXTRA_ENDPOINTS if extras is None else extras)
    endpoints.extend(jogamp_natives_endpoints())
    return endpoints
