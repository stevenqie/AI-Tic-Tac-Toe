
from enum import Enum

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
        #if TicTacToe.current_state == TicTacToe.game_state.OVER:
        self.display_game_over

    
    def display_board(self):
        print("___________")
        print('\n ' + str(self.board[0][0].draw_space()) + " | " + str(self.board[0][1].draw_space()) + " | " + str(self.board[0][2].draw_space()))
        print("___|___|___")
        print('\n ' + str(self.board[1][0].draw_space()) + " | " + str(self.board[1][1].draw_space()) + " | " + str(self.board[1][2].draw_space()))
        print("___|___|___")
        print('\n ' + str(self.board[2][0].draw_space()) + " | " + str(self.board[2][1].draw_space()) + " | " + str(self.board[2][2].draw_space()))
        print("___|___|___")

    def make_move(self):
        turn = "player 0" if TicTacToe.total_turns % 2 == 0 else "player 1"

        if turn == "player 0":
            placement = int(input("Player 0, select a position: "))
            if placement < 1 or placement > 9:
                print("not valid positions")

        else:
            placement = input("Player 1, please select a position: ")
            if placement < 1 or placement > 9:
                print("not valid positions ")
            


    
    def display_game_over(self):
        pass


game = TicTacToe()
game.setup()

