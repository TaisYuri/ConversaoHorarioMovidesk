import pandas as pd

class Leitura_arquivo:

    def __init__(self,arquivo = None, pega_data = None,frame_arquivo = None):
        self.frame_arquivo = frame_arquivo
        self.pega_data = pega_data
        self.arquivo = arquivo
        self.nomes_suporte = nomes_suporte = []

    def nome_arquivo(self):
        print("Digite o nome do arquivo para leitura")
        arq = input(('Arquivo: '))
        self.arquivo = 'C:/Relatorios-horarios/'+arq+'.csv'
        return self.arquivo

    def ler_arquivo(self):
        leitura = pd.read_csv(self.nome_arquivo(), sep=';', encoding='latin-1')
        self.frame_arquivo = pd.DataFrame(leitura, columns=['Usuário', 'Entrada', 'Saída']) #Pega apenas as colunas que necessito analisar
        self.frame_arquivo = self.frame_arquivo.fillna({'Saída':'01/01/2020  00:00'}) #Na coluna de Saida, há valores nulos, substituo por uma data
        self.pega_data = self.frame_arquivo['Entrada']

        return self.frame_arquivo

    def arquivo_txt_com_nomes_para_leitura(self):
        try:
            arquivo = open('C:/Relatorios-horarios/SUPORTE.txt', 'r', encoding="utf8")
            for nome in arquivo:
                self.nomes_suporte.append(nome.rstrip())
        except FileNotFoundError:
            print('ATENÇÃO! \nO arquivo SUPORTE.TXT deve estar na pasta com os nomes dos analistas para leitura.\n'
                  'Verifique e tente novamente!')

