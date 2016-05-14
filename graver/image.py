from reader.proxy_reader import ProxyReader


class Image(ProxyReader):

    @property
    def file_name(self):
        return self.attribute('fileName')

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
    def color(self):
        return self.attribute('color')
