

print("Come on tu see how much money you have")

ColombianPesos = int(input("Enter your Colombian Pesos: "))
PeruvianSoles = int(input("Enter your Peruvian Soles: "))
BrazilianReais = int(input("Enter your Brazilian Reais: "))

ColombianDollars = ColombianPesos / 4169
PeruvianDollars = PeruvianSoles / 3.66
BrazilianDollars = BrazilianReais / 5.65

print(f"You have {ColombianDollars} dollars in Colombian Pesos")
print(f"You have {PeruvianDollars} dollars in Peruvian Soles")
print(f"You have {BrazilianDollars} dollars in Brazilian Reais")

totalDollars = ColombianDollars + PeruvianDollars + BrazilianDollars
print(f"You have {totalDollars} dollars in total")