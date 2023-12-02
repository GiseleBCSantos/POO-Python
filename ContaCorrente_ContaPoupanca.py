class ContaCorrente:
    seq = 0
    def __init__(self, saldo):
        ContaCorrente.seq += 1
        self._numero = ContaCorrente.seq
        self.__saldo = saldo


    def __str__(self):
        return f'Numero da conta: {self._numero} \nSaldo da conta: {self.__saldo:.2f}\n'

    @property
    def numero(self):
        return self._numero

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, value):
        print('Sem permissão')

    def creditar(self, value):
        self.__saldo += value
        print(f'R$ {value} creditado com sucesso. Saldo atual: R$ {self.__saldo}')


    def debitar(self, value):
        if self.__saldo - value >= 0:
            self.__saldo -= value
            print(f'R$ {value} debitado com sucesso. Saldo atual: R$ {self.__saldo}')

        else:
            print('Saldo insuficiente!')


    def transferir(self, value, conta):
        if isinstance(conta, ContaCorrente):
            if self.__saldo - value >= 0:
                self.debitar(value)
                conta.creditar(value)
            else:
                print('Saldo insuficiente!')
        else:
            print('ERRO: Tipo inválido.')


class ContaPoupanca(ContaCorrente):
    def __init__(self, saldo, taxa_juros):
        super().__init__(saldo)
        self.__taxa_juros = taxa_juros


    def __str__(self):
        return f'{super().__str__()}Taxa de juros: {self.__taxa_juros}%\n'


    @property
    def taxa_juros(self):
        return self.__taxa_juros

    @taxa_juros.setter
    def taxa_juros(self, value):
        print('Sem permissão')


    def render_juros(self):
        juros = self.saldo * (self.__taxa_juros / 100)
        self.creditar(juros)
        print(self)



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
        imposto = self.saldo * (self.__percentual_imposto / 100)
        self.debitar(imposto)
        print(self)




# Criação de contas
conta_1 = ContaCorrente(100)
conta_2 = ContaCorrente(200)

print(conta_1)
print(conta_2)
print('-------------------------------------------------------')


conta_1_poupanca = ContaPoupanca(300, 5)
conta_2_poupanca = ContaPoupanca(400, 8)


print(conta_1_poupanca)
print(conta_2_poupanca)
print('-------------------------------------------------------')

conta_1_contaImposto = ContaImposto(100, 10)
conta_2_contaImposto =  ContaImposto(100, 12)

print(conta_1_contaImposto)
print(conta_2_contaImposto)

print('-------------------------------------------------------')

# Teste de métodos da ContaCorrente
conta_1.creditar(50)

print(conta_1)

print('-------------------------------------------------------')
conta_1.debitar(151)
print('-------------------------------------------------------')
conta_1.debitar(50)
print('-------------------------------------------------------')
print(conta_1.saldo)
print('-------------------------------------------------------')
conta_1.transferir(50, conta_2)
print(conta_1)
print(conta_2)
print('-------------------------------------------------------')
conta_2.transferir(100, conta_1)
print(conta_1)
print(conta_2)
print('-------------------------------------------------------')
conta_1_poupanca.render_juros()

conta_2_poupanca.render_juros()

print('-------------------------------------------------------')
conta_1_contaImposto.calcula_imposto()

conta_2_contaImposto.calcula_imposto()


















