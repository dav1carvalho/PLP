from medico import Medico
from medicamento import Medicamento
from datetime import datetime

class Prontuario:

    def __init__(self):
        self.__lista = []
    
    def insere_procedimento(self, medicamento, posologia, medico, data, hora):
        procedimentos = dict()
        nome_medico = medico.nome_medico()
        nome_medicamento = medicamento.nome_medicamento()
        date_object = datetime.strptime(data, '%d-%m-%Y').date()
        time_object = datetime.strptime(hora, '%H:%M').time()
        procedimentos.clear()
        procedimentos['medicamento'] = nome_medicamento
        procedimentos['posologia'] = posologia
        procedimentos['medico'] = nome_medico
        procedimentos['data'] = date_object
        procedimentos['hora'] = time_object

        self.__lista.append(procedimentos.copy())
        

    def exibe_prontuario(self):
         self.exibe = ''
         for i in self.__lista:
             self.exibe = self.exibe + '{} - {} - {} - {} - {}' .format(i['medicamento'], i['posologia'], i['medico'], i['data'], i['hora'])
             self.exibe = self.exibe + '\n'
             

         return print(self.exibe)

        
        
    
