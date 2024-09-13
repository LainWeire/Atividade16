# Crie um programa que receba o peso e a altura de uma pessoa e calcule o Índice de Massa Corporal (IMC). O programa deve classificar o IMC da pessoa de acordo com a tabela a seguir:
# Abaixo do peso: IMC < 18.5
# Peso normal: 18.5 ≤ IMC < 25
# Sobrepeso: 25 ≤ IMC < 30
# Obesidade: IMC ≥ 30

p = float(input("Seu peso: "))
a = float(input("Sua altura: "))

imc = (p / (a*a))

if imc <18.5:
    print (f"Seu IMC é:{imc}, seu peso está abaixo do ideal.")

elif (imc > 18.5) and (imc < 25):
    print (f"Seu IMC é {imc}, está no peso ideal.")

elif (imc > 25) and (imc < 30):
    print (f"Seu IMC é {imc}, o que caracteriza sobrepeso.")

elif (imc > 30):
    print (f"Seu IMC é {imc}, o que caracteriza obesidade.")