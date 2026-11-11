total_partidas, vitorias_X, vitorias_O, empates = 0, 0, 0, 0
seq_X, seq_O, max_seq_X, max_seq_O = 0, 0, 0, 0
tabuleiro = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
executando = True

while executando == True:
    print("\n=== JOGO DA VELHA ===")
    print("1. Jogar\n2. Ver regras\n3. Ver placar\n4. Sair")
    opcao = input("Escolha uma opção (1 a 4): ")

    if opcao == "1":
        # Limpar o tabuleiro com for aninhado
        for i in range(3):
            for j in range(3):
                tabuleiro[i][j] = " "

        turno = "X"
        jogo_ativo = True

        while jogo_ativo == True:
            # Exibição do tabuleiro com for aninhado
            print("\n  1 2 3")
            for i in range(3):
                linha_str = str(i + 1) + " "
                for j in range(3):
                    linha_str = linha_str + tabuleiro[i][j] + " "
                print(linha_str)
            print("\nVez do jogador", turno)
            jogo_ativo = False # (trava de segurança temporária pro loop)
