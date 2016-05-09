import os
from xml.etree import ElementTree

from graver.glif import GLIF


__version__ = "0.0.1"


def open(filepath):
    tree = ElementTree.parse(os.path.abspath(filepath))
    version = tree.getroot().get('format')
    return GLIF(version=version)
