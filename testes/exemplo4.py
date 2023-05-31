def verificar_numero(numero):
    if numero > 0:
        print("O número é positivo.")
    elif numero < 0:
        print("O número é negativo.")
    else:
        print("O número é zero.")

def verificar_paridade(numero):
    if numero % 2 == 0:
        print("O número é par.")
    else:
        print("O número é ímpar.")

def verificar_intervalo(numero):
    if numero < 0:
        print("O número está fora do intervalo permitido.")
    elif numero >= 0 and numero <= 10:
        print("O número está no intervalo de 0 a 10.")
    elif numero > 10 and numero <= 20:
        print("O número está no intervalo de 11 a 20.")
    else:
        print("O número está fora do intervalo permitido.")

def verificar_multiplo(numero):
    if numero % 3 == 0 and numero % 5 == 0:
        print("O número é múltiplo de 3 e 5.")
    elif numero % 3 == 0:
        print("O número é múltiplo de 3.")
    elif numero % 5 == 0:
        print("O número é múltiplo de 5.")
    else:
        print("O número não é múltiplo de 3 nem de 5.")

def verificar_codigo(numero):
    verificar_numero(numero)
    verificar_paridade(numero)
    verificar_intervalo(numero)
    verificar_multiplo(numero)

# Exemplo de uso:
numero = 15
verificar_codigo(numero)