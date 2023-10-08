#escreva um algoritmo que solicite ao usuario a entrada de 5 nomes, e que exiba a lista desses nomes na tela.
#após exibir essa lista, o programa deve mostrar tambem os nomes na ordem inversa em que os digitou, um por linha.


nome = [0, 0, 0, 0, 0]
nome2 = [0, 0, 0, 0, 0]
i = 4

for x in range(5):
    nome[x] = input("digite um nome:")

print(f"ordem digitada dos nomes: {nome}")

for y in range(5):
    nome2[y] = nome[i]
    print(f"{nome2[y]}")
    i -= 1
