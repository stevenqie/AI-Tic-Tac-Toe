
from enum import Enum
import random

class GridSquare():
    state = ""
    pos = 0

    def __init__(self, x):
        self.pos = x
        self.state = "-1"
    
    def draw_space(self):
        if self.state == "1":
            return 'X'
        if self.state == "0":
            return 'O'
        return str(self.pos)[0]



class TicTacToe():
    cols = 3
    rows = 3
    total_turns = 0
    winner = -1

    class game_state(Enum):
        OVER =0
        RUNNING = 1
    
    current_state = game_state.OVER
    
    def setup(self):
        self.board = [[None] * self.cols for _ in range(self.rows)]
        counter = 1
        r = 0
        while r < TicTacToe.rows:
            c = 0
            while c < TicTacToe.cols:
                self.board[r][c] = GridSquare(counter)
                counter += 1
                c += 1
            r += 1
        TicTacToe.current_state = TicTacToe.game_state.RUNNING
        self.play_game()

    def play_game(self):
        while TicTacToe.current_state == TicTacToe.game_state.RUNNING:
            self.display_board()
            self.make_move()
            if self.isGameOver("1"):
                TicTacToe.current_state = TicTacToe.game_state.OVER
                self.winner = 1
                break
            if self.isGameOver("0"):
                TicTacToe.current_state = TicTacToe.game_state.OVER
                self.winner = 0
                break
            if self.total_turns == 9:
                TicTacToe.current_state = TicTacToe.game_state.OVER
                break
        self.display_board()
        self.display_game_over()

    
    def display_board(self):
        print("___________")
        print('\n ' + str(self.board[0][0].draw_space()) + " | " + str(self.board[0][1].draw_space()) + " | " + str(self.board[0][2].draw_space()))
        print("___|___|___")
        print('\n ' + str(self.board[1][0].draw_space()) + " | " + str(self.board[1][1].draw_space()) + " | " + str(self.board[1][2].draw_space()))
        print("___|___|___")
        print('\n ' + str(self.board[2][0].draw_space()) + " | " + str(self.board[2][1].draw_space()) + " | " + str(self.board[2][2].draw_space()))
        print("___|___|___")

    def valid_spot(self, position):
        for r in range(TicTacToe.rows):
            for c in range(TicTacToe.cols):
                if self.board[r][c].pos == position:
                    if self.board[r][c].state == "-1":
                        return True
        return False
                    

    def make_move(self):
        turn = "player 0" if TicTacToe.total_turns % 2 == 0 else "player 1"
        TicTacToe.total_turns += 1

        if turn == "player 0":
            placement = int(input("Player 0, select a position: "))
            while(placement < 1 or placement > 9 or self.valid_spot(placement) is False):
                placement = int(input("Invalid Position. Select again: "))

            for r in range(TicTacToe.rows):
                for c in range(TicTacToe.cols):
                    if self.board[r][c].pos == placement:
                        self.board[r][c].state = '0'
        else:
            aiturn = random.randint(1, 9)
            while(aiturn < 1 or aiturn > 9 or self.valid_spot(aiturn) is False):
                aiturn = random.randint(1, 9)
            print("Computer selects position" + str(aiturn))
            for r in range(TicTacToe.rows):
                for c in range(TicTacToe.cols):
                    if self.board[r][c].pos == aiturn:
                        self.board[r][c].state = '1'

    def isGameOver(self, player):
        #check row wins 
        for r in range(TicTacToe.rows):
            if self.board[r][0].state == player and self.board[r][1].state == player and self.board[r][2].state == player:
                return True 
        
        #check col wins
        for c in range(TicTacToe.cols):
            if self.board[0][c].state == player and self.board[1][c].state == player and self.board[2][c].state == player:
                return True 
        
        #diagonal wins
        if self.board[0][0].state == player and self.board[1][1].state == player and self.board[2][2].state == player:
            return True 

        if self.board[0][2].state == player and self.board[1][1].state == player and self.board[2][0].state == player:
            return True

    
    def display_game_over(self):
        if self.winner == 1:
            print("Player 1 wins")
        elif self.winner == 0:
            print("Player 0 wins")
        else:
            print("Tie Game")



game = TicTacToe()
game.setup()

