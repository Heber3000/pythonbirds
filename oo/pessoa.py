class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome = None, idade = 32):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        f'{cls} - olhos {cls.olhos}'


class Homem(Pessoa):
    pass


if __name__ == '__main__':
    heber = Homem(nome='Heber')
    levy = Homem(heber,nome='Levy')
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
    pessoa = Pessoa('Anônimo')
    print(isinstance(pessoa,Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(levy, Homem))
    print(isinstance(levy, Pessoa))



