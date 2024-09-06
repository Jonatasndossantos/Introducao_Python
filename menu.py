from operacao import Operacao

#controller

class Menu:
    def __init__(self):
        self.opcao = -1
        self.opera = Operacao()
        self.num1 = 0
        self.num2 = 0

    def mostrarMenu(self):
        print('\n-------MENU------\n\n'        +
              'Escolha uma das opções abaixo: '+
              '\n0. sair'                     +
              '\n1. somar'                     +
              '\n2. Subtrair'                  +
              '\n3. Dividir'                   +
              '\n4. Multiplicar'               +
              '\n5. Potencia'                  +
              '\n6. Raiz'                      +
              '\n7. Tabuada'                   +
              '\n8. Numeros de 1 a 10'         +
              '\n9. Numeros Pares de 1 a 20'   +
              '\n'
              '')

    def coletar(self):
        self.num1 = int(input('Informe o primeiro número: '))
        self.num2 = int(input('Informe o segundo número: '))

    def operacao(self):
        while self.opcao != 0:
            self.mostrarMenu()
            self.opcao = int(input('Escolha uma das opções a cima: '))

            if self.opcao == 0:
                print(f'Obrigado!')
            if self.opcao == 1:
                self.coletar()  # chamando o input
                print(f'A soma dos numeros é: {self.opera.somar(self.num1, self.num2)}')
            elif self.opcao == 2:
                self.coletar()
                print(f'A subtração dos numeros é: {self.opera.subtrair(self.num1, self.num2)}')
            elif self.opcao == 3:
                self.coletar()
                print(f'A divisão dos numeros é: {self.opera.dividir(self.num1, self.num2)}')
            elif self.opcao == 4:
                self.coletar()
                print(f'A multiplicação dos numeros é: {self.opera.multiplicar(self.num1, self.num2)}')
            elif self.opcao == 5:
                self.coletar()
                print(f'O resultado da potencia é: {self.opera.potencia(self.num1, self.num2)}')
            elif self.opcao == 6:
                self.coletar()
                print(f'A raiz de {self.num1} é: {self.opera.raiz(self.num1)}')
                print(f'A raiz de {self.num2} é: {self.opera.raiz(self.num2)}')
            elif self.opcao == 7:
                self.coletar()
                print(f'A tabuada do {self.num1} é {self.opera.tabuada(self.num1)}')
                print(f'A tabuada do {self.num2} é {self.opera.tabuada(self.num2)}')
            elif self.opcao == 8:
                self.coletar()
                print(f'Os numeros de 1 a 10 são: {self.opera.numAte10()}')
            elif self.opcao == 9:
                self.coletar()
                print(f'Os numeros pares de 1 a 20 são: {self.opera.numParAte20()}')
