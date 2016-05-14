from reader.proxy_reader import ProxyReader


class Advance(ProxyReader):

    @property
    def width(self):
        return int(self.attribute('width'))

    @property
    def height(self):
        return int(self.attribute('height'))
