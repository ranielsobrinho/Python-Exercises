num = int(input("Digite um número para gerar a sua tabuada:"))

for numeros in range(1, 11):
    resultado = num * numeros
    print("-"*10)
    print("{} x {} = {}".format(num, numeros, resultado))
    print("-"*10)