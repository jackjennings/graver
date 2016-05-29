from reader.proxy_reader import ProxyReader


class Advance(ProxyReader):

    @property
    def width(self):
        return self.attribute('width', int)

    @property
    def height(self):
        return self.attribute('height', int)
