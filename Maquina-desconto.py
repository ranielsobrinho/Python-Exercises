preco = float(input("Qual é o preço do produto? R$"))
desconto = int(input("Quantos porcentos de desconto você quer?"))
novo = preco - (preco * desconto /100)

print("O valor de R${:.2f} com desconto de {}% será de: {:.2f}".format(preco,desconto,novo))