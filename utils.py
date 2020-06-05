from models import Pessoas


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


if __name__ == '__main__':
    insere_pessoas()
    consulta_pessoas()

    # altera_pessoa()
    # consulta_pessoas()

    # exclue_pessoa()
    # consulta_pessoas()
