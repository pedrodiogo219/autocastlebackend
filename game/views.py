from django.shortcuts import render
from django.http import HttpResponse

from game import stockfish

# Create your views here.
def index(request):
    proccessGame()
    return HttpResponse("Teste")


def proccessGame():
    print(stockfish.get_parameters())
    # print(stockfish)
    stockfish.set_fen_position("r1bk3q/pp1p4/nbp3p1/4N3/3P1p2/6P1/PPP4P/R1B1R1K1 w - - 0 2")

    moves = []
    while True:
        print(stockfish.get_board_visual())

        move = stockfish.get_best_move()
        if not move:
            break

        moves.append(move)

        stockfish.make_moves_from_current_position([move])
    
    print(moves)
    return moves






