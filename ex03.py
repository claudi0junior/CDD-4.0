#altere o execicio anterior para permitir achar o nome de um aluno na lista.


qtd = int(input("quantos alunos tem na sala:"))
alunos = [0] * qtd

for x in range(qtd):
    alunos[x] = input("insira o nome de um aluno:")

pergunta = input("insira um nome inserido acima, para mostrar está sua posição:")

for y in range(qtd):
    if pergunta == alunos[y]:
        print(f"o nome {pergunta}, está na posição: {[y]}")
        break
else:
    print("nome não está na lista")