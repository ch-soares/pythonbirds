class Motor:
    def __init__(self, velocidade=None):
        self.velocidade = velocidade

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2

class Direcao:
    def girar_a_direita(self):
        pass

    def girar_a_esquerda(self):
        pass

class carro(Motor, Direcao):
    pass
