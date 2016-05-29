from reader.proxy_reader import ProxyReader


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
