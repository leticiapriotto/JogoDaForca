from os import system

def Clear():
    system('cls')

def Linha():
    print('')

def Title1():
    print('='*60)
    print('Bem-vindo ao Jogo da Forca'.center(60))
    print('='*60)

def Title2():
    print('='*60)
    print('Jogo da Forca'.center(60))
    print('='*60)

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

def Historico(palavraChave, vencedor, perdedor):
    arquivo = open("historico", "a")
    arquivo.write(f"Palavra escolhida: {palavraChave} | ")
    arquivo.write(f"Vencedor: {vencedor} | Perdedor: {perdedor}\n")
    arquivo.close()
    return palavraChave
    return vencedor
    return perdedor

def fimdeJogo(vencedor, perdedor, palavraChave):
    print('Fim de Jogo!'.center(60))
    Linha()
    print(f'Vencedor: {vencedor}'.center(60))
    print(f'Perdedor: {perdedor}'.center(60))
    print(f'Palavra Chave: {palavraChave}'.center(60))
    Linha()
    print('='*60)
    return vencedor
    return perdedor
    return palavraChave

def forca(erros):
    if erros == 0:
        print()
        print("|----- ")
        print("|    | ")
        print("|      ")
        print("|      ")
        print("|      ")
        print("|      ")
        print("_      ")
        print()

    elif erros == 1:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|      ")
        print("|      ")
        print("|      ")
        print("_      ")
        print()

    elif erros == 2:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|    |  ")
        print("|      ")
        print("|      ")
        print("_      ")
        print()
    elif erros == 3:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|   /| ")
        print("|      ")
        print("|      ")
        print("_      ")

    elif erros == 4:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|   /|\ ")
        print("|      ")
        print("|      ")
        print("_      ")

    elif erros == 5:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|   /|\ ")
        print("|    | ")
        print("|   /  ")
        print("_      ")
        print()
    elif erros == 6:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|   /|\ ")
        print("|    | ")
        print("|   / \ ")
        print("_      ")
        print()