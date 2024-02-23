"""
Autor: Leandro Henry Alves Ribeiro Vieira Magalhães

Componente Curricular: EXA 854-MI-Algoritmos

Concluido em: 06/10/2023

Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
"""

from random import randint, choice


def gerar_tabuleiro():
    matriz = [[0 for _ in range(4)] for _ in range(4)]
    posicao1 = (randint(0, 3), randint(0, 3))
    posicao2 = (randint(0, 3), randint(0, 3))

    while posicao1 == posicao2:
        posicao2 = (randint(0, 3), randint(0, 3))

    matriz[posicao1[0]][posicao1[1]] = 2
    matriz[posicao2[0]][posicao2[1]] = 2

    return matriz


def gerar_aleatorio(matriz):
    len_lin = len(matriz)
    len_col = len(matriz[0])
    zeros_posi = []
    for linha in range(len_lin):
        for coluna in range(len_col):
            if matriz[linha][coluna] == 0:
                zeros_posi.append((linha, coluna))
    zero_sorteado = choice(zeros_posi)
    substitutos = (2, 2, 4)
    substituto = choice(substitutos)
    matriz[zero_sorteado[0]][zero_sorteado[1]] = substituto
    return matriz


def receber_jogada():
    validas = ["a", "s", "d", "w"]
    while True:
        jogada = input("\n  W\nA S D: ")
        if jogada.lower() in validas:
            return jogada.lower()
        else:
            print(f'\n"{jogada}" não é uma jogada válida. ')


def verificar_vitoria(tabuleiro):
    for linha in tabuleiro:
        for numero in linha:
            if numero == 2048:
                return True
    return False


def verificar_derrota(tabuleiro):
    for linha in tabuleiro:
        if 0 in linha:
            return False

    for i in range(4):
        for j in range(3):
            if (
                tabuleiro[i][j] == tabuleiro[i][j + 1]
                or tabuleiro[j][i] == tabuleiro[j + 1][i]
            ):
                return False

    return True


def mover_zeros(linha, direcao):
    zeros = []
    outros = []

    for numero in linha:
        if numero == 0:
            zeros.append(numero)
        else:
            outros.append(numero)

    if direcao == "d":
        return outros + zeros
    elif direcao == "a":
        return zeros + outros


def transpor_matriz(matriz):
    len_lin = len(matriz)
    len_col = len(matriz[0])
    matriz_transposta = []

    for linha in range(len_col):
        nova_linha = []
        for coluna in range(len_lin):
            nova_linha.append(None)
        matriz_transposta.append(nova_linha)

    for linha in range(len_lin):
        for coluna in range(len_col):
            matriz_transposta[coluna][linha] = matriz[linha][coluna]

    return matriz_transposta


def limpar_matriz_transposta(matriz_transposta):
    for linha in matriz_transposta:
        for coluna in range(len(linha)):
            linha[coluna] = 0


def somar_tabuleiro(tabuleiro, direcao, matriz_transposta):
    aux = []
    score = 0
    if direcao == "d":
        for linha in tabuleiro:
            linha = mover_zeros(linha, "a")
            tam_linha = len(linha)
            i = tam_linha - 1
            while i >= 1:
                atual = linha[i]
                prox = linha[i - 1]
                if atual == prox:
                    linha[i] = 0
                    linha[i - 1] = atual + prox
                    score += atual + prox
                i -= 1
            linha = mover_zeros(linha, "a")
            aux.append(linha)
        limpar_matriz_transposta(matriz_transposta)
    elif direcao == "a":
        for linha in tabuleiro:
            linha = mover_zeros(linha, "d")
            tam_linha = len(linha)
            i = 0
            while i < tam_linha - 1:
                atual = linha[i]
                prox = linha[i + 1]
                if atual == prox:
                    linha[i] = 0
                    linha[i + 1] = atual + prox
                    score += atual + prox
                i += 1
            linha = mover_zeros(linha, "d")
            aux.append(linha)
        limpar_matriz_transposta(matriz_transposta)
    elif direcao == "s":
        tabuleiro = transpor_matriz(tabuleiro)
        for linha in tabuleiro:
            linha = mover_zeros(linha, "a")
            tam_linha = len(linha)
            i = tam_linha - 1
            while i >= 1:
                atual = linha[i]
                prox = linha[i - 1]
                if atual == prox:
                    linha[i] = 0
                    linha[i - 1] = atual + prox
                    score += atual + prox
                i -= 1
            linha = mover_zeros(linha, "a")
            aux.append(linha)
        aux = transpor_matriz(aux)
        limpar_matriz_transposta(matriz_transposta)
    elif direcao == "w":
        tabuleiro = transpor_matriz(tabuleiro)
        for linha in tabuleiro:
            linha = mover_zeros(linha, "d")
            tam_linha = len(linha)
            i = 0
            while i < tam_linha - 1:
                atual = linha[i]
                prox = linha[i + 1]
                if atual == prox:
                    linha[i] = 0
                    linha[i + 1] = atual + prox
                    score += atual + prox
                i += 1
            linha = mover_zeros(linha, "d")
            aux.append(linha)
        aux = transpor_matriz(aux)
        limpar_matriz_transposta(matriz_transposta)

    return aux, score


def movimentar_tabuleiro(tabuleiro, direcao):
    aux = []
    if direcao == "d":
        for linha in tabuleiro:
            nova_linha = mover_zeros(linha, "a")
            aux.append(nova_linha)
    elif direcao == "a":
        for linha in tabuleiro:
            nova_linha = mover_zeros(linha, "d")
            aux.append(nova_linha)
    elif direcao == "s":
        tabuleiro = transpor_matriz(tabuleiro)
        for linha in tabuleiro:
            nova_linha = mover_zeros(linha, "a")
            aux.append(nova_linha)
        aux = transpor_matriz(aux)
    elif direcao == "w":
        tabuleiro = transpor_matriz(tabuleiro)
        for linha in tabuleiro:
            nova_linha = mover_zeros(linha, "d")
            aux.append(nova_linha)
        aux = transpor_matriz(aux)

    return aux


def maior_numero(matriz):
    maior = 0
    for linha in matriz:
        for coluna in linha:
            if coluna > maior:
                maior = coluna
    return maior


def montar_tabuleiro(matriz):
    tam_linha = len(matriz)
    tam_coluna = len(matriz[0])

    m_num = maior_numero(matriz)
    espaço = len(str(m_num)) + 2

    print("-" * ((tam_coluna * espaço) + tam_coluna + 1))

    for linha in range(tam_linha):
        for coluna in range(tam_coluna):
            if matriz[linha][coluna] != 0:
                elemento = f"|{matriz[linha][coluna]:^{espaço}}"
            else:
                elemento = f"|{' ':^{espaço}}"
            print(elemento, end="")

        print("|")

    print("-" * ((tam_coluna * espaço) + tam_coluna + 1))


def main():
    historico = []
    ficar_menu = True
    while ficar_menu:
        jogadas = 0
        opcao = input(
            "\n[ 0 ] - Tutorial do jogo 2048\n[ 1 ] - Começar uma nova partida\n[ 2 ] - Exibir Histórico de partidas\n[ 3 ] - Sair do jogo:\nEscolha uma opção: "
        )
        if opcao == "0":
            print(
                """

Objetivo do Jogo:
    O objetivo principal do jogo "2048" é combinar peças com números iguais para criar uma peça com o número 2048.

Como Jogar:

Tabuleiro Inicial: O jogo é jogado em um tabuleiro 4x4, onde você verá várias peças com números. Inicialmente, duas peças com o número 2 são colocadas aleatoriamente no tabuleiro.

Movimentação: Você pode mover as peças na direção desejada, escolhendo entre as quatro direções: cima (W), baixo (S), esquerda (A) e direita (D). Use as teclas correspondentes no seu teclado para fazer os movimentos.

Combinação: Quando duas peças com o mesmo número se movem para uma direção e colidem, elas se combinam em uma única peça com a soma dos seus valores. Por exemplo, se duas peças com o número 2 colidirem, elas se combinarão em uma única peça com o número 4.

Geração de Novas Peças: Após cada movimento, uma nova peça com o número 2 ou 4 é gerada aleatoriamente em uma posição vazia no tabuleiro.

Pontuação: Você ganha pontos toda vez que combina peças. A pontuação é a soma dos valores das peças combinadas.

Vitória: Você vence o jogo quando consegue criar uma peça com o número 2048 no tabuleiro. No entanto, você pode continuar jogando para obter uma pontuação mais alta.

Derrota: O jogo termina quando o tabuleiro está cheio e não é possível fazer mais movimentos válidos, ou seja, quando não há espaços vazios e nenhum movimento possível para combinar peças. Nesse momento, o jogo está encerrado e sua pontuação final é registrada.

Continuação: Depois de ganhar ou perder, você pode escolher continuar jogando ou iniciar um novo jogo.        
        
        """
            )

        elif opcao == "1":
            tabuleiro = gerar_tabuleiro()
            pontuacao = 0
            montar_tabuleiro(tabuleiro)
            jogando = True
            while jogando:
                print(f"Jogada: {jogadas + 1}")
                print(f"Score: [{pontuacao}]")
                jogada = receber_jogada()
                # jogada = choice(["a", "s", "d", "w"])
                tabuleiro = movimentar_tabuleiro(tabuleiro, jogada)
                matriz_transposta = []
                somado = somar_tabuleiro(tabuleiro, jogada, matriz_transposta)
                tabuleiro = somado[0]
                pontuacao += somado[1]
                jogadas += 1
                if verificar_derrota(tabuleiro):
                    print("\nVocê perdeu! Game Over!")
                    historico.append((jogadas, pontuacao))
                    jogando = False
                elif verificar_vitoria(tabuleiro):
                    montar_tabuleiro(tabuleiro)
                    print(
                        f"Você venceu! Parabéns! Sua pontuação foi {pontuacao} em {jogadas} jogadas!!!"
                    )
                    historico.append((jogadas, pontuacao))
                    jogando = False
                else:
                    zeros = 0
                    for linha in tabuleiro:
                        for coluna in linha:
                            if coluna == 0:
                                zeros += 1
                    if zeros > 0:
                        tabuleiro = gerar_aleatorio(tabuleiro)
                        montar_tabuleiro(tabuleiro)
                    else:
                        if verificar_derrota(tabuleiro):
                            print("\nVocê perdeu! Game Over!")
                            historico.append((jogadas, pontuacao))
                            jogando = False
        elif opcao == "2":
            if len(historico) == 0:
                print("\nNão houve jogadas a serem registradas!\n")
            else:
                print(f"Histórico de partidas recentes:")
                for partida in historico:
                    jogadas_partida, pontuacao_partida = partida
                    print(f"Jogadas: {jogadas_partida} -- Pontuação: {pontuacao_partida}")
        elif opcao == "3":
            print("\nJogo Finalizado! Até a próxima!\n")
            ficar_menu = False
        else:
            print("\nEntrada inválida, tente novamente!\n")


main()