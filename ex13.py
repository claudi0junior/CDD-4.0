# faça um algoritmo que leia 30 valores do tipo inteiro e armazene-os em um vetor. a seguir , o algoritmo deverá informar
# (1) todos os numeros pares que existem no vetor;
# (2) o menor e o maior valor existente no vetor;
# (3) quantos dos valores do vetor são maiores que a média desses valores:


numero = [0] * 30
N_pares = 0
soma = 0
a = 0
b = 0

for x in range(30):
    numero[x] = int(input("insira um mumero inteiro:"))

    if numero[x] % 2 == 0:
        N_pares += 1

maior = max(numero)
menor = min(numero)

for y in range(30):
    soma = soma + numero[a]

    a += 1
media = soma / 30
c = 0
for z in range(30):
    if numero[b] >= media:
        c += 1
    b += 1

print(f"(1) os numeros pares foi de: {N_pares}")
print(f"(2) o maior numero foi de: {maior}, e o menor de: {menor}")
print(f"(3) a média dos numeros foi de: {media}, e os numeros que alcaçaram essa média foi de: {c}")