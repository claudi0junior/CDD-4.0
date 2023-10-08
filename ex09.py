#altere o sistema anterior, e faça um sistema de login, pedindo a senha do usuario e mostrando seu nome e a mensagem,
#login efetuado com sucessso.


nome = [0, 0, 0, 0, 0]
senha = [0, 0, 0, 0, 0]
log_senha = 0
p = 0
v = 0

for x in range(5):
    nome[x] = input("digite seu nome:")

for y in range(5):
    senha[y] = int(input("Agora digite a sua senha:"))

for l in range(1):
    log_senha = int(input("insira sua senha:"))

for a in range(5):
    if log_senha == senha[p]:
        print(f"olá {nome[p]}")
        print("login efetuado com sucesso")
    p+=1

if p == 4:
    print("erro")