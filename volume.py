from math import pi

def volume_cubo(lado):
    return lado ** 3

def volume_paralelepipedo(comprimento, largura, altura):
    return comprimento * largura * altura

def volume_esfera(raio):
    return (4/3) * pi * (raio ** 3)

def main():
    print("Calculadora de Volume")
    print("1. Cubo")
    print("2. Paralelepípedo")
    print("3. Esfera")
    escolha = input("Escolha uma opção (1-3): ")

    if escolha == '1':
        lado = float(input("Digite o lado do cubo: "))
        print(f"Volume do cubo: {volume_cubo(lado):.2f}")
    elif escolha == '2':
        comprimento = float(input("Comprimento: "))
        largura = float(input("Largura: "))
        altura = float(input("Altura: "))
        print(f"Volume do paralelepípedo: {volume_paralelepipedo(comprimento, largura, altura):.2f}")
    elif escolha == '3':
        raio = float(input("Digite o raio da esfera: "))
        print(f"Volume da esfera: {volume_esfera(raio):.2f}")
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    main()