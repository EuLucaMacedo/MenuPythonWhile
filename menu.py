#Programa Lê dois valores e Apresenta um Menu com Opções!


valor_um = int(input('Digite um Valor: '))
valor_dois = int(input('Digite outro Valor: '))

while True:
    print('''=============== Escolha uma Opção =============== 
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos Números
    [ 5 ] Sair''')
    respo = int(input('Escolha Uma Alternativa: '))
    print('\n')

    if respo == 1:
        print(f'A soma dos valores {valor_um} e {valor_dois} é {valor_um + valor_dois}!')

    elif respo == 2:
        print(f'A multiplicação entre {valor_um} e {valor_dois} é {valor_um * valor_dois}!')

    elif respo == 3:
        if valor_um > valor_dois:
            print(f'O valor {valor_um} é MAIOR que o valor {valor_dois}!')
        elif valor_um < valor_dois:
            print(f'O valor {valor_um} é MENOR que o valor {valor_dois}!')
        else:
            print('Os valores são IGUAIS!')

    elif respo == 4:
        valor_um = int(input('Digite um novo primeiro valor: '))
        valor_dois = int(input('Digite um novo segundo valor: '))

    elif respo == 5:
        print('Finalizando o programa...')
        break

    else:
        print('Opção inválida. Tente novamente.')

print('Fim do Programa!')