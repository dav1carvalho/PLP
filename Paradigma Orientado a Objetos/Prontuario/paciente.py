from pessoa import Pessoa

class Paciente(Pessoa):
    __ativos = 0

    def __init__(self, nome):
        Paciente.__ativos += 1
        super().__init__(nome)

    def __del__(self):
        Paciente.__ativos -= 1

    def definir_id(self, identificacao):
        if len(identificacao) > 5:
            print("ID inválido. Tente novamente")
        else:
            self.identificacao = identificacao

    @classmethod
    def pacientes_ativos(cls):
        return cls.__ativos
        
    def definir_prontuario(self, prontuario):
        self.prontuario = prontuario
