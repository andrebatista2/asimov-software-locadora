import os

def mostrar_lista_carros(lista_carros):
    for i, car in enumerate(lista_carros):
        print("[{}] {} - R$ {}/dia".format(i, car[0], car[1]))


carros = [
    ("Tracker", 120),
    ("Kwid", 50),
    ("Uno", 60),
    ("Nivus", 120),
    ("Tesla", 12000),
    ("Polo", 80)
]
alugados = []

while True:
    os.system("cls")

    print("=============================================")
    print("      Bem vindo a Locadora de Carros         ")
    print("=============================================")

    print("O que deseja fazer?")
    print("0 - Mostrar portfólio | 1 - Alugar Carro | 2 - Devolver um Carro \n")
    op = int(input())

    os.system("cls")
    if op == 0:
        mostrar_lista_carros(carros)
    elif op == 1:
        mostrar_lista_carros(carros)
        print("====================")
        print("Escolha o código do carro: ")
        cod_car = int(input())
        print("Por quantos dias deseja alugar este carro? ")
        qtd_dias = int(input())
        os.system("cls")

        print("Você escolheu {} por {} dias".format(carros[cod_car][0], qtd_dias))
        print("Valor da transação: R$ {}. Deseja alugar?".format(carros[cod_car][1] * qtd_dias))

        print("0 - SIM | 1 - NÃO")
        conf = int(input())
        if conf == 0:
            print("Parabéns. Você alugou o carro {} por {} dias".format(carros[cod_car][0], qtd_dias))
            alugados.append(carros.pop(cod_car))

    else:
        if len(alugados) == 0:
            print("Não há carros para devolver")
        else:
            print("Segue a lista de carros alugados:")
            mostrar_lista_carros(alugados)
            print("")
            print("Escolha o carro que deseja devolver")
            cod = int(input())
            if conf == 0:
                print("Obrigado por devolver o carro {}".format(alugados[cod][0]))
                carros.append(alugados.pop(cod))
            else:
                os.system("cls")

    print("\nQuer continuar?")
    print("0 - Continuar | 1 - Sair")
    if int(input()) == 1:
        break