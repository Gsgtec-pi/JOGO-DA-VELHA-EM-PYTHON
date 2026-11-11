total_partidas, vitorias_X, vitorias_O, empates = 0, 0, 0, 0
seq_X, seq_O, max_seq_X, max_seq_O = 0, 0, 0, 0

tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]
executando = True

# Menu Principal controlado por while
while executando == True:
    print("\n=== JOGO DA VELHA ===")
    print("1. Jogar")
    print("2. Ver regras")
    print("3. Ver placar")
    print("4. Sair")

    opcao = input("Escolha uma opção (1 a 4): ")
