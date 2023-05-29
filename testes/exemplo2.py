print("Calculadora de fatorial")
numero = int(input("Digite um número inteiro não negativo: "))

if numero < 0:
    print("Erro: o número deve ser não negativo.")
else:
    fatorial = 1
    while numero > 0:
        print(fatorial)
        fatorial *= numero
        numero -= 1

    print(f"O fatorial é {fatorial}.")
