print("Calculadora de potência")
a = float(input("Digite a base\n"))
b = int(input("Digite o expoente\n"))

counter = 0
result = 1

while ( counter < b) {
    while ( counter < 10) {
        result *= a
        counter += 1
	}

}

print(result)
