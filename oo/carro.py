


"""Você deve  criar uma classe carro que vai possuir dois atributos compostos por outras classes duas classes
1) Motor
2) Direção

O motor terá responsabilidade de controla a velocidade.
Ele oferece os seguintes atributos:
1) Atributo de dado velocidade
2) Método Acelerar, que deverá incrementar a velocidade de uma unidade.
3) Método frear que deverá decrementar a velocidade em duas unidades

A Direção terá responsabilidade de controlar a direção. Ela oferece os seguintes atributos:
1) Valor de direção com valores possíveis: Norte, Sul, Leste, Oeste.
2) Método girar a direita
3) Método girar a esquerda

      N
    O   L
      S

    Exemplo:
    >>> # Testando Motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0
    >>> # Testando Direção
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Norte'
    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'Leste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Oeste'
"""
class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade +=1

    def frear(self):
        self.velocidade -=2
        self.velocidade = max(0, self.velocidade)



NORTE='Norte'
SUL='Sul'
LESTE='Leste'
OESTE='Oeste'


class Direcao:
    rotacao_a_direita_dct = {NORTE:LESTE,LESTE:SUL,SUL:OESTE,OESTE:NORTE
                             }

    rotacao_a_esquerda_dct = {NORTE: OESTE, OESTE: SUL, SUL: LESTE, LESTE: NORTE
                             }



    def __init__(self):
        self.valor = NORTE

    def girar_a_direita(self):
         self.valor = self.rotacao_a_direita_dct[self.valor]

    def girar_a_esquerda(self):
        self.valor = self.rotacao_a_esquerda_dct[self.valor]







# Resolução Heber
"""
class Motor:
    def __init__(self,velocidade):
        self.velocidade = velocidade

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        if self.velocidade > 2:
            self.velocidade -= 2
        elif self.velocidade == 1:
            self.velocidade -=1


# Testando Motor
if __name__ == '__main__':
    motor = Motor(0)
    motor.acelerar()
    print(motor.velocidade)
    motor.acelerar()
    print(motor.velocidade)
    motor.acelerar()
    print(motor.velocidade)
    motor.frear()
    print(motor.velocidade)
    motor.frear()
    print(motor.velocidade)




class Direcao:
    def __init__(self,valor):
        self.valor = valor


    def girar_direita(self):
        if self.valor == 'Norte':
            self.valor = 'Oeste'
        elif self.valor == 'Oeste':
            self.valor = 'Sul'
        elif self.valor == 'Sul':
            self.valor = 'Leste'
        else:
            self.valor = 'Norte'


    def girar_esquerda(self):
        if self.valor == 'Norte':
            self.valor = 'Leste'
        elif self.valor == 'Leste':
            self.valor = 'Sul'
        elif self.valor == 'Sul':
            self.valor = 'Oeste'
        else:
            self.valor = 'Norte'

print()

if __name__ == '__main__':
    direcao = Direcao('Norte')
    direcao.girar_direita()
    print(direcao.valor)
    direcao.girar_direita()
    print(direcao.valor)
    direcao.girar_direita()
    print(direcao.valor)
    direcao.girar_direita()
    print(direcao.valor)



    print('')




    direcao.girar_esquerda()
    print(direcao.valor)
    direcao.girar_esquerda()
    print(direcao.valor)
    direcao.girar_esquerda()
    print(direcao.valor)
    direcao.girar_esquerda()
    print(direcao.valor)
"""






