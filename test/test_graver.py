import os

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

    def test_writes_glif2_file(self):
        from StringIO import StringIO

        output = StringIO()

        with graver.open('./test/fixtures/glif2.glif') as glif:
            glif.write(output)

        assert output.getvalue() == """<?xml version='1.0' encoding='utf-8'?>
<glyph format="2" name="period"><image fileName="period sketch.png" xScale="0.5" yScale="0.6" /><note /><lib /><outline><contour><point x="237" y="152" /><point x="193" y="187" /><point smooth="yes" type="curve" x="134" y="187" /><point x="74" y="187" /><point x="30" y="150" /><point smooth="yes" type="curve" x="30" y="88" /><point x="30" y="23" /><point x="74" y="-10" /><point smooth="yes" type="curve" x="134" y="-10" /><point x="193" y="-10" /><point x="237" y="25" /><point smooth="yes" type="curve" x="237" y="88" /></contour></outline><unicode hex="002E" /><advance width="268" /><anchor name="top" x="74" y="197" /><guideline name="overshoot" y="-12" /></glyph>"""
