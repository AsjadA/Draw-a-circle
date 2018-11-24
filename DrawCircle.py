import turtle
def draw_square(random):
    x = 1
    while x <= 4 :
        random.forward(100)
        random.right(90)
        x = x + 1

def draw_art():
    window = turtle.Screen()
    
    pen = turtle.Turtle()
    pen.shape("arrow")
    
    x = 1
    while x <= 36:
        draw_square(pen)
        pen.right(10)
        x = x + 1
        
    window.exitonclick()
        
draw_art()