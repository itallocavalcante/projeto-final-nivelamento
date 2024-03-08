def soma(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        print("Não é possível dividir por zero.")
        return None

def potenciacao(num1, num2):
    return num1 ** num2

def fatorial(num1):
    contador = 0
    resultado = 1
    if num1 == 0:
        return 1
    else:
        while contador < num1:
            contador += 1
            resultado *= contador
        return resultado
    

print("CALCULADORA")

while True:
    print("1. soma")
    print("2. subtração")
    print("3. multiplicação")
    print("4. divisão")
    print("5. potenciação")
    print("6. fatorial" )
    print("7. sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 7:
        print("Saindo...")
        break

    if opcao < 1 or opcao > 7:
        print("Opção inválida. Tente novamente.")
        continue
    if opcao >= 1 and opcao <= 6:
        num1 = float(input("Digite um número: "))
    if opcao >= 1 and opcao <= 5:
        num2 = float(input("Digite outro número: "))

    if opcao == 1:
        print(f"O resultado é: {soma(num1, num2)}")
    elif opcao == 2:
        print(f"O resultado é: {subtracao(num1, num2)}")
    elif opcao == 3:
        print(f"O resultado é: {multiplicacao(num1, num2)}")
    elif opcao == 4:
        resultado = divisao(num1, num2)
        if resultado is not None:
            print(f"O resultado é: {resultado}")
    elif opcao == 5:
        print(f"O resultado é: {potenciacao(num1, num2)}")
    elif opcao == 6:
        resposta = fatorial(num1)
        print (f" o fatorial de {num1} é {resposta}")