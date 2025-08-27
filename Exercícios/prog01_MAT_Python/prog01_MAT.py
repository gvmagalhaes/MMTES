num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
print("[1] SOMA")
print("[2] SUBTRAÇÃO")
print("[3] MULTIPLICAÇÃO")
print("[4] DIVISÃO")
escolha = int(input("Escolha o que você deseja fazer com esses números:"))


match escolha:
    case 1:
        resultado = num1 + num2
        print(f"A soma entre {num1} e {num2} é {resultado}. ")
    case 2:
        resultado = num1 - num2
        print(f"A subtração entre {num1} e {num2} é {resultado}. ")
    case 3:
        resultado = num1 * num2
        print(f"A multiplicação entre {num1} e {num2} é {resultado}. ")
    case 4: 
        resultado = num1/num2
        print(f"A divisão entre {num1} e {num2} é {resultado}. ")


