import random

class RadioFM:
    def __init__(self, vol_max, estacoes):
        self.volume_min = 0
        self.volume_max = vol_max
        self.freq_min = 88
        self.freq_max = 108
        self.estacoes = estacoes
        self.volume = None
        self.ligado = False
        self.estacao_atual = None
        self.frequencia_atual = None
        self.antena_habilitada = False

    def ligar(self):
        if self.ligado:
            print("Aparelho já está ligado!")
        else:
            self.ligado = True
            print("Rádio foi ligado!")
            self.volume = self.volume_min
            if self.antena_habilitada:
                self.estacao_atual = list(self.estacoes.values())[0]
                self.frequencia_atual = list(self.estacoes.keys())[0]
                print(f"Frequencia: {self.frequencia_atual}\nVocê está na rádio: {self.estacao_atual}\n")
            else:
                print("Antena desativada. Ative sua antena para ouvir a estação.")

    def desligar(self):
        if self.ligado:
            self.ligado = False
            self.volume = None
            self.frequencia_atual = None
            self.estacao_atual = None
            print("Radio foi desligado!\n")
        else:
            print("Rádio já está desligado!")

    def aumentar_volume(self, valor=None):
        if self.ligado:
            if valor == None:
                if self.volume < self.volume_max and self.volume + 1 < self.volume_max:
                    self.volume += 1
                    print(f"Volume atual: {self.volume}")
                else:
                    self.volume = self.volume_max
                    print("Você atingiu o volume máximo!")
                    print(f"Volume atual: {self.volume}")
            else:
                if self.volume < self.volume_max and self.volume + valor < self.volume_max:
                    self.volume += valor
                    print(f"Volume atual: {self.volume}")
                else:
                    self.volume = self.volume_max
                    print("Você atingiu o volume máximo!")
                    print(f"Volume atual: {self.volume}")
        else:
            print("Rádio desligado!")

    def diminuir_volume(self, valor=None):
        if self.ligado:
            if valor == None:
                if self.volume > self.volume_min and self.volume - 1 > self.volume_min:
                    self.volume -= 1
                    print(f"Volume atual: {self.volume}")
                else:
                    self.volume = self.volume_min
                    print("Você atingiu o volume minimo!")
                    print(f"Volume atual: {self.volume}")
            else:
                if self.volume > self.volume_min and self.volume - valor > self.volume_min:
                    self.volume -= valor
                    print(f"Volume atual: {self.volume}")
                else:
                    self.volume = self.volume_min
                    print("Você atingiu o volume minimo!")
                    print(f"Volume atual: {self.volume}")
        else:
            print("Rádio desligado!")

    def ajustar_volume(self, valor):
        if self.ligado:
            if self.volume_max > valor > self.volume_min:
                self.volume = valor
                print(f"Volume atual: {self.volume}")
            else:
                print(f"Valor inválido, escolha um número entre: {self.volume_min} e {self.volume_max}.")

    def mudar_frequencia(self, valor=0):
        if self.antena_habilitada and self.ligado:
            if valor > 0:
                if valor in list(self.estacoes.keys()):
                    self.frequencia_atual = valor
                    self.estacao_atual = self.estacoes[valor]
                    if self.antena_habilitada:
                        print(f"Frequencia: {self.frequencia_atual}\nEstação: {self.estacao_atual}\n")
                    else:
                        print("Antena desativada. Ative sua antena para ouvir a estação.")

                else:
                    self.estacao_atual = 'Estação inexistente'
                    print(self.estacao_atual)
            else:
                i = 0
                while i < len(self.estacoes):
                # for i in range(len(self.estacoes)):
                    if self.frequencia_atual != None:
                        if self.frequencia_atual == list(self.estacoes.keys())[i]:
                            if i < len(self.estacoes) -1:
                                self.frequencia_atual = list(self.estacoes.keys())[i+1]
                                self.estacao_atual = list(self.estacoes.values())[i+1]
                                if self.antena_habilitada:
                                    print(f"Frequencia: {self.frequencia_atual}\nEstação: {self.estacao_atual}\n")
                                    break
                                else:
                                    print("Antena desativada. Ative sua antena para ouvir a estação.")
                                    break
                            else:
                                self.frequencia_atual = list(self.estacoes.keys())[0]
                                self.estacao_atual = list(self.estacoes.values())[0]
                                if self.antena_habilitada:
                                    print(f"Frequencia: {self.frequencia_atual}\nEstação: {self.estacao_atual}\n")
                                    break
                                else:
                                    print("Antena desativada. Ative sua antena para ouvir a estação.")
                                    break

                    else:
                        self.frequencia_atual = round(random.uniform(88,108),1)
                        if self.frequencia_atual not in list(self.estacoes.keys()):
                            self.estacao_atual = 'Interferência'
                        else:
                            self.estacao_atual = self.estacoes[self.frequencia_atual]
                        print(f"Frequencia: {self.frequencia_atual}\nEstação: {self.estacao_atual}\n")
                        break

                    i += 1

def main():
    estacoes = {89.5: 'Cocais',
                91.5: 'Mix',
                94.1: 'Boa',
                99.1: 'Clube'}


    r1 = RadioFM(100, estacoes)
    r1.ligar()
    r1.mudar_frequencia(100)
    r1.ligar()
    r1.desligar()

    r1.antena_habilitada = True
    r1.ligar()
    r1.mudar_frequencia()
    r1.mudar_frequencia()
    r1.aumentar_volume()
    r1.aumentar_volume(10)
    r1.aumentar_volume(88)
    r1.aumentar_volume(5)
    r1.diminuir_volume(5)
    r1.diminuir_volume(100)
    r1.ajustar_volume(105)
    r1.ajustar_volume(30)

    r1.mudar_frequencia(89.5)
    for i in range(4):
        r1.mudar_frequencia()
    r1.desligar()

    r1.antena_habilitada = False

    r1.ligar()
    r1.antena_habilitada = True
    r1.mudar_frequencia()
    r1.mudar_frequencia(89.5)
    r1.mudar_frequencia()

if __name__ == '__main__':
    main()