from unittest import TestCase
import pandas as pd
from pandas._testing import assert_frame_equal

from Desenvolvimento.aplicativo_Converte_Hora import Conversao, Leitura_arquivo


class testConversao(TestCase):

    def test_converte_data(self):
        dado = Conversao()
        dado.converte_Data(['31/12/2028 12:00', '31/12/2028 13:00'])
        self.assertEqual(['31/12/2028', '31/12/2028'],dado.vl_Final)

    def test_converte_hora(self):
        dado = Conversao()
        dado.converte_Hora(['31/12/2028 12:00', '31/12/2028 13:00'])
        df1 = pd.DataFrame(['12:00','13:00'])
        assert_frame_equal(df1,dado.vl_Final)


class testArquivo(TestCase):

    def test_nome_arquivo(self):
        leitura_arquivo = Leitura_arquivo()
        auxiliar = str(leitura_arquivo.nome_arquivo())
        self.assertEqual('C:/Relatorios-horarios/teste123.csv', auxiliar)

    def test_leitura_arquivo(self):
        df = pd.DataFrame({'Usuário': ['Caleb Souza', 'Rafael Simabuco'], 'Entrada': ['20/01/2021 18:03', '20/01/2021 16:52'],
                           'Saída': ['20/01/2021 22:01','20/01/2021 22:03']})

        x = Leitura_arquivo()
        x.ler_arquivo()
        assert_frame_equal(df, x.frame_arquivo)

    def test_coluna_data(self):
        df = pd.DataFrame(['20/01/2021', '20/01/2021'])

        arquivo = Leitura_arquivo()
        arquivo.ler_arquivo()
        dados = Conversao()
        dados.converte_Data(arquivo.pega_data)
        data_Frame = pd.DataFrame(dados.vl_Final)
        assert_frame_equal(df, data_Frame)
