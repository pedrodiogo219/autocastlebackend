from django.shortcuts import render
from django.http import HttpResponse

from game import stockfish

# Create your views here.
def index(request):
    proccessGame()
    return HttpResponse("Teste")




def proccessGame():
    # print(stockfish.get_parameters())
    # print(stockfish)
    stockfish.set_fen_position("rnbqkbnr/pppp1ppp/4p3/8/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 0 2")

    while True:
        print(stockfish.get_board_visual())

        move = stockfish.get_best_move()
        print(move)

        stockfish.make_moves_from_current_position([move])






