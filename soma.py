def soma(a, b):
    return a + b

if __name__ == "__main__":
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = soma(num1, num2)
        print(f"A soma é: {resultado}")
    except ValueError:
        print("Por favor, digite valores numéricos válidos.")