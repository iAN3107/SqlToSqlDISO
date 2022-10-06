import pyodbc
from services.sqlOrigem import *
from services.sqlDestino import deletaDadosTabelaDestino

if __name__ == '__main__':

    ################################################################
    #DELETA OS DADOS DO BANCO DESTINO PARA NOVA INSERÇÃO
    deletaDadosTabelaDestino()

    ################################################################
    #ENVIA OS DADOS PARA INSERÇÃO
    exportCategoria()
    exportCobertura()
    exportFaturamento()
    exportIev()
    exportRecomendador()
    exportRoteiro()
    exportUsuarios()

    print('API CONCLUIDA, LOG GERADO EM LOGS')
