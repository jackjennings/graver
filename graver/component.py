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
        return float(self.attribute('xOffset'))

    @property
    def y_offset(self):
        return float(self.attribute('yOffset'))

    @property
    def x_scale(self):
        return float(self.attribute('xScale'))

    @property
    def y_scale(self):
        return float(self.attribute('yScale'))

    @property
    def xy_scale(self):
        return float(self.attribute('xyScale'))

    @property
    def yx_scale(self):
        return float(self.attribute('yxScale'))

    @property
    def identifier(self):
        return self.attribute('identifier')
