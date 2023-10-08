#perguntar ao usuario quantos alunos tem na sala e criar um array, unidimenssional(vetor) com o nome de todos os alunos
# da sala


qtd = int(input("quantos alunos tem na sala:"))
alunos = [0] * qtd

for x in range(qtd):
    alunos[x] = input("insira o nome de um aluno:")

print(f"Esses foram os nomes dos alunos inseridos: {alunos}.")