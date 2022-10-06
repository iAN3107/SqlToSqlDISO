import pyodbc
from services.sqlDestino import *
from datetime import datetime
import logging


#CONFIGURAÇÃO GERADOR DE ARQUIVO DE LOG
now = datetime.now()
dt_string = now.strftime('%d-%m-%Y_%H:%M:%S')
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p', filename='logs/' + dt_string, encoding='utf-8', level=logging.DEBUG)

################################################################
#SQL AOND OS DADOS SÃO IMPORTADOS
sqlOrigem = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                           'Server=192.168.11.100,1433;'
                           'Database=edith;'
                           'Trusted_Connection=No; UID=sa;PWD=admin1234')

origem = sqlOrigem.cursor()

################################################################
#PEGA OS DADOS DA TABELA CATEGORIA E ENVIA PARA O SQL DESTINO
def exportCategoria():

    try:
        origem.execute("SELECT * FROM Categoria")
        rows = origem.fetchall()

        for row in rows:
            insertCategoriaDestino(row.Chave, row.Fabricante, row.Categoria, row.Meta, row.Real, row.Perc, row.Falta)
            logging.debug('CATEGORIA: ' + row.Chave + ' - exportado com sucesso')


    except Exception as e:
        print(e)
        logging.error('CATEGORIA ERROR: ' + str(e))
        sqlDestino.rollback()

################################################################
#PEGA OS DADOS DA TABELA COBERTURA E ENVIA PARA O SQL DESTINO
def exportCobertura():

    try:
        origem.execute("SELECT * FROM Cobertura")
        rows = origem.fetchall()

        for row in rows:
            insertCoberturaDestino(row.Ativo, row.Meta, row.Cobertura, row.Gap, row.Perc, row.Premio, row.Chave, row.Fabricante)
            logging.debug('COBERTURA: ' + row.Chave + ' - exportado com sucesso')

    except Exception as e:
        print(e)
        sqlDestino.rollback()
        logging.error('COBERTURA ERROR: ' + str(e))

################################################################
#PEGA OS DADOS DA TABELA FATURAMENTO E ENVIA PARA O SQL DESTINO
def exportFaturamento():

    try:
        origem.execute("SELECT * FROM Faturamento")
        rows = origem.fetchall()

        for row in rows:
            insertFaturamentoDestino(row.Meta, row.Real, row.Fornecedor, row.Chave, row.Perc, row.CodMeta, row.HasCateg, row.Premio)
            logging.debug('FATURAMENTO: ' + row.Chave + ' - exportado com sucesso')

    except Exception as e:
        print(e)
        sqlDestino.rollback()
        logging.error('FATURAMENTO ERROR: ' + str(e))

################################################################
#PEGA OS DADOS DA TABELA IEV E ENVIA PARA O SQL DESTINO
def exportIev():

    try:
        origem.execute("SELECT * FROM IEV")
        rows = origem.fetchall()

        for row in rows:
            insertIevDestino(row.Visitas, row.Positivas, row.PercMes, row.PecDiaAnterior, row.Premio, row.Chave)
            logging.debug('IEV: ' + row.Chave + ' - exportado com sucesso')


    except Exception as e:
        print(e)
        sqlDestino.rollback()
        logging.error('IEV ERROR: ' + str(e))

################################################################
#PEGA OS DADOS DA TABELA RECOMENDADOR E ENVIA PARA O SQL DESTINO
def exportRecomendador():

    try:
        origem.execute("SELECT * FROM Recomendador")
        rows = origem.fetchall()


        for row in rows:
            insertRecomendadorDestino(row.Carteira, row.Solds, row.SkusRec, row.Aderencia, row.Perc, row.AderenciaVolume,
                             row.PercVolume, row.Premio, row.Chave)
            logging.debug('RECOMENDADOR: ' + row.Chave + ' - exportado com sucesso')

    except Exception as e:
        print(e)
        sqlDestino.rollback()
        logging.error('RECOMENDADOR ERROR: ' + str(e))

################################################################
#PEGA OS DADOS DA TABELA ROTEIROS E ENVIA PARA O SQL DESTINO
def exportRoteiro():

    try:
        origem.execute("SELECT * FROM Roteiros")
        rows = origem.fetchall()

        for row in rows:
            insertRoteiroDestino(row.Cod, row.Chave, row.Cliente)
            logging.debug('ROTEIRO: ' + row.Chave + ' - exportado com sucesso')
    except Exception as e:
        print(e)
        sqlDestino.rollback()
        logging.error('ROTEIRO ERROR: ' + str(e))

################################################################
#PEGA OS DADOS DA TABELA USUARIOS E ENVIA PARA O SQL DESTINO
def exportUsuarios():

    try:
        origem.execute("SELECT * FROM Usuarios")
        rows = origem.fetchall()

        for row in rows:
            insertUsuariosDestino(row.Cod,row.Nome,row.Area,row.Empresa,row.Chave,row.Senha,row.Supervisor,row.isKan)
            logging.debug('USUARIOS: ' + row.Chave + ' - exportado com sucesso')

    except Exception as e:
        print(e)
        sqlDestino.rollback()
        logging.error('USUARIOS ERROR: ' + str(e))