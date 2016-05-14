from StringIO import StringIO

from graver.image import Image
from graver.reader.xml_reader import XMLReader

imageSource = XMLReader.parse(StringIO('<image fileName="Sketch 1.png" \
    xOffset="100" yOffset="200" xScale=".78" yScale=".75" color="1,0,0,.5" \
    xyScale="1.75" yxScale="-1.6" />'))


class TestImage(object):

    def test_has_file_name(self):
        image = Image(imageSource)
        assert image.file_name == "Sketch 1.png"

    def test_has_x_offset(self):
        image = Image(imageSource)
        assert image.x_offset == 100

    def test_has_y_offset(self):
        image = Image(imageSource)
        assert image.y_offset == 200

    def test_has_x_scale(self):
        image = Image(imageSource)
        assert image.x_scale == 0.78

    def test_has_y_scale(self):
        image = Image(imageSource)
        assert image.y_scale == 0.75

    def test_has_xy_scale(self):
        image = Image(imageSource)
        assert image.xy_scale == 1.75

    def test_has_yx_scale(self):
        image = Image(imageSource)
        assert image.yx_scale == -1.6

    def test_has_color(self):
        image = Image(imageSource)
        assert image.color == "1,0,0,.5"
