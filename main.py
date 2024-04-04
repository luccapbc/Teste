# Exercício soma 2 números

while True:
    try:
        peso = float(input("Digite seue peso: "))
        break
    except ValueError:
        print("Valor inválido. Por favor, digite um número inteiro.")

while True:
    try:
        altura = float(input("Digite sua altura: "))
        imc = peso / (altura ** 2)
        print(" o seu imc e de", imc)
        break
    except ValueError:
        print("Valor inválido. Por favor, digite um número inteiro.")


