import math

class Operacao:
    def __init__(self):  # self porque é desta classe
        self.num1 = 0
        self.num2 = 0

    def coletar(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def somar(self, num1, num2):
        self.coletar(num1, num2)  # usando a def coletar
        return self.num1 + self.num2

    def subtrair(self, num1, num2):
        self.coletar(num1, num2)
        return self.num1 - self.num2

    def multiplicar(self, num1, num2):
        self.coletar(num1, num2)
        return self.num1 * self.num2

    def dividir(self, num1, num2):
        self.coletar(num1, num2)
        if self.num2 <= 0:
            return "Impossivel dividir!"
        else:
            return self.num1 / self.num2

    def tabuada(self, num1):
        resultado = ""
        for i in range(0, 11, 1):
            resultado += f'\n{num1} * {i} = {num1 * i}'
        return resultado

    def potencia(self, base, expoente):
        return pow(base, expoente)

    def raiz(self, num):
        return math.sqrt(num)

    def numAte10(self):
        resul = ""
        for i in range(1, 10, 1):
            resul += f'\n{i}'
        return resul

    def numParAte20(self):
        resul = ""
        for i in range(1, 20, 1):
            if i % 2 == 0:
                resul += f'\n{i}'
        return resul
    def somaAte100(self):
        resul = ""
