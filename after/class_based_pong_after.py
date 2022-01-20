'''
name: Naser Al Madi
file: pong.py
data: 9/20/2020
course: CS151 fall
description: simple implementation of the game Pong using python 3 turtles.
'''

'''
Refactoring - 1/20/21
Bret Miller & Deka Popov 
CS321
'''

from tkinter import Y
import turtle


class Paddle:
    # implements a Pong game paddle

    def __init__(self, x_position, y_position):
        ''' initializes a paddle with a position '''

        self.x_position = x_position
        self.y_position = y_position

        self.turt = make_turtle("square", "white", 5, 1, self.x_position, self.y_position)


    def up(self):
        y = self.turt.ycor()
        y += 20
        #self.turt.sety(y)
        #New: setter 
        self.set_ycord(y)
        #self.y_position = y
        #New changed to setter
        self.set_ypos(y)


    def down(self):
        y = self.turt.ycor() #Get the current y coordinate
        y -= 20             #add 20px could also be y=y+20
        #self.turt.sety(y)    #move the paddle to the new y position
        #New: setter
        self.set_ycord(y)
        #self.y_position = y
        #New: changed to setter 
        self.set_ypos(y)

    #changed the function name
    def get_xcor(self):
        ''' returns turtle x_cord '''
        return self.turt.xcor()

    #changed the function name
    def get_ycor(self):
        ''' returns turtle y_cord '''
        return self.turt.ycor()
    
    #New
    def set_ycord(self, ycord):
        '''sets the turtle y coordinate'''
        self.turt.sety(y)
    
    def set_xcord(self, xcord):
        '''sets the turtle x coordinate'''
        self.turt.setx(xcord)
    
    #New: getter for x position instance variable
    def get_xpos(self):
        '''returns the x position'''
        return self.x_position
    
    #New: getter for y position instance 
    def get_ypos(self):
        '''returns the y position'''
        return self.y_position

    #New: setter for x position
    def set_xpos(self, xpos):
        '''sets the x position'''
        self.x_position = xpos
    
    #New: setter for y position
    def set_ypos(self, ypos):
        '''sets the y position'''
        self.y_position = ypos
    


class Ball:
    # implements a Pong game ball

    def __init__(self, ball_speed):
        ''' intializes a ball with default direction and position '''

        self.turt = make_turtle("square", "white", 1, 1, 0, 0)
        #self.ball_dx = 0.0925 #speed in x direction
        #self.ball_dy = 0.0925 #speed in y direction
        #New: Ball Speed added to the init
        self.ball_dx = ball_speed
        self.ball_dy = ball_speed
        self.x_position = 0
        self.y_position = 0


    def move(self):
        ''' moves the ball in x and y directions '''

        # Move the ball
        #self.turt.setx(self.turt.xcor() + self.ball_dx)
        #self.turt.sety(self.turt.ycor() + self.ball_dy)
        #New
        new_x = self.get_xcor() + self.ball_dx
        new_y = self.get_ycor() + self.ball_dy
        
        self.set_xcor(new_x)
        self.set_ycor(new_y)

        #self.x_position = self.turt.xcor()
        #self.y_position = self.turt.ycor()
        self.set_x(new_x)
        self.set_y(new_y)
        
        #New method to wrap around the turtle
        self.wrap_around(new_y)

        # Top and bottom
        #if new_y > 290:
            #self.set_ycor(290)
            #self.ball_dy *= -1

        #elif new_y < -290:
            #self.set_ycor(-290)
            #self.ball_dy *= -1
        
        
        
    def wrap_around(self, y_pos):
        '''Checks to see if the ball has gone beyond y boundary
        and wrap around'''
        if y_pos > 290:
            self.set_ycor(290)
            self.ball_dy *= -1
        elif y_pos < -290:
            self.set_ycor(-290)
            self.ball_dy *= -1

    #Getters and Setters for Turtle
    def get_xcor(self):
        ''' returns turtle x_cord '''
        return self.turt.xcor()

    def get_ycor(self):
        ''' returns turtle y_cord '''
        return self.turt.ycor()
    
    #New 
    def set_xcor(self, xcord):
        '''Setst the turtle x coordinate'''
        self.turt.setx(xcord)
    
    #New 
    def set_ycor(self, ycord):
        '''Sets the turtle y coordinate'''
        self.turt.sety(ycord)
        
    def goto(self, x_pos, y_pos):
        ''' moves ball to new x, y positions '''
        self.turt.goto(x_pos, y_pos)
        self.x_position = x_pos
        self.y_position = y_pos
        
    #Getters and Setters for the Balls Position 
    def get_x(self):
        '''return the balls x position'''
        return self.x_position
    
    def get_y(self):
        '''return the balls y position'''
        return self.y_position

    def set_x(self, x_cor):
        ''' sets the ball x position '''
        self.set_xcor(x_cor)
        self.x_position = x_cor
    
    def set_y(self, y_cor):
        '''sets the ball y position'''
        self.set_ycor(y_cor)
        self.y_position = y_cor



def make_window(window_title, bgcolor, width, height):
    '''this function creates a screen object and returns it'''

    window = turtle.getscreen() #Set the window size
    window.title(window_title)
    window.bgcolor(bgcolor)
    window.setup(width, height)
    window.tracer(0) #turns off screen updates for the window Speeds up the game
    return window


def make_turtle(shape, color, stretch_width, stretch_length, x_pos, y_pos):
    ''' creates a turtle and sets initial position '''

    turt = turtle.Turtle()
    turt.speed(0) # Speed of animation, 0 is max
    turt.shape(shape) # square defualt is 20,20
    turt.color(color)
    turt.shapesize(stretch_width, stretch_length) 
    turt.penup()
    turt.goto(x_pos, y_pos) #Start position
    return turt


def main():
    ''' the main function where the game events take place '''

    window = make_window("Pong - A CS151 Reproduction!", "black", 800, 600)

    # Score
    score_player1 = 0
    score_player2 = 0

    # paddels
    paddle_1 = Paddle(-350, 0)
    paddle_2 = Paddle(350, 0)

    # ball
    ball = Ball(0.0925)

    # Pen
    pen = make_turtle("square", "white", 1, 1, 0, 260)
    pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))
    pen.hideturtle()

    # Keyboard bindings
    window.listen() #Listen for keyboard input
    window.onkeypress(paddle_1.up, "w") #when you press w run paddle_a_up
    window.onkeypress(paddle_1.down, "s")
    window.onkeypress(paddle_2.up, "Up")
    window.onkeypress(paddle_2.down, "Down")

    # Main game loop
    while True:
        window.update() #This is the update to offset the wn.tracer(0)

        ball.move()

        # Border checking    
        # Left and right
        if ball.xcor() > 350:
            score_player1 += 1
            pen.clear()
            pen.write("Player A: "+ str(score_player1) + "  Player B: "+ str(score_player2), align="center", font=("Courier", 24, "normal"))
            ball.goto(0, 0)
            ball.ball_dx *= -1

        elif ball.xcor() < -350:
            score_player2 += 1
            pen.clear()
            pen.write("Player A: "+ str(score_player1) + "  Player B: "+ str(score_player2), align="center", font=("Courier", 24, "normal"))
            ball.goto(0, 0)
            ball.ball_dx *= -1

        # Paddle and ball collisions
        if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() < paddle_1.ycor() + 50 and ball.ycor() > paddle_1.ycor() - 50:
            ball.setx(-340)
            ball.ball_dx *= -1.5
        
        elif ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < paddle_2.ycor() + 50 and ball.ycor() > paddle_2.ycor() - 50:
            ball.setx(340)
            ball.ball_dx *= -1.5




if __name__ == "__main__":
	main()