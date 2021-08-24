import turtle
import random
import time

player1 = turtle.Turtle()  # creating player 1
player1.shape("turtle")
player1.penup()
player1.goto(10, 20)  # setting player 1s position
player1.pendown()
player1.color('blue')  # setting player1 color
player1.write('player 1')

player2 = turtle.Turtle()  # creating playeer 2
player2.shape("turtle")
player2.penup()
player2.goto(10, 80)  # setting player2 position
player2.pendown()
player2.color('red')  # setting player 2 color
player2.write('player 2')

start1 = 0
start2 = 0
end = 180

# creating end circle for player1
endTurtle1 = turtle.Turtle()
endTurtle1.penup()

# creating end circle for players 1 st position
endTurtle1.goto(200, 20)
endTurtle1.pendown()

# creating circle
endTurtle1.shape('circle')

# coloring the circle
endTurtle1.fillcolor('white')

# creating end circle fpr player 2
endTurtle2 = turtle.Turtle()
endTurtle2.penup()
# creating end circle for player 2s position
endTurtle2.goto(200, 80)
endTurtle2.pendown()
# creating a circle
endTurtle2.shape('circle')
# coloring the circle
endTurtle2.fillcolor('white')

wn = turtle.Screen()
# wn.bgcolor("light green)
# running while loop untill the start
# position for any player is less than end position
while start1 <= end or start2 <= end:
    if start1 >= end:
        # printing the player 1 name in the title
        wn.title(
            f"player1 position is {start1},player2 position is{start2},player1 wins")
        time.sleep(5)
        break
    elif start2 >= end:
        # printing the player2 name in the title
        wn.title(
            f"player1 position is {start1},player2.position is {start2},player2 wins")
        time.sleep(5)
        break

    # dice for player1
    dice1 = random.randrange(1, 6)
    # dice for player2
    dice2 = random.randrange(1, 6)
    # forwaring playe1
    player1.forward(dice1*2)
    time.sleep(1)
    # forwarding player2
    player2.forward(dice2*2)
    time.sleep(1)
    # increasing position values for player1
    start1 += dice1*2
    # increasing position values for player 2
    start2 += dice2*2
    wn.title(
        f"player1 position is {start1}, player2 position is {start2},The winner is:")
time.sleep(3)
turtle.bye()
