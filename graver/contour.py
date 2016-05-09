from .collection import Collection
from .point import Point


class Contour(object):

    @property
    def points(self):
        return Collection(Point)
