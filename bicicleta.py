class Bicicleta:
    def __init__(self, veloc_atual, altura_cela, calibragem_pneus):
        self.veloc_atual = veloc_atual
        self.altura_cela = altura_cela
        self.calibragem_pneus = calibragem_pneus


    def regular_cela(self):
        self.altura_cela_min = 0
        self.altura_cela_max = 30

        if self.veloc_atual == 0:
            if self.altura_cela >= self.altura_cela_min and self.altura_cela <= self.altura_cela_max:
                self.altura_cela = 15
                print("Cela regulada!")
            else:
                print("Valor inválido para altura de cela!")
        else:
            print("Bicicleta em movimento! Pare para regular a cela.")

    def calibrar_pneus(self):
        self.calibragem_pneus_min = 35
        self.calibragem_pneus_max = 45

        if self.veloc_atual == 0:
            if self. calibragem_pneus >= self.calibragem_pneus_min and self.calibragem_pneus <= self.calibragem_pneus_max:
                self.calibragem_pneus = 39
                print("Pneu calibrado!")
            else:
                print("Valor inválido para calibragem de pneus!")
        else:
            print("Bicicleta em movimento! Pare para calibrar o pneu.")


    def andar_bicicleta(self):
        self.vel_min = 0
        self.vel_max = 50
        if self.veloc_atual == 0:
            print("A bicicleta está parada.")
        while True:
            a = int(input("Deseja acelerar (1), desacelerar (2) ou parar (3)?"))
            if a == 1:
                if self.veloc_atual < self.vel_max:
                    self.acelerar()
                    print(f"Você está andando a {self.veloc_atual}km por hora.")
                else:
                    print("Você ultrapassou a velocidade máxima!")
            elif a == 2:
                if self.veloc_atual > self.vel_min:
                    self.desacelerar()
                    print(f"Você está andando a {self.veloc_atual}km por hora.")
                else:
                    print("Você está parado!")
            elif a == 3:
                self.veloc_atual = 0
                print("A bicicleta parou.")
                break

    def acelerar(self):
        self.veloc_atual += 5

    def desacelerar(self):
        self.veloc_atual -= 5


def main():
    bicicleta1 = Bicicleta(int(input("Insira uma velocidade (0-48): ")),int(input("Insira a altura da cela (0-30): ")), int(input("Insira a calibragem dos pneus (35-45): ")))
    if bicicleta1.veloc_atual == 0:
        bicicleta1.calibrar_pneus()
        bicicleta1.regular_cela()
        bicicleta1.andar_bicicleta()

    else:
        print("Sua bicicleta está em movimento. Pare para realizar as regulagens.")



if __name__ == '__main__':
    main()