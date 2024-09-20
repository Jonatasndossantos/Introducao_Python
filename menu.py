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
        #Exercícios C#
              '\n28. Trocas de valor'                  +#1
              '\n29. Antecessor'                       +#2
              '\n30. Area retangulo'                   +#3
              '\n31. Sua idade em dias'                +#4
              '\n32. Percentual de eleitores'          +#5
              '\n33. Reajuste de salario'              +#6
              '\n34. Reajuste do custo'                +#7
              '\n35. Media de 3 notas'                 +#8
              '\n36. Preço das maças'                  +#9
              '\n37. Ordem crescente de 10 valores'    +#10
              '\n38. Salario com comisssao'            +#11
              '\n39. Verificar saldo'                  +#12
              '\n40. Tabuada'                          +#13
              '\n41. Numeros de 1 a num'               +#14
              '\n42. Numeros negativos'                +#15
              '\n43. Soma dos menores que 40'          +#16
              '\n44. A media aritmética de 15 a 100'   +#17
              '\n45. A media e o maior'                +#18
              '\n46. Turma de 20 alunos'               +#19
              '\n47. Prefeitura'                       +#20

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
                num1 = int(input('Informe o primeiro número: '))
                print(f'A tabuada do {num1} é {self.opera.tabuada(num1)}')

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
                num1 = int(input('Informe o primeiro número: '))
                print(f'O numero {num1} é: {self.opera.parOuImpar(num1)}')
            elif self.opcao == 13: #6
                num1 = int(input('Informe o primeiro número: '))
                print(f'O numero {num1} é: {self.opera.posiNegaOuZero(num1)}')
            elif self.opcao == 14: #7
                num1 = int(input('Informe o primeiro número: '))
                print(f'A tabuada do {num1} é: {self.opera.tabuada(num1)}')
            elif self.opcao == 15: #8
                num1 = int(input('Informe o primeiro número: '))
                print(f'Os numeros de 1 a {num1} são: {self.opera.numAteNum(num1)}')
            elif self.opcao == 16: #9
                num1 = int(input('Informe o primeiro número: '))
                print(f'A soma dos numeros de 1 ate {num1} são: {self.opera.somaAteNum(num1)}')
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

#Exercícios C#
            elif self.opcao == 28: #1
                print(f'A = 10 B = 20 vira {self.opera.trocaV()}')
            elif self.opcao == 29: #2
                n = int(input("Informe um Valor: "))
                print(f'O antecessor de {n} é: {self.opera.antecessor(n)}')
            elif self.opcao == 30: #3
                base = int(input("Informe a Base: "))
                altura = int(input("Informe a Altura: "))
                print(f'A Area do triangulo é: {self.opera.areaRetangulo(base,altura)}')
            elif self.opcao == 31: #4
                ano = int(input("Informe os anos: "))
                mes = int(input("Informe os meses: "))
                dia = int(input("Informe os dias: "))
                print(f'Sua idade expressa apenas em dias é: {self.opera.anosEmDias(ano,mes,dia)}')
            elif self.opcao == 32: #5
                total = int(input("Informe o Total de Eleitores: "))
                brancos = int(input("Informe o Total de votos Brancos: "))
                nulos = int(input("Informe o Total de votos Nulos: "))
                validos = int(input("Informe o Total de votos Validos: "))
                print(f'O percentual dos Eleitores é: {self.opera.percentualEleitores(total,brancos,nulos,validos)}')
            elif self.opcao == 33: #6
                salario = int(input("Informe o salario: "))
                percentual = int(input("Informe o Percentual: "))
                print(f'O valor do novo salario é: {self.opera.reajusteSalario(salario,percentual)}')
            elif self.opcao == 34: #7
                custo = int(input("Informe o custo: "))
                print(f'O custo final para o consumidor é: {self.opera.custoFinal(custo)}')
            elif self.opcao == 35: #8
                nota1 = int(input("Informe a primeira nota: "))
                nota2 = int(input("Informe a segunda nota: "))
                nota3 = int(input("Informe a terceira nota: "))
                print(f'A media das notas é: {self.opera.mediaNota(nota1, nota2, nota3)}')
            elif self.opcao == 36: #9
                maca = int(input("Informe a quantidade de maças: "))
                print(f'O valor total é: R${self.opera.macas(maca)}')
            elif self.opcao == 37: #10
                vetor = []
                for i in range(0,10,1):
                    vetor.append(input(f'Informe o {i}º valor: '))
                print(f'A ordem crescente dos valores é: {self.opera.ordem(vetor)}')
            elif self.opcao == 38: #11
                salario = int(input("Informe o salario: "))
                vendas = int(input("Informe o valor das vendas: "))
                print(f'O Salario total é: {self.opera.comissao(salario, vendas)}')
            elif self.opcao == 39: #12
                numero = int(input("Informe o numero da conta: "))
                saldo   = int(input("Informe o seu saldo: "))
                debito  = int(input("Informe o seu debido: "))
                credito = int(input("Informe o seu credito: "))
                print(f'O saldo atual é: {self.opera.saldo(saldo, debito, credito)}')
            elif self.opcao == 40: #13
                num = -1
                while not num > 1 and num < 10:
                    num = int(input("Informe um numero: "))
                    if num < 1 or num > 10:
                        print("numero invalido, escreva de 1 a 10")
                    else:
                        print(f'A tabuada do {num} é {self.opera.tabuada(num)}')
            elif self.opcao == 41: #14
                num1 = int(input("Informe um numero: "))
                print(f'Os numeros de 1 a {num1} são: {self.opera.numAteNum(num1)}')
            elif self.opcao == 42: #15
                vetor = []
                for i in range(0,10,1):
                    vetor.append(int(input(f'Informe o {i}º valor: ')))
                print(f'A quantidade de numeros negativos são: {self.opera.numNegativo(vetor)}')
            elif self.opcao == 43: #16
                vetor = []
                for i in range(0,10,1):
                    vetor.append(int(input(f'Informe o {i}º valor: ')))
                print(f'O valor da soma dos numors inferiores a 40 são: {self.opera.somaMenor40(vetor)}')
            elif self.opcao == 44: #17
                print(f'A media aritmética de 15 a 100 é: {self.opera.mediaAritmetica(15,100)} ')
            elif self.opcao == 45: #18
                q = int(input("Informe a quantidade: "))
                vetor = []
                for i in range(1,(q+1),1):
                    vetor.append(int(input(f'Informe o {i}º valor: ')))
                print(f'A media é: {self.opera.media(vetor)} \n '
                      f'O maior é: {self.opera.maior(vetor)}')
            elif self.opcao == 46: #19
                vetor = []
                for i in range(1, 21, 1):
                    vetor.append(int(input(f'Informe o {i}º valor: ')))
                print(f'A media da turma é: {self.opera.media(vetor)}\n'
                      f'A quantidade de alunos acima da media é: {self.opera.acimaDaMedia(vetor)}\n')
            elif self.opcao == 47: #20
                sal = []
                fil = []
                i = 0
                q = 0
                while True:
                    sal.append(int(input("Informe o salario: ") ))
                    fil.append(int(input("Informe a quantidade de filhos: ")))
                    q = sal[i]
                    i += 1
                    if q < 0:
                        break
                print(f'A media do salario é: {self.opera.media(sal)}\n'
                      f'A media do numero de filhos é: {self.opera.media(fil)}\n'
                      f'O maior salario é: {self.opera.maior(sal)}\n'
                      f'O percentual de pessoas com salario menor que 150 é: {self.opera.percentual150(sal)}%\n'
                      )




