class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome = None, idade = 32):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)



    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    heber = Pessoa(nome='Heber')
    levy = Pessoa(heber,nome='Levy')
    print(Pessoa.cumprimentar(levy))
    print(id(levy))
    print(levy.cumprimentar())
    print(levy.nome)
    for filho in levy.filhos:
        print(filho.nome)

    heber.sobrenome = 'Almeida'
    del heber.filhos
    levy.olhos = 1
    print(heber.__dict__)
    print(levy.__dict__)
    print(Pessoa.olhos)
    Pessoa.olhos = 3
    del levy.olhos
    print(heber.olhos)
    print(levy.olhos)
    print(id(Pessoa.olhos), id(heber.olhos), id(levy.olhos))



