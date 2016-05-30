from reader import attribute
from reader.proxy_reader import ProxyReader


@attribute('file_name')
@attribute('x_offset')
@attribute('y_offset')
@attribute('x_scale')
@attribute('y_scale')
@attribute('xy_scale')
@attribute('yx_scale')
@attribute('color')
class Image(ProxyReader):

    @property
    def file_name(self):
        return self.attribute('fileName')

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
    def color(self):
        return self.attribute('color')
