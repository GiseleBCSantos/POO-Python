from time import *

class Relogio_Digital_Simples:
    ligado = False
    hora = 0
    minuto = 0
    segundo = 0

    def ligar_desligar(self):
        if self.ligado == False:
            self.ligado = True
        else:
            self.ligado = False

    def definir_hora(self):
        if self.ligado:
            self.hora = int(input("Insira a hora atual: "))
            self.minuto = int(input("Insira o minuto atual: "))
            self.segundo = int(input("Insira o segundo atual: "))

    def definir_alarme(self):
        if self.ligado:
            self.hora_alarme = int(input("Insira a hora para o alarme: "))
            self.minuto_alarme = int(input("Insira o minuto para o alarme: "))


    def mostrar_hora(self):
        while self.ligado:
            print(f"{self.hora:02}:{self.minuto:02}:{self.segundo:02}")
            if self.hora == self.hora_alarme and self.minuto == self.minuto_alarme:
                print("ALARME!!!")
                self.hora_alarme = None
                self.minuto_alarme = None
                break
            sleep(1)
            self.segundo += 1
            if self.segundo == 60:
                self.segundo = 0
                self.minuto += 1
            if self.minuto == 60:
                self.minuto = 0
                self.hora += 1
            if self.hora >= 24:
                self.hora = 0
                self.minuto = 0
                self.segundo = 0
        else:
            print("Ligue seu relógio primeiro!")


    def executar_relogio(self):
        while True:
            acao = int(input(
                '1 - Ligar o relógio;\n2 - Definir a hora para o relógio;\n3 - Definir um alarme; \n4 - Iniciar o funcionamento do relógio (só inicie se tiver definido a hora);\n'))

            if acao == 1:
                self.ligar_desligar()
                print("Você ligou o relógio!")
            if acao == 2 and self.ligado:
                self.definir_hora()
            if acao == 3 and self.ligado:
                self.definir_alarme()
            if acao == 4 and self.ligado:
                self.mostrar_hora()
            if not self.ligado:
                print("Ligue seu relógio primeiro.")

def main():
    relogio1 = Relogio_Digital_Simples()
    relogio2 = Relogio_Digital_Simples()


    while True:
        rel = int(input("Com qual relógio você deseja operar? \n1 - relogio1;\n2 - relogio2;\n3 - relogio3 (já operante):\n4 - sair do modo de operação:\n"))
        if rel == 1:
            rel = relogio1
            rel.executar_relogio()
        elif rel == 2:
            rel = relogio2
            rel.executar_relogio()
        elif rel == 3:
            relogio3 = localtime()
            print(f"{relogio3[3]:02}:{relogio3[4]:02}:{relogio3[5]:02}")
        elif rel == 4:
            print("Encerrando operação de relógios!")
            break



if __name__ == '__main__':
    main()