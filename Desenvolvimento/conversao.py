from _datetime import datetime
import pandas as pd

class Conversao:

    def __init__(self):
        self.info_convertido = 0
        self.vl_Final = []
        self.coluna_hora = []

    def converte_Data(self, ler_coluna):
        for linha in ler_coluna:
            self.info_convertido = datetime.strptime(linha, "%d/%m/%Y %H:%M")
            self.info_convertido = self.info_convertido.strftime('%d/%m/%Y')
            self.vl_Final.append(self.info_convertido)

    def converte_Hora(self, ler_coluna):
        self.vl_Final = []
        for linha in ler_coluna:
            self.info_convertido = datetime.strptime(linha, "%d/%m/%Y %H:%M")
            self.info_convertido = self.info_convertido.strftime('%H:%M')
            self.vl_Final.append(self.info_convertido)
        self.vl_Final = pd.DataFrame(self.vl_Final)