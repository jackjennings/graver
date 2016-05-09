import pytest

from graver.contour import Contour
from graver.collection import Collection


class TestContour(object):

    def test_contour_has_points(self):
        contour = Contour()
        assert type(contour.points) is Collection
