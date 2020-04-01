#estudando estrutura de repetição
while True:
    operador = input("Digite '+','-','*' ou '/' para fazer a operação matemática:")
    if operador == 'q' or operador == 'Q':
        break
    elif operador == '+' or operador == '-' or operador == '*' or operador == '/':
        valor1 = float(input("Digite o primeiro valor :"))
        valor2 = float(input("Digite o segundo valor: "))
    else:
        print("Operador não válido, por favor tente novamente.")
    #  -- soma --
    if operador == "+":
        resultado = valor1 + valor2
        print(resultado)
    #  -- subtração --
    elif operador == "-":
        resultado = valor1 - valor2
        print(resultado)
    #  -- multiplicação --
    elif operador == "*":
        resultado = valor1 * valor2
        print(resultado)
    #  -- divisão --
    elif operador == "/":
        resultado = valor1 / valor2
        print(resultado)

