from operacao import Operacao

#controller

class Menu:
    def __init__(self):
        self.opcao = -1
        self.opera = Operacao()
        self.num1 = 0
        self.num2 = 0

    def mostrarMenu(self):
        print('\n-------MENU------\n\n'                +
              'Escolha uma das opções abaixo: '        +
              '\n0. sair'                              +
              '\n1. somar'                             +
              '\n2. Subtrair'                          +
              '\n3. Dividir'                           +
              '\n4. Multiplicar'                       +
              '\n5. Potencia'                          +
              '\n6. Raiz'                              +
              '\n7. Tabuada'                           +
        #Exercicios
              '\n8. Numeros de 1 a 10'                 +#1
              '\n9. Numeros Pares de 1 a 20'           +#2
              '\n10. Soma de 1 a 100'                  +#3
              '\n11. Numeros multiplos de 5 ate 50'    +#4
              '\n12. Numero par ou impar'              +#5
              '\n13. Numero Positivo, Negativo ou Zero'+#6
              '\n14. Tabuada'                          +#7
              '\n15. Contagem'                         +#8
              '\n16. Soma dos numeros'                 +#9
              '\n17. Numeros primos ate 20'            +#10
              '\n19. Fatorial'                         +#12
              '\n20. Fibonacci'                        +#13
              '\n21. É Fibonacci'                      +#14
              '\n22. Soma dos digitos'                 +#15
              '\n23. Numeros par e impar'              +#16
              '\n24. Numeros primos'                   +#17
              '\n25. Sequencia de collatz'             +#18
              '\n26. Soma de pares e impares'          +#19
              '\n27. Numero perfeito'                  +#20
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
#Exercicios
            elif self.opcao == 8: #1
                print(f'Os numeros de 1 a 10 são: {self.opera.numAte10()}')
            elif self.opcao == 9: #2
                print(f'Os numeros pares de 1 a 20 são: {self.opera.numParAte20()}')
            elif self.opcao == 10: #3
                print(f'A soma dos numeros de 1 a 100 é: {self.opera.somaAte100()}')
            elif self.opcao == 11: #4
                print(f'Os numeros multiplos de 5 de 1 a 50 são: {self.opera.multiplos5()}')
            elif self.opcao == 12: #5
                self.coletar()
                print(f'O numero {self.num1} é: {self.opera.parOuImpar(self.num1)}')
                print(f'O numero {self.num2} é: {self.opera.parOuImpar(self.num2)}')
            elif self.opcao == 13: #6
                self.coletar()
                print(f'O numero {self.num1} é: {self.opera.posiNegaOuZero(self.num1)}')
                print(f'O numero {self.num2} é: {self.opera.posiNegaOuZero(self.num2)}')
            elif self.opcao == 14: #7
                self.coletar()
                print(f'A tabuada do {self.num1} é: {self.opera.tabuada(self.num1)}')
                print(f'A tabuada do {self.num2} é: {self.opera.tabuada(self.num2)}')
            elif self.opcao == 15: #8
                self.coletar()
                print(f'Os numeros de 1 a {self.num1} são: {self.opera.numAteNum(self.num1)}')
                print(f'Os numeros de 1 a {self.num2} são: {self.opera.numAteNum(self.num2)}')
            elif self.opcao == 16: #9
                self.coletar()
                print(f'A soma dos numeros de 1 ate {self.num1} são: {self.opera.somaAteNum(self.num1)}')
                print(f'A soma dos numeros de 1 ate {self.num2} são: {self.opera.somaAteNum(self.num2)}')
            elif self.opcao == 17: #10
                print(f'Os numeros primos de 1 a 20 são: {self.opera.primos(20)}')
            elif self.opcao == 19: #12
                num1 = int(input('Informe o numero: '))
                print(f'O fatorial de {num1} é: {self.opera.fatorial(num1)}')
            elif self.opcao == 20:  #13
                print(f'A sequencia de fibonacci ate o decimo termo é: {self.opera.fibonacci()}')
            elif self.opcao == 21: #14
                numero = int(input("Digite um número: "))
                if self.opera.seFibonacci(numero):
                    print("O número pertence à sequência de Fibonacci!")
                else:
                    print("O número não pertence à sequência de Fibonacci.")
            elif self.opcao == 22: #15
                numero = int(input("Digite um número: "))
                print(f'A soma dos digitos de {numero} é: {self.opera.somaDigitos(numero)}')
            elif self.opcao == 23: #16
                numero = int(input("Digite um número: "))
                print(f'os numeros pares e impares ate {numero} é: {self.opera.parEImpares(numero)}')
            elif self.opcao == 24: #17
                numero = int(input("Digite um número: "))
                print(f'os numeros primos ate {numero} é: {self.opera.impPrimo(numero)}')
            elif self.opcao == 25: #18
                numero = int(input("Digite um número: "))
                print(f'A sequencia de collatz de {numero} é: {self.opera.collatz(numero)}')
            elif self.opcao == 26: #19
                numero = int(input("Digite um número: "))
                print(f'A soma dos numeros Pares e Impares ate: {numero} são: {self.opera.somaParImpar(numero)}')
            elif self.opcao == 27: #20
                numero = int(input("Digite um número: "))
                if self.opera.perfeito(numero):
                    print(f"O número {numero} pertence aos numeros perfeitos!{self.opera.perfeito(numero)}")
                else:
                    print(f"O número {numero} nao pertence aos numeros perfeitos.{self.opera.perfeito(numero)}")



