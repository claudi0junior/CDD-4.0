#faça um codigo para ler um N qualquer (que será o tamanho dos vetores). após, ler dois vetores a e b (de tamanho n cada um)
#e depois armazenar em  um terceiro vetor a soma dos elementos do vetor A com do vetor B (respeitando as mesmas posições)
#e escrever o vetor soma.


qtd = int(input("insira um numero que será o tamanho dos vetores:"))
a = [0] * qtd
b = [0] * qtd
n = [0] * qtd
c = 0

for x in range(qtd):
    a[x] = int(input("insira um numero:"))
    x+=1

for y in range(qtd):
    b[y] = int(input("insira um numero:"))
    y+=1

for s in range(qtd):
    n[s] = a[c] + b[c]
    c+=1

print(n)
