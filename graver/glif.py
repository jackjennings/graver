from versioned import version
from versioned import VersionedObject

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


class GLIF(VersionedObject):

    @version(1)
    @version(2)
    @property
    def name(self):
        return Name()

    @version(1)
    @version(2)
    @property
    def format(self):
        return Format()

    @version(1)
    @version(2)
    @property
    def advance(self):
        return Advance()

    @version(1)
    @version(2)
    @property
    def unicode(self):
        return Unicode()

    @version(1)
    @version(2)
    @property
    def outline(self):
        return Outline()

    @version(1)
    @version(2)
    @property
    def lib(self):
        return Lib()

    @version(2)
    @property
    def note(self):
        return Note()

    @version(2)
    @property
    def image(self):
        return Image()

    @version(2)
    @property
    def guidelines(self):
        return Collection(Guideline)

    @version(2)
    @property
    def anchors(self):
        return Collection(Anchor)
