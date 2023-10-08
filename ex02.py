#altere o exercicio anterior e mostre na tela, ao final o nome de cada aluno e sua respectiva posiçao no array


qtd = int(input("quantos alunos tem na sala:"))
alunos = [0] * qtd

for x in range(qtd):
    alunos[x] = input("insira o nome de um aluno:")

for y in range(qtd):
    print(f"na posição {y}, está o nome {alunos[y]}.")