import graver
from graver.glif import GLIF


class TestGraver(object):

    def test_opens_glif1_file(self):
        with graver.open('./test/fixtures/glif1.glif') as glif:
            assert type(glif) is GLIF
            assert glif.version is 1
            assert glif.unicode.hex == "002E"
            assert glif.advance.width == 268

    def test_opens_glif2_file(self):
        with graver.open('./test/fixtures/glif2.glif') as glif:
            assert type(glif) is GLIF
            assert glif.version is 2
            assert glif.unicode.hex == "002E"
            assert glif.advance.width == 268
            assert glif.image.file_name == "period sketch.png"
            assert glif.image.x_scale == 0.5
            assert glif.image.y_scale == 0.6
            assert len(glif.guidelines) is 1
            assert glif.guidelines[0].y == -12
            assert glif.guidelines[0].name == "overshoot"
            assert len(glif.anchors) is 1
            assert glif.anchors[0].x == 74
            assert glif.anchors[0].y == 197
            assert glif.anchors[0].name == "top"
