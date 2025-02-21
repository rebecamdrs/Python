#Header/Cabeçalho
print("======== OPERAÇOES MATEMÁTICAS ========")
print("Soma, subtração, multiplicação e divisão.")

#Entradas
numero1 = float(input("> Digite o primeiro número: "))
numero2 = float(input("> Digite o segundo número: "))

print("============= RESULTADOS =============")

#Operações
soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2

#Saída
print(f'Soma: {soma:.2f}')
print(f'Subtração: {subtracao:.2f}')
print(f'Multiplicação: {multiplicacao:.2f}')
print(f'Divisão: {divisao:.2f}')

