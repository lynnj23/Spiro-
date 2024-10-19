import turtle as t
import random


class Circle_Spiro:
    def __init__(self):
        pass

    def screen_control(self, bg_color="white"):  #sets up the screen
        t.colormode(1.0)
        screen = t.Screen()
        screen.bgcolor(bg_color)
        screen.exitonclick()

    def random_colour(self):
        r = random.random()  # Random float between 0 and 1
        g = random.random()  # Random float between 0 and 1
        b = random.random()  # Random float between 0 and 1
        return (r, g, b)

    #def random_turns(selfs):
        #turns = [pen.right(90), pen.left(90)]
        #left_rigth = random.choice(turns)
        #return (left_right)

    def spirograph_circle(self):
        t.home()
        angle = 0
        for i in range(360):
            t.pencolor(self.random_colour())
            t.setheading(angle)
            t.circle(100)
            angle += 5