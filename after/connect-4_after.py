'''
name: Naser Al Madi
file: .py
data: 9/22/2020
course: CS151 fall
description: 
'''

'''
Refactoring - 1/20/21
Bret Miller & Deka Popov 
CS321
'''

import turtle


def make_window(window_title, bgcolor, width, height):
	''' this function creates a screen object and returns it '''

	window = turtle.getscreen() # Set the window size
	window.title(window_title)
	window.bgcolor(bgcolor)
	window.setup(width, height)
	window.tracer(0) #turns off screen updates for the window Speeds up the game
	return window


def make_turtle(shape, color, stretch_width, stretch_length, x_pos, y_pos):
    ''' creates a turtle and sets initial position '''

    turt = turtle.Turtle()
    turt.speed(0)    # Speed of animation, 0 is max
    turt.shape(shape)
    turt.color(color)
    turt.shapesize(stretch_width, stretch_length) 
    turt.penup()
    turt.goto(x_pos, y_pos) # Start position
    return turt

class Grid: 
    ''' creates a grid with initial position, tile size, and number of rows and columns '''
    def __init__(self, x_pos, y_pos, tile_size, rows, cols):
        self.x_pos = x_pos
        self.y_pos = y_pos

        self.turt = make_turtle('classic', "white", 1, 1, 0, 0 )
        self.tile_size = tile_size 
        self.rows = rows
        self.cols = cols 
        self.grid = []

        for r in range(rows):
            self.grid.append([0]* cols)
            
    def draw_grid(self): 
        for row in range(self.rows):
            for col in range(self.cols):
                self.turt.up()
                self.turt.goto(x_pos + col * tile_size, y_pos -row * tile_size)
                self.turt.down()
                if self.get_value(row, col) == 1:
                    self.turt.dot(self.tile_size-5, "red")
                elif self.get_value(row, col) == 2:
                    self.turt.dot(self.tile_size-5, "yellow")
                else:
                    self.turt.dot(self.tile_size-5, "white")
        
    def get_value(self, row, col):
        return self.grid[row][col]

    def set_value(self, row, col, value):
        self.grid[row][col] = value
    
    def get_rows(self):
        return self.rows
    
    def get_cols(self):
        return self.cols

class Game: 
    def __init__(self):
        self.window = make_window("Connect 4", "light sky blue", 800, 600)
        self.board = Grid(-150, 200, 50, 5, 7).draw_grid()
        self.turn = 1 

    def check_win(self, player):
        ''' checks the winner in the grid
        returns true if player won
        returns false if player lost
        '''
        count = 0
        for row in range(self.board.get_rows()):
            count = 0
            for col in range(self.board.get_cols()):
                if self.board.get_value(row,col) == player:
                    count += 1
                    if count == 4:
                        return True
                else:
                    count = 0
                
        # check columns
        for col in range(self.board.get_cols()):
            count = 0
            for row in range(self.board.get_rows()):
                if self.board.get_value(row,col) == player:
                    count += 1
                    if count == 4:
                        return True
                else:
                    count = 0

        # check diagonal
        for row in range(self.board.get_rows()):
            for col in range(self.board.get_cols()):

                if row + 3 < self.board.get_rows() and col + 3 < self.board.get_cols():
                    if self.board.get_value(row, col) == 1\
                    and self.board.get_value(row+1, col+1)== 1\
                    and self.board.get_value(row+2, col+2) == 1\
                    and self.board.get_value(row+3, col+3) == 1:
                        return True 

    def play(self):
        ''' the main function where the game events take place '''

        while True:

            selected_row = int(input("enter row, player "+ str(self.turn) +": "))
            selected_col = int(input("enter col, player "+ str(self.turn) +": "))

            if self.board.get_value(selected_row,selected_col) == 0:
                if self.turn == 1:
                    self.board.set_value(selected_row,selected_col,1)
                else:
                    self.board.set_value(selected_row,selected_col,2)
                
            self.board.draw_grid()
            self.window.update()

            if self.check_win(1):
                print("player 1 won")

            elif self.check_win(2):
                print("player 2 won")

            if self.turn == 1:
                self.turn = 2
            else:
                self.turn = 1

if __name__ == "__main__":
    new_game = Game()
    new_game.play()
