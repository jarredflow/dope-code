from turtle import*     #imports turtle module
from random import randint      #imports random integer module

speed(0)        #sets speed of drawing to max
penup()
goto(-250,140)      #goes to starting point

for step in range(26):          #loop draws 25 vertical lines for the "track"
    write(step, align = 'center')
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)

ada = Turtle()      #creates 4 different turtle shapes and sets their own unique color and starting point
ada.color('red')
ada.shape('turtle')

ada.penup()
ada.goto(-260,100)
ada.pendown()

yes = Turtle()
yes.color('blue')
yes.shape('turtle')

yes.penup()
yes.goto(-260,70)
yes.pendown()

no = Turtle()
no.color('green')
no.shape('turtle')

no.penup()
no.goto(-260,40)
no.pendown()

um = Turtle()
um.color('purple')
um.shape('turtle')

um.penup()
um.goto(-260,10)
um.pendown()

while True:         #while loop that moves the turtles a random number of places
    ada.forward(randint(0,6))
    yes.forward(randint(0,6))
    no.forward(randint(0,6))
    um.forward(randint(0,6))
    if ada.xcor() > 250 or yes.xcor() > 250 or no.xcor() > 250 or um.xcor() > 250:
        if ada.xcor() > 250:            #if one of the turtles reaches past the x coordinate of 250, stop
            for turn in range(36):
                ada.right(10)           #whichever turtle wins, do a 360 spin
        if yes.xcor() > 250:
            for turn in range(36):
                yes.right(10)
        if no.xcor() > 250:
            for turn in range(36):
                no.right(10)
        if um.xcor() > 250:
            for turn in range(36):
                um.right(10)
        break




 
 

    
    


