import os

from graver.glif import GLIF
from graver.reader.xml_reader import XMLReader


__version__ = "0.0.1"


def open(filepath):
    reader = XMLReader.parse(os.path.abspath(filepath))
    version = reader.attribute('format')
    return GLIF(version=version, reader=reader)
