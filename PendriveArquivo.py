# criar lista de arquivos como um dicionario
# chave sendo o nome do arquivo e o valor o objeto
# espaco ocupado e espaco livre sendo metodos

class PenDrive:
    def __init__(self, id, capacidade):
        self.__id = id
        self.__capacidade = capacidade
        self.__arquivos = {}
        self.__espaco_ocupado = 0
        self.__espaco_livre = self.__capacidade


    def __str__(self):
        tabela_arquivos = ''
        tabela_arquivos += f'Nome:\t\t\tTamanho:\tTipo:\n'
        for i in self.__arquivos.values():
            tabela_arquivos += f'{i.nome}\t\t\t{i.tamanho}\t\t\t{i.tipo}\n'
        espaco_ocupado = f'\nEspaço ocupado: {self.__espaco_ocupado}\n'
        espaco_livre = f'Espaço livre: {self.__capacidade - self.__espaco_ocupado}\n'

        return tabela_arquivos+espaco_ocupado+espaco_livre
        # nome
        # nome =
        # lista de arquivos
        # espaco ocupado
        # espaco livre


    @property
    def id(self):
        return self.__id
    @property
    def capacidade(self):
        return self.__capacidade
    @property
    def arquivos(self):
        return self.__arquivos
    @property
    def espaco_ocupado(self):
        return self.__espaco_ocupado
    @property
    def espaco_livre(self):
        return self.__espaco_livre


    def espacos_ocupado(self):
        self.__espaco_ocupado = 0
        for i in list(self.__arquivos.values()):
            self.__espaco_ocupado += i.tamanho
        self.__espaco_livre = self.__capacidade - self.__espaco_ocupado



    def formatar(self):
        q = input('Deseja formatar o pendrive? s/n (Se digitar "s" todos seus arquivos serão apagados e o pendrive voltará a sua capacidade máxima)\n')
        if q == 's':
            self.__arquivos = {}
            self.__espaco_livre = self.__capacidade
            self.__espaco_ocupado = 0
        else:
            print('Seu pendrive continua com seus arquivos.')


    def adicionar_arquivo(self, arquivo):
        if isinstance(arquivo, Arquivo):
            if arquivo.tamanho <= self.espaco_livre:
                if arquivo.nome not in self.__arquivos.keys():
                    self.__arquivos[arquivo.nome] = arquivo
                    self.espacos_ocupado()
                else:
                    print('ERRO: Nome já está sendo utilizado.')
            else:
                print('ERRO: Espaço insuficiente.')
        else:
            print('ERRO: Tipo inválido.')


    def apagar_arquivo(self, arquivo):
        if isinstance(arquivo, Arquivo):
            if arquivo.nome in list(self.__arquivos.keys()):
                for i in list(self.__arquivos.keys()):
                    if arquivo.nome == i:
                        self.__arquivos.pop(i)
                        self.espacos_ocupado()
            else:
                print('Arquivo não encontrado.')
        else:
            print('Tipo inválido.')


class Arquivo:
    def __init__(self, nome, tipo, tamanho):
        self.__nome = nome
        self.__tipo = tipo
        self.__tamanho = tamanho

    def __str__(self):
        return f'Nome: {self.__nome}\tTamanho: {self.__tamanho}\tTipo: {self.__tipo}'

    @property
    def nome(self):
        return self.__nome
    @property
    def tipo(self):
        return self.__tipo
    @property
    def tamanho(self):
        return self.__tamanho

    def renomear(self, nome):
        self.__nome = nome


pendrive1 = PenDrive(1, 50)

pendrive1.adicionar_arquivo(Arquivo('Video', 1, 10))

print(pendrive1)
print('-------------------------------------------------------')

pendrive1.adicionar_arquivo(Arquivo('Image', 2, 0.5))

print(pendrive1)
print('-------------------------------------------------------')
pendrive1.adicionar_arquivo(Arquivo('Audio', 3, 5))

print(pendrive1)
print('-------------------------------------------------------')
pendrive1.adicionar_arquivo(Arquivo('Audio', 3, 5))

print(pendrive1)
print('-------------------------------------------------------')
pendrive1.adicionar_arquivo(Arquivo('Zip', 4, 30))

print(pendrive1)
print('-------------------------------------------------------')

pendrive1.apagar_arquivo(Arquivo('Zip', 4, 30))

print(pendrive1)
print('-------------------------------------------------------')

pendrive1.formatar()

print(pendrive1)
print('-------------------------------------------------------')



