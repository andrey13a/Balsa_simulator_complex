class Embarcacao:

    def __init__(self):

        self.__carga = []
        self.__peso_total = 0
        self.__peso_maximo = 0

        self.__trajeto = []
        self.__parada_atual = 0
        self.__ida = True

    def iniciar(self):
        self.__peso_maximo = float(input('Digite o peso máximo da embarcação: '))
        qtd_paradas = int(input('Digite quantas paradas tem seu trajeto: '))
        for numero in range(1, qtd_paradas + 1):
            self.__trajeto.append(str(input(f'Digite o nome da {numero}° parada: ')))

    def proxima_parada(self):
        if self.__parada_atual == int(len(self.__trajeto) - 1):
            self.__ida = False
        else:
            if not self.__ida and self.__parada_atual == 0:
                self.__ida = True

        if self.__ida:
            self.__parada_atual += 1
        else:
            self.__parada_atual -= 1

    def mostrar_parada(self):
        print(f'Parada atual: {self.__trajeto[self.__parada_atual]}')

    def calcular_carga(self):
        self.__peso_total = 0
        for item in self.__carga:
            self.__peso_total = self.__peso_total + float(item[1])

    def adicionar_carga(self):
        print()
        carga = str(input('Digite o nome da carga: '))
        for numero in range(1, int(input(f'Digite a quantidade de {carga}: ')) + 1):
            temp = []
            peso = (float(input(f'Digite o peso de {numero}° {carga}: ')))
            self.calcular_carga()
            if (self.__peso_total + peso) > self.__peso_maximo:
                print('Peso excedido!')
                break
            else:
                temp.append(str(carga))
                temp.append(peso)
                self.__carga.append(temp)

    def mostrar_carga(self):
        if len(self.__carga) == 0:
            print('Embarcação Vazia!')
            print()
        else:
            self.calcular_carga()
            print(f'Carga total da embarcação: {self.__peso_total}Kg / {self.__peso_maximo}')
            print()
            for numero, item in enumerate(self.__carga):
                print(f'[ {numero + 1} ] {item[0]} = {item[1]}Kg')
            print()

    def retirar_carga(self, id):
        if len(self.__carga) == 0:
            print('Você não possui itens para remover!')
            print()
        else:
            if (id - 1) > len(self.__carga):
                print('Digite um ID válido!')
            else:
                self.__carga.pop(id - 1)
                self.calcular_carga()
