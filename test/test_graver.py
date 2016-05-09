import graver
from graver.glif import GLIF


class TestGraver(object):

    def test_opens_glif1_file(self):
        glif = graver.open('./test/fixtures/glif1.glif')
        assert type(glif) is GLIF
        assert glif.version is 1

    def test_opens_glif2_file(self):
        glif = graver.open('./test/fixtures/glif2.glif')
        assert type(glif) is GLIF
        assert glif.version is 2
