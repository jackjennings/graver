from StringIO import StringIO

from graver.guideline import Guideline
from graver.reader.xml_reader import XMLReader

guidelineSource = XMLReader.parse(StringIO('<guideline y="-12" x="4" name="overshoot" color="0,0,0" identifier="x1234" angle="90" />'))


class TestGuideline(object):

    def test_has_y(self):
        guideline = Guideline(guidelineSource)
        assert guideline.y == -12

    def test_has_x(self):
        guideline = Guideline(guidelineSource)
        assert guideline.x == 4

    def test_has_angle(self):
        guideline = Guideline(guidelineSource)
        assert guideline.angle == 90

    def test_has_name(self):
        guideline = Guideline(guidelineSource)
        assert guideline.name == "overshoot"

    def test_has_color(self):
        guideline = Guideline(guidelineSource)
        assert guideline.color == "0,0,0"

    def test_has_identifier(self):
        guideline = Guideline(guidelineSource)
        assert guideline.identifier == "x1234"
