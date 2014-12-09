from versioned import version
from versioned import VersionedObject


class GLIF(VersionedObject):

    @version(1)
    @version(2)
    @property
    def name(self):
        return True # return str()

    @version(1)
    @version(2)
    @property
    def format(self):
        return True # return int()

    @version(1)
    @version(2)
    @property
    def advance(self):
        return True # return Advance

    @version(1)
    @version(2)
    @property
    def unicode(self):
        return True # return Unicode

    @version(1)
    @version(2)
    @property
    def outline(self):
        return True # return Outline

    @version(1)
    @version(2)
    @property
    def lib(self):
        return True # return Lib

    @version(2)
    @property
    def note(self):
        return True # return Note

    @version(2)
    @property
    def image(self):
        return True # return Image

    @version(2)
    @property
    def guidelines(self):
        return True # return Collection(Guideline)

    @version(2)
    @property
    def anchors(self):
        return True # return Collection(Anchor)
