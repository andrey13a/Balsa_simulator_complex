from minhaclasse import Embarcacao

embarcacao = Embarcacao()

print(' DEFINIÇÕES INICIAIS '.center(43, '='))
embarcacao.iniciar()

while True:
    print(' BARCA SIMULATOR '.center(43, '='))
    embarcacao.mostrar_parada()
    embarcacao.mostrar_carga()

    opcao = int(input('1 para ADICIONAR / 2 para REMOVER / 3 Prox. PARADA: '))
    if opcao == 1:
        while True:
            print(' ADICIONAR '.center(43, '='))
            embarcacao.mostrar_carga()
            opcao = int(input('0 CANCELAR / 1 CONTINUAR: '))
            if opcao == 0:
                break
            elif opcao == 1:
                embarcacao.adicionar_carga()
            else:
                print('Opção inválida!')


    elif opcao == 2:
        while True:
            print(' REMOVER '.center(43, '='))
            embarcacao.mostrar_carga()
            id = int(input('0 CANCELAR / Digite o ID para remover: '))
            if id == 0:
                break
            else:
                embarcacao.retirar_carga(id)

    elif opcao == 3:
        embarcacao.proxima_parada()

    else:
        print('Ação inválida!')
