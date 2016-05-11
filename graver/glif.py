from versioned import version
from versioned import VersionedObject

from reader.proxy_reader import ProxyReader

from .collection import Collection
from .name import Name
from .format import Format
from .advance import Advance
from .unicode import Unicode
from .outline import Outline
from .lib import Lib
from .note import Note
from .image import Image
from .guideline import Guideline
from .anchor import Anchor


class GLIF(ProxyReader, VersionedObject):

    @version(1)
    @version(2)
    @property
    def name(self):
        return Name(self.attribute('name'))

    @version(1)
    @version(2)
    @property
    def format(self):
        return Format(self.attribute('format'))

    @version(1)
    @version(2)
    @property
    def advance(self):
        return Advance(reader=self.element('advance'))

    @version(1)
    @version(2)
    @property
    def unicode(self):
        return Unicode(reader=self.element('unicode'))

    @version(1)
    @version(2)
    @property
    def outline(self):
        return Outline(reader=self.element('outline'))

    @version(1)
    @version(2)
    @property
    def lib(self):
        return Lib(reader=self.element('lib'))

    @version(2)
    @property
    def note(self):
        return Note(reader=self.element('note'))

    @version(2)
    @property
    def image(self):
        return Image(reader=self.element('image'))

    @version(2)
    @property
    def guidelines(self):
        return Collection(Guideline, self.elements('guideline'))

    @version(2)
    @property
    def anchors(self):
        return Collection(Anchor, self.elements('anchor'))
