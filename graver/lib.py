from xml.etree import ElementTree

from reader.proxy_reader import ProxyReader
from reader.plist_reader import PlistReader


class Lib(ProxyReader):

    def __init__(self, source):
        self.reader = PlistReader.parse(source)

    def __getitem__(self, key):
        return self.attribute(key)
