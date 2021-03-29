from pessoa import Pessoa

class Medico(Pessoa):

    def __init__(self, nome):
        super().__init__(nome)

    def definir_id(self, identificacao):
        if len(identificacao) > 3:
            print("ID inválido. Tente novamente")
        else:
            self.identificacao = identificacao

    def nome_medico(self):
        return Pessoa.get_nomepessoa(self)
    
