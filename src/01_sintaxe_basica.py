a = 10
b = 5

adicao_1 = a + b
subtracao_1 = a - b
multiplicacao_1 = a - b
divisao_1 = a / b
resto_1 = a % b

resultado_1 = ('Adição -> {adicao};\nSubtração -> {sub};\nMultiplicação -> {multi};\nDivisão -> {div};\nResto -> {resto}').format(adicao=adicao_1, sub=subtracao_1, multi=multiplicacao_1, div=divisao_1, resto=resto_1)

print(resultado_1)


print("- - - - - - - - - - - - - -")


# Recebendo os valores a partir do input do usuário via terminal
# Os dados inputados são originalmente do tipo String e por conta disso precisam ser convertidos para inteiro.
# Os métodos int(), input(), format() dentre tantos outros são métodos nativos do Python chamados de built in.
input_A = int(input("Informe o valor de A: "))
input_B = int(input("Informe o valor de B: "))

adicao_2 = input_A + input_B
subtracao_2 = input_A - input_B
multiplicacao_2 = input_A * input_B
divisao_2 = input_A / input_B
resto_2 = input_A % input_B

resultado_2 = ('Adição -> {adicao};\nSubtração -> {sub};\nMultiplicação -> {multi};\nDivisão -> {div};\nResto -> {resto}').format(adicao=adicao_2, sub=subtracao_2, multi=multiplicacao_2, div=divisao_2, resto=resto_2)

print(resultado_2)