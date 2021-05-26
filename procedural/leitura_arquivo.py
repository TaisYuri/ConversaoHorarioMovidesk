import pandas as pd

SUPORTE = ['nomes', 'separados', 'em', 'listas' ]

class Leitura_arquivo:

    def __init__(self,arquivo, pega_data = None,frame_arquivo = None):
        self.frame_arquivo = frame_arquivo
        self.pega_data = pega_data
        self.arquivo = arquivo

    def nome_arquivo(self):
        print("Digite o nome do arquivo para leitura")
        arq = input(('Arquivo: '))
        self.arquivo = 'C:/Relatorios-horarios/'+arq+'.csv'
        return self.arquivo

    def leitura_arquivo(self):
        leitura = pd.read_csv(self.nome_arquivo(), sep=';', encoding='latin-1')
        self.frame_arquivo = pd.DataFrame(leitura, columns=['Usuário', 'Entrada', 'Saída']) #Pega apenas as colunas que necessito analisar
        self.frame_arquivo = self.frame_arquivo.fillna({'Saída':'01/01/2020  00:00'}) #Na coluna de Saida, há valores nulos, substituo por uma data
        self.pega_data = self.frame_arquivo['Entrada']

        return self.frame_arquivo
