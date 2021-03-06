from reader import attribute
from reader.proxy_reader import ProxyReader


@attribute('y')
@attribute('x')
@attribute('type')
@attribute('smooth')
@attribute('name')
@attribute('identifier')
class Point(ProxyReader):

    @property
    def y(self):
        return self.attribute('y', int)

    @property
    def x(self):
        return self.attribute('x', int)

    @property
    def type(self):
        return self.attribute('type')

    @property
    def smooth(self):
        return self.attribute('smooth')

    @property
    def name(self):
        return self.attribute('name')

    @property
    def identifier(self):
        return self.attribute('identifier')
