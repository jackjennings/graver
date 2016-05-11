from xml.etree import ElementTree

from .abstract_reader import AbstractReader


class XMLReader(AbstractReader):

    @classmethod
    def parse(cls, source):
        tree = ElementTree.parse(source)
        return cls(tree.getroot())

    def __init__(self, element):
        self.node = element

    def attribute(self, name):
        return self.node.get(name)

    def element(self, name):
        return self.__class__(self.node.find(name))

    def elements(self, name):
        return [self.__class__(e) for e in self.node.findall(name)]
