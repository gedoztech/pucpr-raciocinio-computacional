total_turmas = 9
total_alunos = 24
total_avaliacoes = 5
notas_alunos = []

# retorno esperado:

# notas_alunos = [
    # turma
    # [
        # aluno
        # [
            # avaliação
            # [
                # notas e média
                # n1, n2, n3, n4, n5, média
            # ]
        # ]
    #]
# ]

for i in range(total_turmas):
    notas_j = []
    for j in range(total_alunos):
        notas_k = []
        for k in range(total_avaliacoes):
            mensagem = 'Digite a nota do aluno {0} da avaliação {1} da turma {2}: '.format(j+1, k+1, i+1)
            nota = float(input(mensagem))
            notas_k.append(nota)
        notas_k.append(sum(notas_k)/total_avaliacoes)
        notas_j.append(notas_k)
    notas_alunos.append(notas_j)
        
print(notas_alunos)
