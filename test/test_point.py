from StringIO import StringIO

from graver.point import Point
from graver.reader.xml_reader import XMLReader

pointSource = XMLReader.parse(StringIO('<point y="-12" x="4" type="move" smooth="yes" name="initial" identifier="x1234" />'))


class TestPoint(object):

    def test_has_y(self):
        point = Point(pointSource)
        assert point.y == -12

    def test_has_x(self):
        point = Point(pointSource)
        assert point.x == 4

    def test_has_name(self):
        point = Point(pointSource)
        assert point.name == "initial"

    def test_has_type(self):
        point = Point(pointSource)
        assert point.type == "move"

    def test_has_smooth(self):
        point = Point(pointSource)
        assert point.smooth == "yes"

    def test_has_identifier(self):
        point = Point(pointSource)
        assert point.identifier == "x1234"
