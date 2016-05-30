from reader import attribute
from reader.proxy_reader import ProxyReader


@attribute('base')
@attribute('x_offset')
@attribute('y_offset')
@attribute('x_scale')
@attribute('y_scale')
@attribute('xy_scale')
@attribute('yx_scale')
@attribute('identifer')
class Component(ProxyReader):

    @property
    def base(self):
        return self.attribute('base')

    @property
    def x_offset(self):
        return self.attribute('xOffset', float)

    @property
    def y_offset(self):
        return self.attribute('yOffset', float)

    @property
    def x_scale(self):
        return self.attribute('xScale', float)

    @property
    def y_scale(self):
        return self.attribute('yScale', float)

    @property
    def xy_scale(self):
        return self.attribute('xyScale', float)

    @property
    def yx_scale(self):
        return self.attribute('yxScale', float)

    @property
    def identifier(self):
        return self.attribute('identifier')
