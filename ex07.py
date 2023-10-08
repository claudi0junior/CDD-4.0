# faça um codigo para ler 5 numeros e armazenar em um vetor. após a leitura total dos 5 numeros, o codigo deve escrever
# esses 5 numeros lidos na ordem inversa.


numeros = [0, 0, 0, 0, 0]

for x in range(5):
    numeros[x] = int(input("digite um numero:"))

print(f"A ordem inversa dos numeros inseridos foi: {numeros[4]}, {numeros[3]}, {numeros[2]}, {numeros[1]}, {numeros[0]}.")