import pandas as pd
from _datetime import datetime

class Recriar_estrutura_apresentacao:
    def __init__(self):
        self.dia = dia = []
        self.analista = analista =[]
        self.lista_com_valores = []
        self.h1 = h1 =[]
        self.h2 = h2 =[]
        self.h3 = h3 =[]
        self.h4 = h4 =[]
        self.h5 = h5 =[]
        self.h6 = h6 =[]
        self.juncao_de_dados = juncao_de_dados = []

    def recriar(self, dados_suporte):

        for dt in dados_suporte['Data'].drop_duplicates():
            compara_data = (dados_suporte['Data'] == dt)
            compara_usuario = dados_suporte[compara_data]
            compara_usuario = pd.DataFrame(compara_usuario)
            compara_usuario = compara_usuario['Usuário'].drop_duplicates()

            for usuario in compara_usuario:
                seleciona_analista = (dados_suporte['Usuário'] == usuario) & (dados_suporte['Data'] == dt)
                pega_analista_e_data = dados_suporte[seleciona_analista]
                pega_analista_e_data = pd.DataFrame(pega_analista_e_data)
                pega_analista_e_data.sort_values(by='horario', inplace=True)

                for usuario, dat, hora in pega_analista_e_data.values:
                    self.lista_com_valores.append(hora)

                if len(pega_analista_e_data) == 6:
                    self.h1.append(self.lista_com_valores[0])
                    self.h2.append(self.lista_com_valores[1])
                    self.h3.append(self.lista_com_valores[2])
                    self.h4.append(self.lista_com_valores[3])
                    self.h5.append(self.lista_com_valores[4])
                    self.h6.append(self.lista_com_valores[5])
                    self.dia.append(dt)
                    self.juncao_de_dados = pd.DataFrame(
                        {'Data': self.dia, 'Hora1': self.h1, 'Hora2': self.h2, 'Hora3': self.h3, 'Hora4': self.h4, 'Hora5': self.h5, 'Hora6': self.h6})
                    self.analista.append(usuario)
                    self.lista_com_valores.clear()


                elif len(pega_analista_e_data) == 4:
                    self.h1.append(self.lista_com_valores[0])
                    self.h2.append(self.lista_com_valores[1])
                    self.h3.append(self.lista_com_valores[2])
                    self.h4.append(self.lista_com_valores[3])
                    self.h5.append('')
                    self.h6.append('')
                    self.dia.append(dt)
                    self.juncao_de_dados = pd.DataFrame(
                        {'Data': self.dia, 'Hora1': self.h1, 'Hora2': self.h2, 'Hora3': self.h3, 'Hora4': self.h4, 'Hora5': self.h5, 'Hora6': self.h6})
                    self.analista.append(usuario)
                    self.lista_com_valores.clear()

                else:
                    self.h1.append(self.lista_com_valores[0])
                    self.h2.append('-')
                    self.h3.append('-')
                    self.h4.append(self.lista_com_valores[1])
                    self.h5.append('')
                    self.h6.append('')
                    self.dia.append(dt)
                    self.juncao_de_dados = pd.DataFrame(
                        {'Data': self.dia, 'Hora1': self.h1, 'Hora2': self.h2, 'Hora3': self.h3, 'Hora4': self.h4, 'Hora5': self.h5, 'Hora6': self.h6})
                    self.analista.append(usuario)
                    self.lista_com_valores.clear()

            self.juncao_de_dados['Usuario'] = self.analista
            self.juncao_de_dados = self.juncao_de_dados.set_index('Usuario')


    def gerar_relatorio_completo(self):
        try:
            data_hora_atual = str(datetime.strftime(datetime.now(), '%d%m%Y-%H%M'))
            self.juncao_de_dados.to_csv('C:/Relatorios-horarios/ ' + data_hora_atual + '.csv', sep=';')

            print('Processo finalizado! Arquivo salvo em: C:/Relatorios-horarios/')
            input('Pressione ENTER para fechar!')
        except AttributeError:
            pass
