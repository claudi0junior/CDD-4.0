# escreva um codigo que permita a leitura das notas de uma turma de 5 alunos e guarde num vetor, calcular a media da turma e contar quantos alunos
# obtiveram nota acima desta média e o resultado da contagem.


notas = [0, 0, 0, 0, 0]
soma = 0
qtd = 0

for x in range(5):
    notas[x] = float(input("insira uma nota:"))

for x in range(5):
    soma = notas[x] + soma

media = soma / 5

for x in range(5):
    if notas[x] >= media:
        qtd += 1

print(f"a media da sala foi de: {media}, e os alunos que alcançaram ela ou maior foi de:{qtd}")
