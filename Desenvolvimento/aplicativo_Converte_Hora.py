import pandas as pd

from Desenvolvimento.conversao import Conversao
from Desenvolvimento.leitura_arquivo import Leitura_arquivo
from Desenvolvimento.recriar_apresentacao import Recriar_estrutura_apresentacao

if __name__ == '__main__':

    arquivo = Leitura_arquivo()
    arquivo.ler_arquivo()
    arquivo.arquivo_txt_com_nomes_para_leitura()

    dados = Conversao()
    dados.converte_Data(arquivo.pega_data)
    data_frame = pd.DataFrame(dados.vl_Final)

    '''Captura informação HORA da coluna Entrada'''
    dados.converte_Hora(arquivo.frame_arquivo['Entrada'])
    entrada = dados.vl_Final

    '''Captura informação HORA da coluna Saída'''
    dados.converte_Hora(arquivo.frame_arquivo['Saída'])
    saida = dados.vl_Final

    '''Junta Frame de entrada + saida para ficar apenas uma coluna de horario'''
    frame1 = pd.concat([arquivo.frame_arquivo['Usuário'], data_frame, entrada], axis=1)
    frame2 = pd.concat([arquivo.frame_arquivo['Usuário'], data_frame, saida], axis=1)
    frame_constituido = pd.concat([frame1, frame2])

    selecao = frame_constituido['Usuário'].isin(arquivo.nomes_suporte)  # Seleciona apenas o pessoal do suporte
    dados_suporte = frame_constituido[selecao]  # Cria um frame apenas com os dados selecionados acima
    dados_suporte.columns = ('Usuário', 'Data', 'horario')  # Renomeia as colunas do novo frame

    recriar_estrurura = Recriar_estrutura_apresentacao()
    recriar_estrurura.recriar(dados_suporte)
    recriar_estrurura.gerar_relatorio_completo()
