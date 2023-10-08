# faça um codigo para ler 5 numeros e armazenar em um vetor. após a leitura total dos 5 numeros, o codigo deve escrever
# esses 5 numeros lidos na ordem inversa.


numeros = [0, 0, 0, 0, 0]
numeros2 = [0, 0, 0, 0, 0]
qtd = 4

for x in range(5):
    numeros[x] = int(input("digite um numero:"))

for y in range(5):
    numeros2[y] = numeros[qtd]
    qtd-=1

print(f"o resultado inverso dos numeros inseridos é: {numeros2}")
