import pandas as pd
from _datetime import datetime
from leitura_arquivo import Leitura_arquivo

def converte_dado_hora(ler_coluna):
    horario = []

    for linha in ler_coluna:
        z = datetime.strptime(str(linha), "%d/%m/%Y %H:%M")
        entr = z.strftime('%H:%M')
        horario.append(entr)
    return horario

def converte_dado_dia(ler_data):
    data = []

    for linha in ler_data:
        z = datetime.strptime(str(linha), "%d/%m/%Y %H:%M")
        entr = z.strftime('%d/%m/%Y')
        data.append(entr)
    return data

def cria_frame_hora(frame):
    retorna_horario = converte_dado_hora(frame)
    hora = pd.DataFrame(retorna_horario)
    return hora

arquivo = Leitura_arquivo
arquivo.leitura_arquivo()

retorna_data = converte_dado_dia(pega_data) #Converte a coluna 'Entrada' em apenas data
data = pd.DataFrame(retorna_data) #Converte a lista em um dataframe

hor_entrada = cria_frame_hora(frame_arquivo['Entrada']) #Converte lista das horas de entrada em um frame
hor_saida = cria_frame_hora(frame_arquivo['Saída']) #Converte lista das horas de saida em um frame
frame1 = pd.concat([frame_arquivo['Usuário'],data, hor_entrada], axis=1) #Concatena entradas + data e usuario
frame2 = pd.concat([frame_arquivo['Usuário'],data, hor_saida], axis=1) #Concatena saida + data e usuario

frameFinal = pd.concat([frame1, frame2]) #Junta Frame de entrada + saida para ficar apenas uma coluna de horario

selecao = frameFinal['Usuário'].isin(suporte) #Seleciona apenas o pessoal do suporte
dados_suporte = frameFinal[selecao] #Cria um frame apenas com os dados selecionados acima
dados_suporte.columns = ('Usuário', 'Data','horario') #Renomeia as colunas do novo frame

dia = []
analista = []
xx = []
h1 = []
h2 = []
h3 = []
h4 = []
h5 = []
h6= []

for dt in dados_suporte['Data'].drop_duplicates():
    xxx = (dados_suporte['Data'] == dt)
    xxx2 = dados_suporte[xxx]
    xxx2 = pd.DataFrame(xxx2)
    xxx2 = xxx2['Usuário'].drop_duplicates()

    for usuario in xxx2:
        seleciona_analista = (dados_suporte['Usuário']==usuario) & (dados_suporte['Data'] == dt)
        pega_analista_e_data = dados_suporte[seleciona_analista]
        pega_analista_e_data = pd.DataFrame(pega_analista_e_data)
        pega_analista_e_data.sort_values(by='horario', inplace=True)


        for usuario,dat,hora in pega_analista_e_data.values:
            xx.append(hora)


        if len(pega_analista_e_data) == 6:
            h1.append(xx[0])
            h2.append(xx[1])
            h3.append(xx[2])
            h4.append(xx[3])
            h5.append(xx[4])
            h6.append(xx[5])
            dia.append(dt)
            JuncaoDados = pd.DataFrame({'Data': dia, 'Hora1': h1, 'Hora2': h2, 'Hora3': h3, 'Hora4': h4, 'Hora5': h5, 'Hora6': h6})
            analista.append(usuario)
            xx = []


        elif len(pega_analista_e_data) == 4:
            h1.append(xx[0])
            h2.append(xx[1])
            h3.append(xx[2])
            h4.append((xx[3]))
            h5.append('')
            h6.append('')
            dia.append(dt)
            JuncaoDados = pd.DataFrame({'Data': dia, 'Hora1': h1, 'Hora2': h2, 'Hora3': h3, 'Hora4': h4, 'Hora5': h5, 'Hora6': h6})
            analista.append(usuario)
            xx = []

        else:
            h1.append(xx[0])
            h2.append('-')
            h3.append('-')
            h4.append(xx[1])
            h5.append('')
            h6.append('')
            dia.append(dt)
            JuncaoDados = pd.DataFrame({'Data': dia, 'Hora1': h1, 'Hora2': h2, 'Hora3': h3, 'Hora4': h4, 'Hora5': h5, 'Hora6': h6})
            analista.append(usuario)
            xx = []

    JuncaoDados['Usuario'] = analista
    JuncaoDados = JuncaoDados.set_index('Usuario')


atual = str(datetime.strftime(datetime.now(),'%d%m%Y-%H%M'))
JuncaoDados.to_csv('C:/Relatorios-horarios/ ' + atual + '.csv', sep=';')

print('Processo finalizado! Arquivo salvo em: C:/Relatorios-horarios/')
input('Pressione ENTER para fechar!')
