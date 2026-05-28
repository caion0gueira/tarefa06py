def contar_vogais(texto):
    vogais = 'aeiouAEIOU'
    contador = 0
    for letra in texto:
        if letra in vogais:
            contador += 1
    return contador
print(contar_vogais("Caio Nogueira Oliveira"))

#OUTRA FORMA DE FAZER A MESMA COISA

def contar_vogais(texto):
    contador = 0
    for letra in texto:
        if letra.upper() in 'AEIOU':
            contador += 1
    return contador
print(contar_vogais("Fabiana Nogueira Oliveira"))