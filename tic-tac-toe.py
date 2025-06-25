import random 

def main():
    board = {
        "A1": "_", "A2": "_", "A3": "_",
        "B1": "_", "B2": "_", "B3": "_",
        "C1": "_", "C2": "_", "C3": "_",
    }
    
    while True:
        player = str(input())
        computer = random.choice(board)
        board[player] = "x"
        board[computer] = "o"
        graphics(board)
        winner = check_winner(board)
        if winner:
            print(f"{winner} wins!")
        else:
            print("no winner")
        
 
def graphics(board):
    print("   1  2  3")
    print(f" A |{board['A1']}|{board['A2']}|{board['A3']}|")
    print(f" B |{board['B1']}|{board['B2']}|{board['B3']}|")
    print(f" C |{board['C1']}|{board['C2']}|{board['C3']}|") 
    return board

def check_winner(board):
    win_combos = [
        ["A1", "A2", "A3"],  # top row
        ["B1", "B2", "B3"],  # middle row
        ["C1", "C2", "C3"],  # bottom row
        ["A1", "B1", "C1"],  # left column
        ["A2", "B2", "C2"],  # middle column
        ["A3", "B3", "C3"],  # right column
        ["A1", "B2", "C3"],  # diagonal
        ["A3", "B2", "C1"],  # diagonal
    ]
    for combo in win_combos:
        values = [board[pos] for pos in combo]
        if values[0] != "_" and all(v == values[0] for v in values):
            return values[0]
    return None


if __name__ == "__main__":
    main()