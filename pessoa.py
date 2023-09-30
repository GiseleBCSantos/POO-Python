class Pessoa:
    def __init__(self, nome, idade, peso, altura, sexo, estado='vivo', estado_civil='solteiro', conjuge=None):
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso
        self.__altura = altura
        self.__sexo = sexo
        self.__estado = estado.lower()
        self.__estado_civil = estado_civil.lower()
        self.__conjuge = conjuge

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        if self.__estado != 'vivo':
            return f'{self.__nome} está morto.'
        else:
            return self.__idade
    @idade.setter
    def idade(self, valor):
        print('sem permissão')



    @property
    def peso(self):
        if self.__estado == 'vivo':
            return self.__peso
        else:
            return f'{self.__nome} está morto.'
    @peso.setter
    def peso(self, valor):
        print('sem permissão')
    @property
    def altura(self):
        if self.__estado == 'vivo':
            return self.__peso
        else:
            return f'{self.__nome} está morto.'
    @altura.setter
    def altura(self, valor):
        print('sem permissão')


    @property
    def sexo(self):
        return self.__sexo

    @property
    def estado(self):
        return self.__estado
    @estado.setter
    def estado(self, value):
        print('sem permissão')


    @property
    def estado_civil(self):
        return self.__estado_civil
    @estado_civil.setter
    def estado_civil(self, value):
        print('sem permissão')


    @property
    def conjuge(self):
        return self.__conjuge
    @conjuge.setter
    def conjuge(self, value):
        print('sem permissão')



    def envelhecer(self):
        if self.__estado == 'vivo':
            if self.__idade < 21:
                self.__altura += 5
                self.__idade += 1
                print(f'{self.__nome} está com {self.__idade} anos e {self.__altura} cm de altura.')
            else:
                self.__idade += 1
                print(f"{self.__nome} fez aniversário! Ela agora tem {self.__idade} anos.")
        else:
            print(f"{self.__nome} não está mais viva.")

    def engordar(self, value=0):
        if self.__estado == 'vivo':
            self.__peso += value
            print(f'{self.__nome} engordou e agora pesa {self.__peso}')
        else:
            print(f"Operação não realizada. {self.__nome} está morta.")

    def emagrecer(self, value=0):
        if self.__estado == 'vivo':
            self.__peso -= value
            print(f'{self.__nome} emagreceu e agora pesa {self.__peso}')
        else:
            print(f"{self.__nome} não está mais viva.")

    def crescer(self, value):
        if self.__estado == 'vivo':
            if self.__idade < 21:
                self.__altura += value
                print(f'{self.__nome} cresceu e agora tem {self.__altura} de altura.')
            else:
                print(f'{self.__nome} não pode mais crescer pois está com 21 anos ou mais.')
        else:
            print(f"{self.__nome} não está mais viva.")

    def casar(self, value):
        if self.__estado == 'vivo':
            if self != value:
                if self.__estado_civil != 'casado(a)':
                    if self.__idade >=18:
                        if value.__estado == 'vivo':
                            if value.__estado_civil != 'casado(a)':
                                if value.idade >=18:

                                        self.__estado_civil = 'casado(a)'
                                        value.__estado_civil = 'casado(a)'
                                        self.__conjuge = value
                                        value.__conjuge = self
                                        print(f"{self.__nome} está casado com {value.__nome}.")

                                else:
                                    print(f"Casamento não permitido. {value.__nome} é de menor.")
                            else:
                                print(f"“Casamento não realizado. {value.__nome} é casado.”")
                        else:
                            print(f"{value.__nome} não está vivo, portanto não pode se casar.")
                    else:
                        print(f"Casamento não permitido. {self.__nome} é de menor.")
                else:
                    print(f"Casamento não realizado. {self.__nome} é casado.")
            else:
                print("Você não pode se casar consigo mesmo.")
        else:
            print(f"Casamento não realizado. {self.__nome} está morto.")

    def morrer(self):
        if self.__estado == 'vivo':
            self.__estado = 'morto'
            if self.__estado_civil == 'casado(a)':
                self.__conjuge.__estado_civil = 'viuvo(a)'
                print(f'{self.__nome} morreu.')

            else:
                print(f'{self.__nome} morreu.')
        else:
            print(f"{self.__nome} já estava morto(a).")




maria = Pessoa("Maria", 5, 20, 100, 'F')


joao = Pessoa("Joao", 12, 40, 140, 'M')


pedro = Pessoa("Pedro", 22, 65, 170, 'M')


bia = Pessoa("Bia", 18, 55, 160, 'F')


julia = Pessoa('Julia', 30, 65, 170,'F')


carlos = Pessoa('Carlos', 2, 11, 80,'M')


jonas = Pessoa('Jonas', 34, 70, 180, 'M')


# a)
print('a)')
maria.idade = 10

# b)
print('b)')
maria.envelhecer()

# c)
print('c)')
pedro.crescer(2)

# d)
print('d)')
bia.casar(carlos)

# e)
print('e)')
pedro.casar(maria)

# f)
print('f)')
pedro.casar(julia)

# g)
print('g)')
pedro.casar(bia)

# h)
print('h)')
maria.morrer()

# i)
print('i)')
maria.engordar()

# j)
print('j)')
bia.casar(jonas)

# k)
print('k)')
bia.morrer()

# l)
print('l)')
pedro.morrer()

# m)
print('m)')
jonas.casar(julia)

# n)
print('n)')
pedro.casar(bia)

# o)
print('o)')
print(pedro.idade)

# p)
print('p)')
joao.idade = 50

