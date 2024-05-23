import conexaoComBancoDados.bancoDados
import funcoesdequery
import conexaoComBancoDados
import sqlite3
from funcoesdequery import query



usuario = query.Funcoesdequery.dadosTrabalhados()
dadosIsercao = query.Funcoesdequery.insert(consulta=usuario)
conexaoBD = conexaoComBancoDados.bancoDados.conexaoBancoDados()
commitDedados = conexaoComBancoDados.bancoDados.comandoquery(conexaoBD, dadosIsercao)
