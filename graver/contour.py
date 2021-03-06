from reader import attribute, collection
from reader.proxy_reader import ProxyReader

from .collection import Collection
from .point import Point


@attribute('identifier')
@collection('points')
class Contour(ProxyReader):

    @property
    def points(self):
        return Collection(Point, self.elements('point'))

    @property
    def identifier(self):
        return self.attribute('identifier')
