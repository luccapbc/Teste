# Exercício soma 2 números

while True:
    try:
        numero1 = int(input("Digite um número: "))
        break
    except ValueError:
        print("Valor inválido. Por favor, digite um número inteiro.")

while True:
    try:
        numero2 = int(input("Digite outro número: "))
        soma = numero1 + numero2
        print("A soma de", numero1, "e", numero2, "é:", soma)
        break
    except ValueError:
        print("Valor inválido. Por favor, digite um número inteiro.")


