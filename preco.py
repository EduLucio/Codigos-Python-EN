def calcular_preco_total():
    try:
        preco_unitario = float(input("Digite o preço unitário do produto: R$ "))
        quantidade = int(input("Digite a quantidade desejada: "))
        preco_total = preco_unitario * quantidade
        print(f"Preço total: R$ {preco_total:.2f}")
    except ValueError:
        print("Por favor, insira valores válidos.")

if __name__ == "__main__":
    calcular_preco_total()