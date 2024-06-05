class Funcoesdequery:
    def __init__(self):
        #construção da classe para criar as querys para o banco de dados
        nome = ""
        numero = ""
        email = ""

    def dadosTrabalhados():
        nome = input("Digite o nome dousuario: ")
        numero = input("Digite o numero do usuario: ")
        email = input("Dgite o email do usuario: ")
        retornoDados = {
            "nome": nome,
            "numero": numero,
            "email": email
        }
        return retornoDados


    def insert(consulta):
        nome = consulta["nome"]
        numero = consulta["numero"]
        email = consulta["email"]
        sql = (f"INSERT INTO tb_contatos (T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO) VALUES ('{nome}', '{numero}', '{email}')")
        return sql
    
    def excluir(consulta, tipodeconsulta):
        match int(tipodeconsulta):
            case 1:
                perfilDeBusca = consulta["nome"]
                sql = f"DELETE FROM tb_contatos WHERE T_NOMECONTATO='{perfilDeBusca}' "
            case 2:
                perfilDeBusca = consulta["numero"]
                sql = f"INSERT INTO tb_contatos (T_TELEFONECONTATO) VALUES ('{perfilDeBusca}')"
            case 3:
                perfilDeBusca = consulta["email"]
                sql = f"INSERT INTO tb_contatos (T_EMAILCONTATO,) VALUES ('{perfilDeBusca}')"
        return sql
