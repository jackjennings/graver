from reader import collection
from reader.proxy_reader import ProxyReader

from .collection import Collection
from .component import Component
from .contour import Contour


@collection('components')
@collection('contours')
class Outline(ProxyReader):

    @property
    def components(self):
        return Collection(Component, self.elements('component'))

    @property
    def contours(self):
        return Collection(Contour, self.elements('contour'))
