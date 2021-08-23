from defs import Clear, Linha, Title1, Title2, fimdeJogo, Historico, hasNumbers, forca
from time import sleep

def JogoMain(nLetras, palavraChave, erros, letrasErradas):

    nLetras = int(len(palavraChave))
    print(f'A palavra escolhida possui {nLetras} letras\n')
    print(f'Erros: {erros}')
    print("Letras Erradas:", end = ' ')
    espacinhos(letrasErradas)
 
    espaco = '_'*len(palavraChave)
    for i in range(len(palavraChave)): 
        if palavraChave[i] in letrasAcertadas:
            espaco = espaco[:i] + palavraChave[i] + espaco[i+1:] 
    
    print(' ')
    espacinhos(espaco)
    print(' ')

def recebeChute(chutesFeitos):
    while True: 
        chute = input('Adivinhe alguma letra: ').upper()
        Linha()
        
        if len(chute) != 1: 
            print('Coloque uma unica letra')
        elif chute in chutesFeitos: 
            print('Voce ja digitou essa letra, digite de novo!')
        elif hasNumbers(chute) or chute in "!@#$%&*()_+=-[{]}´`¨~^;><.,/\|]'": 
            print('Digite apenas letras')
        else:
            return chute 

def verificaChute(chute):
    global letrasAcertadas, letrasErradas, erros, jogando
    global competidor, desafiante
    if chute in palavraChave:
        letrasAcertadas += chute

        if quemGanhou(palavraChave, letrasAcertadas):
            vencedor = 'Competidor - {}'.format(competidor)
            perdedor = 'Desafiante - {}'.format(desafiante)

            print('='*60)
            Linha()
            fimdeJogo(vencedor, perdedor, palavraChave)
            Historico(palavraChave, vencedor, perdedor)
            jogando = False
    
    else:
        erros = erros + 1
        letrasErradas = letrasErradas + chute 

        if erros == 6: 
            vencedor = 'Desafiante - {}'.format(desafiante)
            perdedor = 'Competidor - {}'.format(competidor)
            
            Clear()
            Title2()
            print(f'Erros: {erros}')
            forca(erros)
            print('='*60)
            Linha()
            fimdeJogo(vencedor, perdedor, palavraChave)
            Historico(palavraChave, vencedor, perdedor)
            jogando = False

def quemGanhou(palavraChave, letrasAcertadas):
    competidorWon = True

    for letra in palavraChave: 
        if letra not in letrasAcertadas:
            competidorWon = False
            break

    return competidorWon

def competidores():
    global competidor

    competidor = input(str('Nome do competidor: ')).strip()
    while True:
        while len(competidor) == 0:
            print("\n==Nome do competidor não pode ser deixado em branco!==")
            competidor = input(str('Nome do competidor: ')).strip()
        return competidor

def desafiantes():
    global desafiante

    desafiante = input(str('Nome do desafiante: ')).strip()
    while True:
        while len(desafiante) == 0:
            print("\n==Nome do desafiante não pode ser deixado em branco!==")
            desafiante = input(str('Nome do desafiante: ')).strip()
        return desafiante

def palavraDef():
    global palavraChave

    Clear() 
    Title1()
    palavraChave = input(str('Digite a palavra chave: ')).upper().strip()
    while True:
        while hasNumbers(palavraChave) or len(palavraChave) == 0 or palavraChave in "!@#$%&*()_+=-[{]}´`¨~^;><.,/\|]'":
                print("\nA palavra chave não pode ser um numero, nem caractere e não podeser deixada em branco\n")
                palavraChave = input(str('Digite a palavra chave: ')).upper()
        return palavraChave 

def dicasDef():
    global dicas
    Linha()

    for c in range(1, 4):
        dica = input(str(f'Digite a {c}ª dica: '))
        while True:
            if len(dica) == 0:
                print('\n==Não se pode deixar a dica em branco!==')
                dica = input(str(f'Digite a {c}ª dica: '))
            else: 
                dicas.append(dica)
                break
            
    Clear()
    Title2()
    return dicas

def dicasList():
    dicasTotais = int(len(dicas))
    while True:
        if dicasTotais == 3:
            print(f'A primeira dica é: {dicas[0]}\n')
            del(dicas[0])
            break

        elif dicasTotais == 2:
            print(f'A segunda dica é: {dicas[0]}\n')
            del(dicas[0])
            break

        elif dicasTotais == 1:
            print(f'A terceira e ultima dica é: {dicas[0]}\n')
            del(dicas[0])
            break

        else:
            print('Não restam mais dicas disponíveis!\n')
            break

def JogarNovamente():
    global escolha

    print('Jogar novamente?\n[ 1 ] sim\n[ 2 ] não\n')
    escolha = input('Sua opção: ')
    return escolha
   
def espacinhos(palavraChave):
    for c in palavraChave:
        print(c, end = ' ')
 
    print()

def main():
    global jogando, palavraChave, erros, letrasErradas, letrasAcertadas, dicas
    palavraChave = letrasErradas = letrasAcertadas = vencedor = perdedor = chutesFeitos = ''
    dicas = []
    erros = nLetras = 0
    jogando = True

    Clear()
    Title1()
    desafiantes()
    competidores()

    Clear()
    Title1()
    palavraDef()
    dicasDef()

    while jogando:
        try:
            Clear()
            Title2()
            JogoMain(nLetras, palavraChave, erros, letrasErradas)
            forca(erros)
            
            while len(dicas) > 0:
                print('\nOpções disponíveis:\n[ 1 ] Jogar\n[ 2 ] Dica')
                opcao = int(input('Sua escolha: '))
                Linha()
                break
            else:
                print('\nOpções disponíveis:\n[ 1 ] Jogar')
                opcao = int(input('Sua escolha: '))
                
        
 
            if opcao == 1:
                Clear()
                Title2()
                JogoMain(nLetras, palavraChave, erros, letrasErradas)
                forca(erros)
                chute = recebeChute(letrasErradas + letrasAcertadas)
                verificaChute(chute)

            elif opcao == 2:
                dicasList()

                chute = recebeChute(letrasErradas + letrasAcertadas)
                verificaChute(chute)

            else:
                print('\nOpção Inválida, digite a opção correta!')
                sleep(2)

            if not jogando:
                JogarNovamente()
                if escolha == '1':
                    letrasErradas = ''
                    letrasAcertadas = ''
                    palavraChave = ''
                    jogando = True
                    erros = 0
                    main()
                else:
                    print('Obrigada por Jogar!')
        except ValueError:
            print('\nDigite uma opção válida!')
            sleep(2)
         
main()