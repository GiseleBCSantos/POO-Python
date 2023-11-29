class Banco:
    def __init__(self):
        self._contas = {}

    def __str__(self):
        return self._contas

    @property
    def contas(self):
        return self._contas

    @contas.setter
    def contas(self, value):
        print('Sem permissão')

    def adicionar_conta(self, conta):
        self._contas[conta.numero] = conta

    def sacar(self, conta, value):
        conta.sacar(value)



class ContaCorrente:
    seq = 0
    def __init__(self, saldo):
        ContaCorrente.seq += 1
        self._numero = ContaCorrente.seq
        self._saldo = saldo


    def __str__(self):
        return f'Numero da conta: {self._numero} \nSaldo da conta: {self._saldo:.2f}\n'

    @property
    def numero(self):
        return self._numero

    @property
    def saldo(self):
        return f'R$ {self._saldo:.2f}'

    @saldo.setter
    def saldo(self, value):
        print('Sem permissão')

    def creditar(self, value):
        self._saldo += value
        print(f'R$ {value} creditado com sucesso. Saldo atual: R$ {self._saldo}')


    def debitar(self, value):
        if self._saldo - value >= 0:
            self._saldo -= value
            print(f'R$ {value} debitado com sucesso. Saldo atual: R$ {self._saldo}')

        else:
            print('Saldo insuficiente!')


    def transferir(self, value, conta):
        if isinstance(conta, ContaCorrente):
            if self._saldo - value >= 0:
                self._saldo -= value
                conta._saldo += value
                print(f'Valor transferido com sucesso para conta de número {conta.numero}. Saldo atual: R$ {self._saldo}.')
            else:
                print('Saldo insuficiente!')
        else:
            print('ERRO: Tipo inválido.')

    def sacar(self, valor):
        if self._saldo - 2 >= 0:
            self._saldo -= (valor+2)
            print(f'R$ {valor:.2f} sacado com sucesso!\nCobrança para saque: R$ 2.00\nSaldo atual: R$ {self._saldo:.2f}')
        else:
            print('Saldo insuficiente!')


class ContaPoupanca(ContaCorrente):
    def __init__(self, saldo, taxa_juros):
        super().__init__(saldo)
        self.__taxa_juros = taxa_juros
        self.__qntd_saques = 0

    def __str__(self):
        return f'{super().__str__()}Taxa de juros: {self.__taxa_juros}%\n'


    @property
    def taxa_juros(self):
        return self.__taxa_juros

    @taxa_juros.setter
    def taxa_juros(self, value):
        print('Sem permissão')

    @property
    def qntd_saques(self):
        return self.__qntd_saques

    @qntd_saques.setter
    def qntd_saques(self, value):
        print('Sem permissão.')


    def render_juros(self):
        juros = self._saldo * (self.__taxa_juros / 100)
        self._saldo += juros
        print(self)

    def sacar(self, valor):
        self.__qntd_saques += 1
        if self.__qntd_saques < 5:
            self._saldo -= valor
            print(f'R$ {valor:.2f} sacado com sucesso!\nSaldo atual: R$ {self._saldo:.2f}')
        else:
            if self._saldo - 0.5 >= 0:
                self._saldo -= (valor+0.5)
                print(f'R$ {valor:.2f} sacado com sucesso!\nCobrança para saque: R$ 0.50\nSaldo atual: R$ {self._saldo:.2f}')
            else:
                print('Saldo insuficiente!')



class ContaImposto(ContaCorrente):
    def __init__(self, saldo, percentual_imposto):
        super().__init__(saldo)
        self.__percentual_imposto = percentual_imposto

    def __str__(self):
        return f'{super().__str__()}Percentual de imposto: {self.percentual_imposto}%\n'

    @property
    def percentual_imposto(self):
        return self.__percentual_imposto

    @percentual_imposto.setter
    def percentual_imposto(self, value):
        print('Sem permissão')


    def calcula_imposto(self):
        imposto = self._saldo * (self.__percentual_imposto / 100)
        self._saldo -= imposto
        print(self)




conta1 = ContaCorrente(500)
conta2 = ContaPoupanca(1000, 5)
conta3 = ContaCorrente(100)
conta4 = ContaPoupanca(2000, 3)

banco = Banco()
banco.adicionar_conta(conta1)
banco.adicionar_conta(conta2)
banco.adicionar_conta(conta3)
banco.adicionar_conta(conta4)

banco.sacar(conta1, 50)
print('----------------------------')
for i in range(5):
    banco.sacar(conta4, 10)
    print('----------------------------')















