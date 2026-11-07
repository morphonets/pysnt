"""
JVM options that PySNT always passes to the JVM it starts.

Fiji's launcher passes JVM options of its own (and unlocks modules through the SciJava app-launcher), but PySNT
starts a bare JVM through JPype and so has to pass what SNT needs itself. All options live in the single table
below: one entry per option, with the platforms it applies to and the reason it is needed.
User-specific options go through ``pysnt.initialize(jvm_args=[...])``.
"""

import platform
from typing import List, NamedTuple, Optional, Tuple


class JvmOption(NamedTuple):
    option: str
    systems: Optional[Tuple[str, ...]]  # platform.system() values (e.g. "Darwin"); None means all platforms
    reason: str


JVM_OPTIONS: Tuple[JvmOption, ...] = (
    JvmOption(
        "--add-opens=java.base/java.lang=ALL-UNNAMED", None,
        "Java 17+ blocks the bytecode patching that ImageJ1 needs unless java.lang is opened. pyimagej adds "
        "this itself, but only if it can parse the requested Java version, which fails for a constraint such "
        "as '21+' ('Failed to guess the Java version.') and then surfaces as "
        "'Invalid service: net.imagej.legacy.LegacyService'"),
    JvmOption(
        "--enable-native-access=ALL-UNNAMED", None,
        "JPype loads a native library: Java 24+ warns about it unless native access is enabled"),
    JvmOption(
        "--add-opens=java.desktop/com.apple.eawt=ALL-UNNAMED", ("Darwin",),
        "ImageJ1 (IJ1Helper) reflectively accesses com.apple.eawt (dock icon, menu bar) when the legacy GUI is "
        "initialized ('gui'/'interactive' modes). Without it: 'IllegalAccessException: ... module java.desktop "
        "does not export com.apple.eawt'"),
    JvmOption(
        "--add-exports=java.desktop/sun.awt=ALL-UNNAMED", ("Darwin",),
        "JOGL (Viewer3D, Tree.show3D()) reflectively accesses sun.awt.AppContext ('AppContextInfo Bug 1004'). "
        "Without it the OpenGL layer is not attached and the viewer window does not display"),
    JvmOption(
        "--add-opens=java.desktop/sun.awt=ALL-UNNAMED", ("Darwin",),
        "Same as above (JOGL AppContextInfo): deep reflective access to sun.awt"),
)


def applicable_jvm_options(system: Optional[str] = None) -> List[str]:
    """Returns the options from JVM_OPTIONS that apply to ``system`` (default: the running platform)."""
    system = system or platform.system()
    return [o.option for o in JVM_OPTIONS if o.systems is None or system in o.systems]
