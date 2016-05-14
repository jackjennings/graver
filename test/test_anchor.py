from StringIO import StringIO

from graver.anchor import Anchor
from graver.reader.xml_reader import XMLReader

anchorSource = XMLReader.parse(StringIO('<anchor y="-12" x="4" name="overshoot" color="0,0,0" identifier="x1234" />'))


class TestAnchor(object):

    def test_has_y(self):
        anchor = Anchor(anchorSource)
        assert anchor.y == -12

    def test_has_x(self):
        anchor = Anchor(anchorSource)
        assert anchor.x == 4

    def test_has_name(self):
        anchor = Anchor(anchorSource)
        assert anchor.name == "overshoot"

    def test_has_color(self):
        anchor = Anchor(anchorSource)
        assert anchor.color == "0,0,0"

    def test_has_identifier(self):
        anchor = Anchor(anchorSource)
        assert anchor.identifier == "x1234"
