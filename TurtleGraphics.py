#TurtleGraphics.py
#Name: Arturo
#Date: 2/16/2025
#Assignment: Lab 4

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def drawPolygon(bob, sides):
    for s in range(sides):
        bob.forward(50)
        bob.right(360/sides) #angle of the polygon
        
def fillCorner(alice, corner):
    #draw big square
    drawSquare(alice, 100) 
    
    if corner == 1:
        alice.begin_fill()
        drawSquare(alice, 50)
        alice.end_fill()
    elif corner == 2:
        alice.forward(50)
        alice.begin_fill()
        drawSquare(alice, 50)
        alice.end_fill()
    if corner == 3:
        alice.right(90)
        alice.forward(50)
        alice.left(90)
        alice.begin_fill()
        drawSquare(alice, 50)
        alice.end_fill()
    if corner == 4:
        alice.forward(100)
        alice.right(90)
        alice.forward(100)
        alice.right(90)
        alice.begin_fill()
        drawSquare(alice, 50)
        alice.end_fill()

def squaresInSquares(zane, num): 
   zane.penup()
   zane.goto(-180, 180)
   zane.pendown()
   for n in range(4):
       zane.forward(360)
       zane.right(90)
   zane.penup()
   zane.forward(20)
   zane.right(90)
   zane.forward(20)
   zane.left(90)
   zane.pendown()
#cant figure this out at all, having trouble with this..
   for n in range(4):
       zane.forward(320)
       zane.right(90)
   zane.penup()
   zane.forward(20)
   zane.right(90)
   zane.forward(20)
   zane.left(90)
   zane.pendown()
   
   for n in range(4):
       zane.forward(280)
       zane.right(90)
   zane.penup()
   zane.forward(20)
   zane.right(90)
   zane.forward(20)
   zane.left(90)
   zane.pendown()
   
   for n in range(4):
       zane.forward(240)
       zane.right(90)
   zane.penup()
   zane.forward(20)
   zane.right(90)
   zane.forward(20)
   zane.left(90)
   zane.pendown()
   
   for n in range(4):
       zane.forward(200)
       zane.right(90)
   zane.penup()
   zane.forward(20)
   zane.right(90)
   zane.forward(20)
   zane.left(90)
   zane.pendown()
   

   
def main():
    myTurtle = turtle.Turtle()
    
    #drawSquare(myTurtle, 100)
    
    #drawPolygon(myTurtle, 5) #draws a pentagon
    #drawPolygon(myTurtle, 8) #draws an octogon
    #drawPolygon(myTurtle, 3) #this one drew a triangle!

    #fillCorner(myTurtle, 1)
    #fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    #fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.
    #fillCorner(myTurtle, 4)

    #squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    #squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()
