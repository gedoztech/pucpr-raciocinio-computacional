import math


class Circulo:

    def __init__(self, raio, x=1, y=1):
        self.x = x
        self.y = y
        self.raio = raio
        self.area = self.__calcula_area()
        self.diametro = self.__calcula_diametro()
        self.circunferencia = self.__calcula_circunferencia()

    def __calcula_area(self):
        return math.pi * (self.raio ** 2)

    def __calcula_diametro(self):
        return 2 * self.raio

    def __calcula_circunferencia(self):
        return 2 * math.pi * self.raio

    def muda_posicao(self, x, y):
        self.x = x
        self.y = y


circulo = Circulo(31, 4, 10)
print('Círculo 1 => ')
print('Área: ', circulo.area)
print('Diâmetro: ', circulo.diametro)
print('Circunferência: ', circulo.circunferencia)
print('Posição Central: ({0},{1})'.format(circulo.x, circulo.y))

circulo.muda_posicao(1, 12)
print('Nova Posição Central: ({0},{1})'.format(circulo.x, circulo.y))
