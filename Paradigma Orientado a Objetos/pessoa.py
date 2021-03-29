import abc

class Pessoa(abc.ABC):

    def __init__(self, __nome):
        self.__nome = __nome

    def get_nomepessoa(self):
        return self.__nome

    @abc.abstractmethod
    def definir_id(self, identificacao):
        pass

