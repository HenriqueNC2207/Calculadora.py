from Operacoes import Operacoes 
from Calculadora import Calculadora

filaOperacoes = []
stack = []

filaOperacoes.append(Operacoes(2,3,'+'))
filaOperacoes.append(Operacoes(14,8,'-'))
filaOperacoes.append(Operacoes(5,6,'*'))
filaOperacoes.append(Operacoes(2147483647,2,'+'))
filaOperacoes.append(Operacoes(18,3,'/'))

calculadora = Calculadora()

while len(filaOperacoes) > 0:

    operacao = calculadora.calcular(filaOperacoes[0])

    filaOperacoes.pop(0)

    resultado = "{} {} {} = {}".format(operacao.valorA, operacao.operador, operacao.valorB, operacao.resultado)

    print(resultado)

    stack.append(resultado)

    if len(filaOperacoes) > 0:
        print("Operações a serem processadas:")

        for operacao in filaOperacoes:
            print("{} {} {}".format(operacao.valorA, operacao.operador, operacao.valorB))
    else:
        print("Resultados dos cálculos: ")
        for result in stack:
            print(result)
    input("Aperte Enter para prosseguir!")
