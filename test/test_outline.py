from StringIO import StringIO

from graver.outline import Outline
from graver.collection import Collection
from graver.reader.xml_reader import XMLReader

outlineSource = XMLReader.parse(StringIO('<outline> \
        <component /> \
        <contour /> \
    </outline>'))


class TestOutline(object):

    def test_outline_has_components(self):
        outline = Outline(outlineSource)
        assert type(outline.components) is Collection

    def test_outline_has_contours(self):
        outline = Outline(outlineSource)
        assert type(outline.contours) is Collection
