import os

from graver.glif import GLIF
from graver.reader.xml_reader import XMLReader


__version__ = "0.0.1"


def read(filepath):
    reader = XMLReader.parse(os.path.abspath(filepath))
    version = reader.attribute('format')
    return GLIF(version=version, reader=reader)


class open(object):

    def __init__(self, filepath):
        self.glif = read(filepath)

    def __enter__(self):
        return self.glif

    def __exit__(self, type, value, trace):
        pass
