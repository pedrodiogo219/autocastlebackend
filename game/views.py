from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from game import stockfish


class gameView(APIView):
    queryset = User.objects.none() 
    def get(self, request):
        # position = "8/5k1P/8/5K2/8/B7/8/4R1R1 w - - 0 1"
        # position = "1k6/7P/1K6/8/8/8/8/8 w - - 0 1"
        # position = "r1bk3q/pp1p4/nbp3p1/4N3/3P1p2/6P1/PPP4P/R1B1R1K1 w - - 0 2"
        position = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
        states = proccessGame(position)
        return Response({'states': states, 'position': position})    

# # Create your views here.
# def index(request):
#     moves = proccessGame()
#     return HttpResponse('{"content":"Teste"}')


def proccessGame(position):
    stockfish.set_fen_position(position)
    
    print(stockfish.get_parameters())
    # print(stockfish)
    # print(stockfish.get_board_visual())

    states = [position]
    while True:
        move = stockfish.get_best_move()
        if not move:
            break
        stockfish.make_moves_from_current_position([move])
        states.append(stockfish.get_fen_position())
    
    return states






