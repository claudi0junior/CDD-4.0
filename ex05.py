# ler um vetor A de 10 numeros. logo em seguida, ler mais um numero e guardar em uma variavel x.
# armazenar em um vetor M o resultado pelo valor x. imprimir o vetor M.


a = [0] * 10
for y in range(10):
    a[y] = int(input("insira um numero:"))

x = [0]
for z in range(1):
    x[z] = int(input("insirir o numero multiplicador:"))

m = [0] * 10
for y in range(10):
    m[y] = a[y] * x[z]
    a[y] = a[y] + a[y]

print(f"o resultado dos numeros inseridos multiplicados por {x}, é {m}")
