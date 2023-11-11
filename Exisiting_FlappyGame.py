"""Flappy, game inspired by Flappy Bird.

Exercises

1. Keep score.
2. Vary the speed.
3. Vary the size of the balls.
4. Allow the bird to move forward and back.
"""

from random import * #built in module to generate random numbers - Ovia Kandiah
from turtle import * #pre-installed library in order to generate graphics for the game - Ovia Kandiah

from freegames import vector #vectors are being used for the positioning/controlling of the bird - Ovia Kandiah

bird = vector(0, 0) #inital position of bird when start - Ovia Kandiah
#vector() is from freegames module
balls = [] # Empty list that gets updated with position of the balls - AS


def tap(x, y):
    """Move bird up in response to screen tap."""
    up = vector(0, 30) #Moves bird up by 30 every time mouse is clicked, within onscreenclick() -Ovia Kandiah
    bird.move(up) #Moving the bird 30 up based off up defined by the vector (0,30) -Ovia Kandiah
    #function .move() is from freegames module -Ovia Kandiah

def inside(point): #Checks if element is within boundaries of the screen - AS
    """Return True if point on screen."""
    return -200 < point.x < 200 and -200 < point.y < 200 #Checks if element is on screen - AS

def draw(alive):
    """Draw screen objects."""
    clear() #clear screen when starting -Ovia Kandiah

    goto(bird.x, bird.y) #go to the vector defined by bird.x, bird.y -Ovia Kandiah

    if alive:
        dot(10, 'green')  #defining the colour of the bird when alive, graphic purposes -Ovia Kandiah
    else:
        dot(10, 'red') #defning the colour of the bird when lost, graphic purposes -Ovia Kandiah
        #10 represents the diameter of the dot/bird - Ovia Kandiah

    for ball in balls: #for loop, repeats for every item in the list balls -Ovia Kandiah
        goto(ball.x, ball.y) #going to the vector defined by ball.x and ball.y -Ovia Kandiah
        dot(20, 'black') #defining the colour of the ball when generated, graphic purposes -Ovia Kandiah
        #20 represents the size of the ball -Ovia Kandiah

    update() #updating the graphics based off the parameters and displaying these new graphics on screen -Ovia Kandiah

def move():
    """Update object positions."""
    bird.y -= 5 #Moves down 5 units when mouse is not clicked - AS

    for ball in balls: #X coordinate of balls decreases by 3 - AS
        ball.x -= 3

    if randrange(10) == 0:
        y = randrange(-199, 199) #Generates random y coordinate between -199 and 199 -Anoushka Saha
        ball = vector(199, y) #Actual position of the ball defined by vector -Anoushka Saha
        balls.append(ball)

    while len(balls) > 0 and not inside(balls[0]): #When the first item of list doesn't fit the screen, it is removed from the list - AS
        balls.pop(0) #removing the balls when they are no longer on the screen -Ovia Kandiah

    if not inside(bird): #When the bird hits the edges it dies (turns red) - AS
        draw(False)
        return

    for ball in balls: # For loop that constantly runs to check if bird hits ball
        if abs(ball - bird) < 15: #When the bird hits a ball the game stops -AS
            # distance has to be less than 15 to account for different sizes of ball vs bird - AS
            draw(False) #the bird is dead and the corresponding graphic from the function is displayed and game is stopped -Ovia Kandiah
            return

    draw(True) #Runs the draw function - AS
    ontimer(move, 50) #from pythonturtle, every 50 miliseconds call function move() -Ovia Kandiah

setup(420, 420, 370, 0) #Defines screen size - AS
hideturtle() # From pythonturtle, stops the drawing pen (no line following the 'turtle's' path)- AS
up() #Lifts pen up so no drawing occurs during movement
tracer(False) #tracer() is from pythonturtle, turns animations on and off and defines delays- Ovia Kandiah
#when tracer(false), turns off animations -Ovia Kandiah
onscreenclick(tap) #Moves bird when mouse is clicked based on what is defined in tap function
move() #move function being called - Ovia Kandiah
done() #after code is doen running, screen is paused before widnow is closed allowing the user to see when lost -Ovia Kandiah
