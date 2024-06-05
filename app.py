import conexaoComBancoDados.bancoDados
import funcoesdequery
import conexaoComBancoDados
from tkinter import *
from funcoesdequery import query



#usuario = query.Funcoesdequery.dadosTrabalhados()
#conexaoBD = conexaoComBancoDados.bancoDados.conexaoBancoDados()
#dadosIsercao = query.Funcoesdequery.insert(consulta=usuario)
#dadosexclusao = query.Funcoesdequery.excluir(usuario, 1)
#commitDedados = conexaoComBancoDados.bancoDados.comandoquery(conexaoBD, dadosexclusao)

def telaprincipal():
    #Criando a tela apartir de uma fução.
    telaAplicacao = Tk()
    telaAplicacao.title("Agenda de contatos")
    telaAplicacao.geometry("400x400")
    telaAplicacao.configure(background="#778870")
    #Adicionando titulo à tela da alicação
    tituloTela = Label(telaAplicacao, text="Agenda de contatos", foreground="#dde")
    tituloTela.pack(padx=10, pady=10,)

    nomelabel = Label(telaAplicacao, text="nome", background="#dde", foreground="#009", anchor=W)
    nomelabel.place(x=10, y= 30, width=100, height=20)

    nomeEntry = Entry(telaAplicacao)
    nomeEntry.place(x=10, y= 60, width=100, height=20)

    numeroLabel = Label(telaAplicacao, text="Número", background="#dde", foreground="#009", anchor=W)
    numeroLabel.place(x=10, y= 90, width=100, height=20)
    
    numeroEntry = Entry(telaAplicacao)
    numeroEntry.place(x=10, y= 120, width=100, height=20)

    emailLabel = Label(telaAplicacao, text="Email", background="#dde", foreground="#009", anchor=W)
    emailLabel.place(x=10, y= 150, width=100, height=20)
    
    emailEntry = Entry(telaAplicacao)
    emailEntry.place(x=10, y= 180, width=100, height=20)



    botaoAdicionar = Button(telaAplicacao, text="Adicionar",command=telaadicionar)
    botaoAdicionar.place(x=10, y=210, width=100, height=20)

    botaoAdicionar = Button(telaAplicacao, text="Cancelar",command=telaadicionar)
    botaoAdicionar.place(x=120, y=210, width=100, height=20)

    telaAplicacao.mainloop()


def telaadicionar():
    tladicionar = Tk()
    tladicionar.title("tela De Adição")
    tladicionar.geometry("400x400")
    tladicionar.configure(background="#77ff")



telaprincipal()