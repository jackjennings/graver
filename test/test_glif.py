import pytest

from graver.versioned import VersionAccessError
from graver.glif import GLIF
from graver.collection import Collection
from graver.name import Name
from graver.format import Format
from graver.advance import Advance
from graver.unicode import Unicode
from graver.outline import Outline
from graver.lib import Lib
from graver.note import Note
from graver.image import Image
from graver.guideline import Guideline
from graver.anchor import Anchor


class TestGLIF(object):

    def test_glif_has_a_version(self):
        assert GLIF(version=2).version is 2

    def test_glif1_has_advance_property(self):
        assert GLIF(version=1).advance is Advance

    def test_glif1_has_name_property(self):
        assert type(GLIF(version=1).name) is Name

    def test_glif1_has_format_property(self):
        assert type(GLIF(version=1).format) is Format

    def test_glif1_has_advance_property(self):
        assert type(GLIF(version=1).advance) is Advance

    def test_glif1_has_unicode_property(self):
        assert type(GLIF(version=1).unicode) is Unicode

    def test_glif1_has_outline_property(self):
        assert type(GLIF(version=1).outline) is Outline

    def test_glif1_has_lib_property(self):
        assert type(GLIF(version=1).lib) is Lib

    def test_glif2_has_advance_property(self):
        assert GLIF(version=2).advance is Advance

    def test_glif2_has_name_property(self):
        assert type(GLIF(version=2).name) is Name

    def test_glif2_has_format_property(self):
        assert type(GLIF(version=2).format) is Format

    def test_glif2_has_advance_property(self):
        assert type(GLIF(version=2).advance) is Advance

    def test_glif2_has_unicode_property(self):
        assert type(GLIF(version=2).unicode) is Unicode

    def test_glif2_has_outline_property(self):
        assert type(GLIF(version=2).outline) is Outline

    def test_glif2_has_lib_property(self):
        assert type(GLIF(version=2).lib) is Lib

    def test_glif2_has_note_property(self):
        assert type(GLIF(version=2).note) is Note

    def test_glif2_has_image_property(self):
        assert type(GLIF(version=2).image) is Image

    def test_glif2_has_guidelines_property(self):
        assert type(GLIF(version=2).guidelines) is Collection

    def test_glif2_has_anchors_property(self):
        assert type(GLIF(version=2).anchors) is Collection

    def test_glif_sets_format_to_version(self):
        assert GLIF(version=2).format == 2

    def test_equality_of_glif_objects(self):
        assert GLIF(version=2) == GLIF(version=2)

    def test_inequality_of_glif_objects(self):
        assert GLIF(version=2) != GLIF(version=1)

    def test_converts_version(self):
        glif1 = GLIF(version=2)
        glif2 = glif1.as_version(2)
        assert glif2.version == 2
        assert glif2.format == 2

    def test_should_be_a_clone_after_version_conversion(self):
        glif1 = GLIF(version=2)
        glif2 = glif1.as_version(2)
        assert glif1 is not glif2
