nome = 'Calculadora DigiConv'


def calcula():
    print('Menu de opções: ')
    print('1 => Converter Bitconins em Reais')
    print('2 => Converter Reais em Bitcoins')
    print('3 => Sair')
    opcao = int(input('Informe a opção desejada: '))
    if opcao == 1:
        bitcoins = float(input('Informe o valor em Bitcoins a ser convertido: '))
        taxa = float(input('Informe o valor do Bitcoin em reais no dia de hoje: '))
        reais = taxa * bitcoins
        print('Valor em Reais: ', reais)
        calcula()
    elif opcao == 2:
        reais = float(input('Informe o valor em Reais a ser convertido: '))
        taxa = float(input('Informe o valor do Real em bitcoins no dia de hoje: '))
        bitcoins = taxa * reais
        print('Valor em Bitcoins: ', bitcoins)
        calcula()
    elif opcao == 3:
        print('Programa encerrado. Obrigado por utilizar a ', nome)
    else:
        print('Opção errada, favor tentar novamente.')
        calcula()


print('Bem vindo à ', nome, '!')
calcula()
