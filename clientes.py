campos_clientes = ['Nome', 'Idade', 'CPF']
dados_clientes = []

for i in range(2):
    print('Digite as inforações abaixo referentes ao cliente nº {0}'.format(i+1))
    nome = input('Nome: ')
    idade = input('Idade: ')
    cpf = input('CPF: ')
    dados = [nome, idade, cpf]
    dados_clientes.append(dados)
    print('')

print("==========================", file=open("clientes.txt", "a"))
colunas = ''
for campo in campos_clientes:
    colunas += "|" + campo + ' '
print(colunas, file=open("clientes.txt", "a"))

print('')
for dados in dados_clientes:
    valores = ''
    for dado in dados:
        valores += "|" + dado + ' '
    print(valores, file=open("clientes.txt", "a"))

print("==========================", file=open("clientes.txt", "a"))

