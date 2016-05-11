import graver
from graver.glif import GLIF


class TestGraver(object):

    def test_opens_glif1_file(self):
        glif = graver.open('./test/fixtures/glif1.glif')
        assert type(glif) is GLIF
        assert glif.version is 1
        assert glif.unicode.hex == "002E"
        assert glif.advance.width == 268

    def test_opens_glif2_file(self):
        glif = graver.open('./test/fixtures/glif2.glif')
        assert type(glif) is GLIF
        assert glif.version is 2
        assert glif.unicode.hex == "002E"
        assert glif.advance.width == 268
        assert glif.image.file_name == "period sketch.png"
        assert glif.image.x_scale == 0.5
        assert glif.image.y_scale == 0.6
