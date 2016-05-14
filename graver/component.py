from reader.proxy_reader import ProxyReader


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
