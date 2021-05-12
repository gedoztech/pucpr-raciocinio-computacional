print('Informando a nota dos 10 alunos da turma.')

notas = []
mensagem_erro = 'Valor incorreto. Digite um número entre 0 e 10.'

i = 0
while i < 10:
    while True:
        try:
            notas.append(float(input('Digite a nota do aluno {0}: '.format(i + 1))))
        except ValueError:
            print(mensagem_erro)
            continue
        if notas[i] < 0 or notas[i] > 10:
            print(mensagem_erro)
            notas.remove(notas[i])
            continue
        else:
            break
    i += 1

print('Notas: ', notas)
print('Maior nota: ', max(notas, key=int))
print('Menor nota: ', min(notas, key=int))
