altura = float(input("Altura da parede :"))
largura = float(input("Largura da parede :"))
area = altura * largura
pintura = area / 2

print("Altura da parede é {:.1f}m, largura da parede é {:.1f}m, sua área é de {:.1f}m²."
      "Para pintar uma parede com essa área você precisará de {:.1f}L de tinta".format(altura,
        largura,area,pintura))