class Calculadora:
    estado = None
    numero1 = None
    numero2 = None
    operacao = None
    resultado = None


    def ligar(self):
        self.resetar()
        self.estado = 'ligado'
        print(f'Calculadora ligada!')
    def desligar(self):
        self.estado = 'desligado'
        print(f'Calculadora desligada!')

    def resetar(self):
        self.numero1 = 0
        self.numero2 = 0
        self.operacao = None
        self.resultado

    def receber_num(self):
        self.numero1 = float(input("Insira o 1° numero: "))
        self.numero2 = float(input("Insira o 2° numero: "))

    def mais_num(self):
        self.numero1 = self.resultado
        self.numero2 = float(input("Insira mais um número: "))

    def soma(self):
        if self.estado =='ligado':
            self.resultado = self.numero1 + self.numero2
            print("Resultado: ",self.resultado)
        else:
            return "Calculadora desligada!"

    def subtracao(self):
        if self.estado == 'ligado':
            self.resultado = self.numero1 - self.numero2
            print("Resultado: ",self.resultado)
        else:
            return "Calculadora desligada!"

    def multip(self):
        if self.estado == 'ligado':
            self.resultado = self.numero1 * self.numero2
            print("Resultado: ",self.resultado)
        else:
            return "Calculadora desligada!"

    def divisao(self):
        if self.estado == 'ligado':
            self.resultado = self.numero1 / self.numero2
            print("Resultado: ",self.resultado)
        else:
            return "Calculadora desligada!"

    def op(self):
        self.operacao = int(input("1-soma; 2-subtração; 3-multiplicacao; 4-divisão "))
        if self.operacao == 1:
            self.soma()
        elif self.operacao == 2:
            self.subtracao()
        elif self.operacao == 3:
            self.multip()
        elif self.operacao == 4:
            self.divisao()
        else:
            print("Valor inválido! Tente novamente.")
def main():
    calculadora1 = Calculadora()
    calculadora1.ligar()
    calculadora1.receber_num()
    calculadora1.op()
    continuar = ""
    while True:
        continuar = input("Deseja fazer outra operação? s/n ").lower()
        if continuar == "s":
            calculadora1.mais_num()
            calculadora1.op()
        elif continuar == "n":
            print("Encerrado!")
            calculadora1.desligar()
            break



if __name__ == '__main__':
    main()