import turtle
from turtle import *
import turtle

# ================pen=================
pen = turtle.Turtle()
border = Screen()
border.bgcolor("black")

# ==============curve=================
def curve():
	for i in range(200):
		pen.right(1)
		pen.forward(1)

# ===============heart================
def heart():
    pen.fillcolor("white")
    pen.color('white')
    pen.begin_fill()
    pen.left(140)
    pen.forward(113)
    curve()
    pen.left(120)
    curve()
    pen.forward(112)
    pen.end_fill()

# ==============text==================
def text():
	pen.up()
	pen.setpos(-68, 95)
	pen.down()
	pen.color('black')
	pen.write("        Ceries", font=(
	"Verdana", 12, "bold"))

# ===================================
heart()
text()

# ==============loop=================
pen.ht()
border.mainloop()