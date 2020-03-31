#média aritmética
nota_1 = float(input("Digite a nota parcial"))
nota_2 = float(input("Digite a nota bimestral"))
soma = nota_1 + nota_2
media = soma/2
if media > 6:
    print("Você está aprovado.Sua nota é",media)
else:
    print("Você está reprovado.Sua nota é",media)