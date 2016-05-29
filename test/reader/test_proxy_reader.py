from StringIO import StringIO

from graver.reader.xml_reader import XMLReader
from graver.reader.proxy_reader import ProxyReader

source = XMLReader.parse(StringIO('<advance height="100" width="200" />'))


class TestAdvance(object):

    def test_reads_attribute(self):
        proxy = ProxyReader(source)
        assert proxy.attribute('height') == "100"

    def test_reads_missing_attribute(self):
        proxy = ProxyReader(source)
        assert proxy.attribute('foobar') == None

    def test_coerces_attribute_as_type(self):
        proxy = ProxyReader(source)
        assert proxy.attribute('height', int) == 100

    def test_returns_none_for_missing_coerced_type(self):
        proxy = ProxyReader(source)
        assert proxy.attribute('foobar', int) is None
