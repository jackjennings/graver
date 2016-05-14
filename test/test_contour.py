from StringIO import StringIO

from graver.contour import Contour
from graver.collection import Collection
from graver.reader.xml_reader import XMLReader

contourSource = XMLReader.parse(StringIO('<contour identifier="x1234"></contour>'))


class TestContour(object):

    def test_contour_has_points(self):
        contour = Contour(contourSource)
        assert type(contour.points) is Collection

    def test_contour_has_identifier(self):
        contour = Contour(contourSource)
        assert contour.identifier == "x1234"
