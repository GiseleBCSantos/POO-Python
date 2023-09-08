import time

class Semaforo:
    estado = "desligado";
    luz_atual = None;
    tempo_luz_verde = None
    tempo_luz_amarela = None
    tempo_luz_vermelha = None

    def ligar(self):
        self.estado = "ligado";
        self.luz_atual = "vermelho";
        self.configurar_tempo_luzes()
        while True:
            self.gerenciar_tempo()

    def desligar(self):
        estado = "desligado";
        self.luz_atual = None;

    def mudar_cor(self):
        if self.luz_atual == "vermelho":
            self.luz_atual = "verde"

        elif self.luz_atual == "verde":
            self.luz_atual = "amarelo"

        elif self.luz_atual == "amarelo":
            self.luz_atual = "vermelho"

        else:
            print("Inválido")


    def configurar_tempo_luzes(self):
        self.tempo_luz_verde = int(input("Quantos segundos o sinal devera ficar no sinal verde? "))
        self.tempo_luz_amarela = int(input("Quantos segundos o sinal devera ficar no sinal amarelo? "))
        self.tempo_luz_vermelha = int(input("Quantos segundos o sinal devera ficar no sinal vermelho? "))


    def gerenciar_tempo(self):
        # while True:
        print("Cor atual: ", self.luz_atual)
        if self.luz_atual == "vermelho":
            time.sleep(self.tempo_luz_vermelha)
            self.mudar_cor()
        elif self.luz_atual == "verde":
            time.sleep(self.tempo_luz_verde)
            self.mudar_cor()
        elif self.luz_atual == "amarelo":
            time.sleep(self.tempo_luz_amarela)
            self.mudar_cor()
        else:
            print("Inválido")



def main():
    semaforo1 = Semaforo()
    semaforo1.ligar()


if __name__ == '__main__':
    main()


