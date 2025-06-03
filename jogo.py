
def imprimeTabela(tab: list):
    for linha in tab:
        for item in linha:
            print(f"{item}", end = "  ")
        print()  
    
def vezJogador(valorVez: int):
    if valorVez == 0:
        return 1
    else:
        return 0
    

def verifcarPosicaoLivre(table: list, indice: list, lance: int):
    if table[int(indice[0])][int(indice[1])] == 0:
        if lance == 0:
            table[int(indice[0])][int(indice[1])] = "x"
            return True
        else:
            table[int(indice[0])][int(indice[1])] = "o"
            return True
    else:
        return False
        
def verficarVencedor(tabela: list, vezDe: int):
    checagem = False
    encaixe = dict()
    encaixe = {
        0 : [tabela[0][0], tabela[0][1], tabela[0][2]],
        1 : [tabela[1][0], tabela[1][1], tabela[1][2]],
        2 : [tabela[2][0], tabela[2][1], tabela[2][2]],
        3 : [tabela[0][0], tabela[1][0], tabela[2][0]],
        4 : [tabela[0][1], tabela[1][1], tabela[2][1]],
        5 : [tabela[0][2], tabela[1][2], tabela[2][2]],
        6 : [tabela[0][0], tabela[1][1], tabela[2][2]],
        7 : [tabela[2][0], tabela[1][1], tabela[0][2]],
    }

    if vezDe == 0:
        for v,j in encaixe.items():
            if "x" in j and 0 not in j and "o" not in j:
                checagem = True
            else:
                pass
    else:
        for k,l in encaixe.items():
            if "o" in l and 0 not in l and "x" not in l:
                checagem = True
            else:
                pass
    return checagem 

tabela = list()

for i in range(3):
    lista = list()
    for j in range(3):
        lista.append(0)
    tabela.append(lista)

vezDoJogador = 0
fimJogo = 0
maxJogada = 8    
while(fimJogo <= maxJogada):
    imprimeTabela(tabela)
    posicaoJagada = input().split()
    
    if verifcarPosicaoLivre(tabela, posicaoJagada, vezDoJogador):
        if verficarVencedor(tabela, vezDoJogador):
            imprimeTabela(tabela)
            print(f"jogador {vezDoJogador} venceu!! Brabo.")
            break
        elif fimJogo == maxJogada:
            print("jogo ficou velho, empatou.")
            fimJogo = fimJogo + 1
        else:
            vezDoJogador = vezJogador(vezDoJogador)
            fimJogo = fimJogo + 1
    else:
        print("posicao ocupada, tente outra.")
 