import random
import time


n = 20
d = 0.05
wait = 1
empty = " "
full = "█"

def print_board(board):
    print(2*(n + 1)*"—")
    for row in board:
        print("|", end="")
        for cell in row:
            print(2*cell, end="")
        print("|")
    print(2*(n + 1)*"—")

def next_board(board):
    new_board = [[empty for j in range(n)] for i in range(n)]
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            neighbours = [
                board[i + di][j + dj]
                if (i + di in range(n)
                    and j + dj in range(n))
                else empty
                for di in (-1, 0, 1)
                for dj in (-1, 0, 1)
                if not (di, dj) == (0, 0)
            ]

            alive_neighbours = neighbours.count(full)

            if cell == empty:
                if alive_neighbours > 2:
                    new_board[i][j] = full
            else:
                if alive_neighbours in (2, 3):
                    new_board[i][j] = full
    return new_board
        
        
board = [random.choices([empty, full], weights=[1 - d, d], k=n) for i in range(n)]
        
while True:
    print_board(board)
    time.sleep(wait)

    print(40*"\n")
    board = next_board(board)

    
