from reader import attribute
from reader.proxy_reader import ProxyReader


@attribute('y')
@attribute('x')
@attribute('angle')
@attribute('name')
@attribute('color')
@attribute('identifier')
class Guideline(ProxyReader):

    @property
    def y(self):
        return self.attribute('y', int)

    @property
    def x(self):
        return self.attribute('x', int)

    @property
    def angle(self):
        return self.attribute('angle', int)

    @property
    def name(self):
        return self.attribute('name')

    @property
    def color(self):
        return self.attribute('color')

    @property
    def identifier(self):
        return self.attribute('identifier')
