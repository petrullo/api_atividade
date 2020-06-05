from models import Pessoas, Usuarios


# Insere dados na Tabela Pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='Petrullo', idade=43)
    pessoa.save()


# Consulta dados na Tabela Pessoa
def consulta_pessoas():
    pessoas = Pessoas.query.all()
    # pessoa = Pessoas.query.filter_by(nome='Alexandre').first()
    print(pessoas)


# Altera dados na Tabela Pessoa
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Petrullo').first()
    pessoa.idade = 21
    pessoa.nome = 'Melissa'
    pessoa.save()


# Exclui dados na Tabela Pessoa
def exclue_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Petrullo').first()
    pessoa.delete()


# Insere usuario na Tabela de usuarios
def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()


# Consulta usuarios na Tabela de usuarios
def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)


# Exclui todos usuarios na Tabela de usuarios
def exclue_usuarios():
    usuarios = Usuarios.query.all()
    for i in usuarios:
        i.delete()


if __name__ == '__main__':
    # insere_usuario('alexandre', '123456')
    # insere_usuario('petrullo', '654321')
    # exclue_usuarios()
    consulta_todos_usuarios()

    # insere_pessoas()
    # consulta_pessoas()
    # altera_pessoa()
    # consulta_pessoas()

    # exclue_pessoa()
    # consulta_pessoas()
