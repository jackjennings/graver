from represents import represents

from versioned import version
from versioned import VersionedObject

from reader import attribute, element, collection
from reader.proxy_reader import ProxyReader

from writer.xml_writer import XMLWriter

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
        self.format = self.version

    def write(self, file, writer=XMLWriter):
        writer(self).write(file)

    @version(1, 2)
    @represents(Name)
    def name(self):
        return self.attribute('name')

    @version(1, 2)
    @represents(Format)
    def format(self):
        return self.attribute('format')

    @version(1, 2)
    @represents(Advance)
    def advance(self):
        return self.element('advance')

    @version(1, 2)
    @represents(Unicode)
    def unicode(self):
        return self.element('unicode')

    @version(1, 2)
    @represents(Outline)
    def outline(self):
        return self.element('outline')

    @version(1, 2)
    @represents(Lib)
    def lib(self):
        return self.attribute('lib')

    @version(2)
    @represents(Note)
    def note(self):
        return self.element('note')

    @version(2)
    @represents(Image)
    def image(self):
        return self.element('image')

    @version(2)
    @represents(Collection, Guideline)
    def guidelines(self):
        return self.elements('guideline')

    @version(2)
    @represents(Collection, Anchor)
    def anchors(self):
        return self.elements('anchor')
