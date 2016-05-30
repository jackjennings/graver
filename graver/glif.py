from versioned import version
from versioned import VersionedObject

from reader import attribute, element, collection
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


@attribute('name')
@attribute('format')
@element('advance')
@element('unicode')
@element('outline')
@element('lib')
@element('note')
@element('image')
@collection('guidelines')
@collection('anchors')
class GLIF(ProxyReader, VersionedObject):

    def __init__(self, *args, **kwargs):
        super(GLIF, self).__init__(*args, **kwargs)
        self.format = Format(self.version)


    @version(1)
    @version(2)
    @property
    def name(self):
        return Name(self.attribute('name'))

    @version(1)
    @version(2)
    @property
    def format(self):
        return self.attribute('format', Format)

    @version(1)
    @version(2)
    @property
    def advance(self):
        return Advance(self.element('advance'))

    @version(1)
    @version(2)
    @property
    def unicode(self):
        return Unicode(self.element('unicode'))

    @version(1)
    @version(2)
    @property
    def outline(self):
        return Outline(self.element('outline'))

    @version(1)
    @version(2)
    @property
    def lib(self):
        return Lib(self.attribute('lib'))

    @version(2)
    @property
    def note(self):
        return Note(self.element('note'))

    @version(2)
    @property
    def image(self):
        return Image(self.element('image'))

    @version(2)
    @property
    def guidelines(self):
        return Collection(Guideline, self.elements('guideline'))

    @version(2)
    @property
    def anchors(self):
        return Collection(Anchor, self.elements('anchor'))
