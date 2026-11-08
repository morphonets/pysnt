"""Platform helpers shared by PySNT modules."""

import platform
import sysconfig


def python_arch() -> str:
    """
    Architecture of the running Python interpreter (lowercase, e.g. 'arm64', 'x86_64', 'amd64').

    On Windows, platform.machine() reports the CPU of the host for emulated processes: an x64 Python running on
    Windows ARM (e.g., in a VM on Apple Silicon) reports 'ARM64'. What matters for the in-process JVM and for
    its native libraries is the architecture the interpreter was built for, which sysconfig knows.
    """
    machine = platform.machine().lower()
    if platform.system() == "Windows":
        built = {"win-amd64": "amd64", "win-arm64": "arm64", "win32": "x86"}.get(sysconfig.get_platform())
        if built:
            return built
    return machine
