real = float(input("Quantos reais você tem? R$"))
dolar = real/5.20
euro = real/5.71
libra = real/6.46
bitcoin = real/33.533

print("Com {:.2f} reais você pode comprar {:.2f} de dólar, {:.2f} de euro, {:.2f} de libra esterlina e"
      " {:.2f} de bitcoin.".format(real, dolar, euro, libra, bitcoin))