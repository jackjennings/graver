from StringIO import StringIO

from graver.unicode import Unicode
from graver.reader.xml_reader import XMLReader

unicodeSource = XMLReader.parse(StringIO('<unicode hex="002E" />'))


class TestUnicode(object):

    def test_has_hex(self):
        unicode = Unicode(unicodeSource)
        assert unicode.hex == '002E'
