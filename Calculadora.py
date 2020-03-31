valor1 = float(input("Digite o primeiro valor:"))
operador = input("Digite o operador matemático:")
valor2 = float(input("Digite o segundo valor:"))
#  -- soma --
if operador == "+":
    resultado = valor1 + valor2
#  -- subtração --
elif operador == "-":
    resultado = valor1 - valor2
#  -- multiplicação --
elif operador == "*":
    resultado = valor1 * valor2
#  -- divisão --
elif operador == "/":
    resultado = valor1 / valor2
else:
    resultado = "Operador não reconhecido"


print(resultado)


