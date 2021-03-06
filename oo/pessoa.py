class Pessoa:
    olhos = 2
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
    petenha.olhos = 1
    #del petenha.olhos
    print(carlos.__dict__)
    print(lis.__dict__)
    print(petenha.__dict__)
    Pessoa.olhos = 3
    print(carlos.olhos, lis.olhos, petenha.olhos)
    print(id(Pessoa.olhos), id(carlos.olhos), id(lis.olhos), id(petenha.olhos))


