import Operacoes
class Calculadora:

    def calcular(self, operacao):

        def soma(a, b):
            return a + b

        def subtracao(a, b):
            return a - b

        def multiplicacao(a, b):
            return a * b

        def divisao(a, b):
            if b == 0:
                raise ValueError("Divisão por zero não é permitida")
            return a / b

        operacoes = {
            '+': soma,
            '-': subtracao,
            '*': multiplicacao,
            '/': divisao
        }

        operador = operacao.operador
        operacao.resultado = operacoes.get(operador, lambda a, b: 0)(operacao.valorA, operacao.valorB)
        return operacao