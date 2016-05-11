from reader.proxy_reader import ProxyReader


class Image(ProxyReader):

    @property
    def file_name(self):
        return self.attribute('fileName')

    @property
    def x_scale(self):
        return float(self.attribute('xScale'))

    @property
    def y_scale(self):
        return float(self.attribute('yScale'))
