from reader.proxy_reader import ProxyReader


class Unicode(ProxyReader):

    @property
    def hex(self):
        return self.attribute('hex')
