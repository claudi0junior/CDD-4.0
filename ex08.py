# faça um codigo para ler 5 nomes de usuarios e suas respectivas senhas, e armazenar cada lista em um array diferente, após
# completar a digitão imprimir, nome, senha e a posição dos dados no array.


nome = [0, 0, 0, 0, 0]
senha = [0, 0, 0, 0, 0]
posit = [0, 0, 0, 0, 0]
num = 0
o = 0

for x in range(5):
    nome[x] = input("digite seu nome:")

for y in range(5):
    senha[y] = int(input("Agora digite a sua senha:"))

for p in range(5):
    posit[p] = num
    num += 1

for z in range(5):
    print(f"seu nome é {nome[o]}, e sua respectiva senha é {senha[o]} , na posição: {posit[o]}")
    o += 1
