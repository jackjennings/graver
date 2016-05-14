import plistlib

from .abstract_reader import AbstractReader


class PlistReader(AbstractReader):

    @classmethod
    def parse(cls, source):
        try:
            return cls(plistlib.readPlistFromString(source))
        except TypeError as e:
            return cls({})

    def __init__(self, node):
        self.node = node

    def attribute(self, name):
        return self.node[name]

    def element(self, name):
        return self.node[name]

    def elements(self, *args):
        return self.node[name]
