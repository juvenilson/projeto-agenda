import os
import sqlite3
from sqlite3 import Error

def conexaoBancoDAdos():
    caminhoBancodados = "C:/Users/juven/OneDrive/Documents/aulas-jornada-do-dev/agenda.db"
    conexao = None
    try:
        conexao = sqlite3.connect(caminhoBancodados)
    except Error as ex:
        print(ex)
    return conexao


def query(conexao, sql):
    try:
        cursor = conexao.cursor()
        cursor.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        conexao.close()


def consultar(conexao, sql):
    try:
        cursor = conexao.cursor()
        cursor.execute(sql)
        respostaDaaConsulta = cursor.fetchall()
        return respostaDaaConsulta
    except Error as ex:
        print(ex)
    finally:
        conexao.close()