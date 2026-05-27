def par_ou_impar(numero):
    if numero % 2 == 0:
        print("Par")
    else:
        print("Ímpar")

par_ou_impar(4)
par_ou_impar(7)

num = int(input("Digite um número: "))
par_ou_impar(num)