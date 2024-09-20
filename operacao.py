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

#Exercicios
    def numAte10(self): #1
        resul = ""
        for i in range(1, 10, 1):
            resul += f'\n{i}'
        return resul

    def numParAte20(self): #2
        resul = ""
        for i in range(1, 20, 1):
            if i % 2 == 0:
                resul += f'\n{i}'
        return resul
    def somaAte100(self): #3
        resul = int()
        for i in range(1, 101, 1):
            resul += i
        return resul
    def multiplos5(self): #4
        resul = ""
        for i in range(1, 51, 1):
            if i % 5 == 0:
                resul += f'\n{i}'
        return resul
    def parOuImpar(self, num1): #5
        if num1 % 2 == 0:
            return f'Par'
        else:
            return f'Impar'
    def posiNegaOuZero(self, num1): #6
        if num1 > 0:
            return f'Positivo'
        elif num1 == 0:
            return f'Zero'
        elif num1 < 0:
            return f'Negativo'
    def numAteNum(self, num1): #8
        resul = ""
        for i in range(1, (num1+1), 1):
            resul += f'\n{i}'
        return resul

    def somaAteNum(self, num1):  #9
        resul = 0
        msg = ""
        for i in range(1, num1, 1):
            msg += f'\n {resul} + {i} = {resul + i}'
            resul += i
        return msg
    def primos(self, n): #10
        resul = "\n 2 \n 3 \n 5 \n 7"
        j = 0
        p = 2
        for i in range(1, n, 1):
            while i >= j:
                if p%2 != 0 and p%3 != 0 and p%5 != 0 and p%7 != 0:
                    resul += f'\n {p}'
                    j += 1
                p += 1
        return resul

    def sePrimo(self,number):
        if number < 2:
            return "False"
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
               return "False"
        return "True"

    def fatorial(self,num1): #12
        resul = 1
        for i in range(1, num1, 1):
            resul *= i
        return resul
    def fibonacci(self): #13
        resul = 1
        ult = 1
        penult = 1

        for i in range(2, 10, 1):
            resul = ult + penult
            penult = ult
            ult = resul
        return resul

    def seFibonacci(self, n): #14
        a, b = 0, 1
        while b < n:
            a, b = b, a + b
        return b == n

    def somaDigitos(self,n): #15
        s = 0
        while n:
            s += n % 10  # Soma `s` ao ultimo numeral de `n`
            n //= 10  # Remove o ultimo numero de `n`
        return s
    def parEImpares(self,n): #16
        resul = ""
        for i in range(1, n, 1):
            resul += f'\n{i} {self.parOuImpar(i)}'
        return resul

    def impPrimo(self,n): #17
        resul = "\n 2 \n 3 \n 5 \n 7"
        j = 0
        p = 2
        for i in range(1, n, 1):
            while i >= j:
                if p % 2 != 0 and p % 3 != 0 and p % 5 != 0 and p % 7 != 0:
                    resul += f'\n {p}'
                    j += 1
                if n == p:
                    return resul
                p += 1
    def collatz(self,x):
        resul = ""
        while x > 1:
            if x % 2 == 0:
                x /= 2
                resul += f'\n {x}'
            else:
                x = 3 * x + 1
                resul += f'\n {x}'
        return resul

    def somaParImpar(self, n):
        resul = ""
        par = 0
        impar = 0
        for i in range(1, n, 1):
            if i%2==0:
                par += i
            else:
                impar += i
        resul = f'\n {par} pares \n {impar} impares'
        return resul

    def perfeito(self,n):
        soma = n
        for i in range(1, (n-1), 1):
            if n % i == 0:
                soma -= i
        return soma == 0



#Exercícios C#
    def trocaV(self): #1
        A = 10
        B = 20
        (A,B)=(B,A)
        return (A,B)

    def antecessor(self,n): #2
        return (n-1)

    def areaRetangulo(self,base,altura): #3
        return (base * altura)

    def anosEmDias(self,ano,mes,dia): #4
        return (dia + (mes*30)+(ano*365))

    def percentualEleitores(self,total,brancos,nulos,validos): #5
        return (f'\n Brancos: {brancos/total*100}%' +
               f'\n Nulos: {nulos / total * 100}%' +
               f'\n Validos: {validos / total * 100}%'
                )

    def reajusteSalario(self,salario,percentual): #6
        return (salario+(salario*(percentual/100)))

    def custoFinal(self,custo): #7
        return (custo + (28 / 100) + (45 / 100) + custo)

    def mediaNota(self,nota1,nota2,nota3): #8
        return ((nota1+nota2+nota3)/3)

    def macas(self,maca): #9
        if maca < 12:
            return maca
        else:
            return (maca*(13/10))

    def ordem(self,vetor): #10
        return sorted(vetor)

    def comissao(self, salario, vendas): #11
        if vendas <= 1500:
            return (salario + (vendas*(3/100)))
        else:
            return (salario+(vendas*(5/100)))

    def saldo(self,saldo,debito,credito): #12
        if (saldo - debito + credito) >= 0:
            return "positivo"
        elif (saldo - debito + credito) < 0:
            return "negativo"

    def numNegativo(self,vetor): #15
        resul=0
        for i in range(len(vetor)):
            if vetor[i] < 0:
                resul += 1
        return resul

    def somaMenor40(self,vetor): #16
        soma = 0
        for i in range(len(vetor)):
            if vetor[i] < 40:
                soma += vetor[i]
        return soma

    def mediaAritmetica(self, num1, num2): #17
        num2 += 1
        numeros = range(num1, num2)
        media = sum(numeros) / len(numeros)
        return(media)  # 57.5

    def media(self,vetor):
        return (sum(vetor) / len(vetor))

    def maior(self,vetor):
        return max(vetor)

    def acimaDaMedia(self,vetor):
        media = self.media(vetor)
        return sum( i > media for i in vetor)

    def abaixoDaMedia(self,vetor,media):
        media = self.media(vetor)
        return sum( i < media for i in vetor)

    def percentual150(self,vetor):
        return (sum(i < 150 for i in vetor)/len(vetor)*100)

