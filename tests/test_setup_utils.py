"""Fiji installation checks on synthetic directory layouts"""
from pysnt.setup_utils import check_fiji_installation


def _layout(root, launchers=("fiji",), snt=True, bundle=False):
    (root / "jars").mkdir(parents=True)
    (root / "plugins").mkdir()
    for name in launchers:
        (root / name).write_text("")
    if snt:
        (root / "jars" / "SNT-5.0.24.jar").write_text("")
    if bundle:
        (root / "Fiji.app").mkdir()
    return root


def test_jaunch_layout_with_launcher_bundle(tmp_path):
    root = _layout(tmp_path / "Fiji", launchers=("fiji", "fiji.bat"), bundle=True)
    status = check_fiji_installation(str(root))
    assert status["is_fiji"] and status["has_snt"]


def test_windows_batch_launcher_only(tmp_path):
    root = _layout(tmp_path / "Fiji", launchers=("fiji.bat",))
    assert check_fiji_installation(str(root))["is_fiji"]


def test_launcher_bundle_alone_is_enough(tmp_path):
    root = _layout(tmp_path / "Fiji", launchers=(), bundle=True)
    assert check_fiji_installation(str(root))["is_fiji"]


def test_bundle_directory_itself_is_not_an_install(tmp_path):
    """Pointing at the nested Fiji.app launcher bundle (no jars) is not an install root"""
    bundle = tmp_path / "Fiji" / "Fiji.app"
    bundle.mkdir(parents=True)
    assert not check_fiji_installation(str(bundle))["is_fiji"]


def test_missing_snt_jar_is_flagged(tmp_path):
    root = _layout(tmp_path / "Fiji", snt=False)
    status = check_fiji_installation(str(root))
    assert not status["is_fiji"] and not status["has_snt"]
