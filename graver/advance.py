from reader import attribute
from reader.proxy_reader import ProxyReader


@attribute('width')
@attribute('height')
class Advance(ProxyReader):

    @property
    def width(self):
        return self.attribute('width', int)

    @property
    def height(self):
        return self.attribute('height', int)
