from StringIO import StringIO

from graver.advance import Advance
from graver.reader.xml_reader import XMLReader

advanceSource = XMLReader.parse(StringIO('<advance height="100" width="200" />'))


class TestAdvance(object):

    def test_has_width(self):
        advance = Advance(advanceSource)
        assert advance.width == 200

    def test_has_height(self):
        advance = Advance(advanceSource)
        assert advance.height == 100
