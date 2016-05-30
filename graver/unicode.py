from reader import attribute
from reader.proxy_reader import ProxyReader


@attribute('hex')
class Unicode(ProxyReader):

    @property
    def hex(self):
        return self.attribute('hex')
