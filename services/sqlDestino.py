import pyodbc

sqlDestino = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                            'Server=192.168.11.100,14333;'
                            'Database=edith;'
                            'Trusted_Connection=No; UID=sa;PWD=Neutralizado12')


################################################################
# EXCLUI OS DADOS PARA ATUAIS PARA INSERÇÃO DOS NOVOS
def deletaDadosTabelaDestino():
    try:
        sqlDestino.execute("DELETE FROM Categoria")
        sqlDestino.execute("DELETE FROM Cobertura")
        sqlDestino.execute("DELETE FROM Faturamento")
        sqlDestino.execute("DELETE FROM IEV")
        sqlDestino.execute("DELETE FROM Recomendador")
        sqlDestino.execute("DELETE FROM Roteiros")
        sqlDestino.execute("DELETE FROM Usuarios")
        sqlDestino.commit()
    except Exception as e:
        print(e)
        sqlDestino.rollback()

################################################################
# INSERE DADOS NO BANCO DESTINO NA TABELA CATEGORIA
def insertCategoriaDestino(Chave, Fabricante, Categoria, Meta, Real, Perc, Falta):
    try:
        sqlDestino.execute("INSERT INTO Categoria VALUES (?,?,?,?,?,?,?)",
                    [Chave, Fabricante, Categoria, Meta, Real, Perc, Falta])

        sqlDestino.commit()

    except Exception as e:
        print(e)
        sqlDestino.rollback()

########################################################################
#INSERE DADOS NO BANCO DESTINO NA TABELA COBERTURA
def insertCoberturaDestino(Ativo, Meta, Cobertura, Gap, Perc, Premio, Chave, Fabricante):
    try:
        sqlDestino.execute("INSERT INTO Cobertura VALUES (?,?,?,?,?,?,?,?)",
                           [Ativo, Meta, Cobertura, Gap, Perc, Premio, Chave, Fabricante])

        sqlDestino.commit()
    except Exception as e:
        print(e)
        sqlDestino.rollback()

########################################################################
#INSERE DADOS NO BANCO DESTINO NA TABELA FATURAMENTO
def insertFaturamentoDestino(Meta,Real,Fornecedor,Chave,Perc,CodMeta,HasCateg,Premio):
    try:
        sqlDestino.execute("INSERT INTO Faturamento VALUES (?,?,?,?,?,?,?,?)",
                           [Meta,Real,Fornecedor,Chave,Perc,CodMeta,HasCateg,Premio])

        sqlDestino.commit()
    except Exception as e:
        print(e)
        sqlDestino.rollback()

########################################################################
#INSERE DADOS NO BANCO DESTINO NA TABELA IEV
def insertIevDestino(Visitas,Positivas,PercMes,PecDiaAnterior,Premio,Chave):
    try:
        sqlDestino.execute("INSERT INTO IEV VALUES (?,?,?,?,?,?)",
                           [Visitas,Positivas,PercMes,PecDiaAnterior,Premio,Chave])

        sqlDestino.commit()
    except Exception as e:
        print(e)
        sqlDestino.rollback()

########################################################################
#INSERE DADOS NO BANCO DESTINO NA TABELA RECOMENDADOR
def insertRecomendadorDestino(Carteira,Solds,SkusRec,Aderencia,Perc,AderenciaVolume,PercVolume,Premio,Chave):
    try:
        sqlDestino.execute("INSERT INTO Recomendador VALUES (?,?,?,?,?,?,?,?,?)",
                           [Carteira,Solds,SkusRec,Aderencia,Perc,AderenciaVolume,PercVolume,Premio,Chave])

        sqlDestino.commit()
    except Exception as e:
        print(e)
        sqlDestino.rollback()

########################################################################
#INSERE DADOS NO BANCO DESTINO NA TABELA ROTEIROS
def insertRoteiroDestino(Cod,Chave,Cliente):
    try:
        sqlDestino.execute("INSERT INTO Roteiros VALUES (?,?,?)",
                           [Cod,Chave,Cliente])

        sqlDestino.commit()
    except Exception as e:
        print(e)
        sqlDestino.rollback()

########################################################################
#INSERE DADOS NO BANCO DESTINO NA TABELA USUARIOS
def insertUsuariosDestino(Cod,Nome,Area,Empresa,Chave,Senha,Supervisor,isKan):
    try:
        sqlDestino.execute("INSERT INTO Usuarios VALUES (?,?,?,?,?,?,?,?)",
                           [Cod,Nome,Area,Empresa,Chave,Senha,Supervisor,isKan])

        sqlDestino.commit()
    except Exception as e:
        print(e)
        sqlDestino.rollback()