import pytest

from graver.versioned import VersionAccessError
from graver.glif import GLIF


class TestGLIF(object):

    def test_glif_has_a_version(self):
        assert GLIF(version=2).version is 2

    def test_glif1_has_advance_property(self):
        assert GLIF(version=1).advance is not None
