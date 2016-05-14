from StringIO import StringIO

from graver.component import Component
from graver.reader.xml_reader import XMLReader

componentSource = XMLReader.parse(StringIO('<component base="a" \
    xOffset="100" yOffset="200" xScale=".78" yScale=".75" \
    xyScale="1.75" yxScale="-1.6" identifier="x1234" />'))


class TestComponent(object):

    def test_has_file_name(self):
        component = Component(componentSource)
        assert component.base == "a"

    def test_has_x_offset(self):
        component = Component(componentSource)
        assert component.x_offset == 100

    def test_has_y_offset(self):
        component = Component(componentSource)
        assert component.y_offset == 200

    def test_has_x_scale(self):
        component = Component(componentSource)
        assert component.x_scale == 0.78

    def test_has_y_scale(self):
        component = Component(componentSource)
        assert component.y_scale == 0.75

    def test_has_xy_scale(self):
        component = Component(componentSource)
        assert component.xy_scale == 1.75

    def test_has_yx_scale(self):
        component = Component(componentSource)
        assert component.yx_scale == -1.6

    def test_has_identifier(self):
        component = Component(componentSource)
        assert component.identifier == "x1234"
