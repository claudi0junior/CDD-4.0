#faça um codigo para ler um vetor de 30 numeros. após isto, ler mais um numero qualquer, calcular e escrever quntas
#vezes esse numero aparece no vetor.


numero = [0] * 30

for y in range(30):
    numero[y] = int(input("insira um numero:"))

qtd = 0
num = int(input("insira o numero que irá calcular e tambem quantas vezes ele aparece n vetor:"))

for y in range(30):
    if num == numero[y]:
        qtd+=1

print(f"o numero {num} , aparece {qtd} vezes na lista")