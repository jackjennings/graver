from .abstract_reader import AbstractReader


class NullReader(AbstractReader):

    def attribute(self, *args, **kwargs):
        return None

    def element(self, *args, **kwargs):
        return None

    def elements(self, *args, **kwargs):
        return []
