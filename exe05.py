def calculadora(a, b, operacao):
    if operacao == 'soma':
        result = a + b
    elif operacao == 'subtracao':
        result = a - b
    elif operacao == 'multiplicacao':
        result = a * b            
    else:
        result = a / b
    return result

print(calculadora(10, 5, 'soma'))
print(calculadora(10, 5, 'subtracao'))
print(calculadora(10, 5, 'multiplicacao'))
print(f"{calculadora(10, 5, 'divisao'):.0f}")