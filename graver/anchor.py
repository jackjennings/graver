from reader.proxy_reader import ProxyReader


class Anchor(ProxyReader):

    @property
    def y(self):
        return int(self.attribute('y'))

    @property
    def x(self):
        return int(self.attribute('x'))

    @property
    def name(self):
        return self.attribute('name')

    @property
    def color(self):
        return self.attribute('color')

    @property
    def identifier(self):
        return self.attribute('identifier')
