class Pessoa:
    def __init__(self, *filhos, nome=None, idade=None):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    petenha = Pessoa(nome='Petenha')
    lis = Pessoa(petenha, nome='Lis')
    carlos = Pessoa(lis, nome='Carlos')
    print(Pessoa.cumprimentar(lis))
    print(id(lis))
    print(lis.cumprimentar())
    print(lis.nome)
    print(lis.idade)
    for filho in lis.filhos:
        print(filho.nome)
    carlos.sobrenome = 'Soares'
    print(carlos.sobrenome)
    del lis.filhos
    print(carlos.__dict__)
    print(lis.__dict__)
    print(petenha.__dict__)


