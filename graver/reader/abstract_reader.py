from abc import abstractmethod, ABCMeta


class AbstractReader(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def attribute(self, name): pass

    @abstractmethod
    def element(self, name): pass

    @abstractmethod
    def elements(self, name): pass
