import turtle as tt
import random

kim = tt.Turtle()

# Random walk
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]
directions = [0, 90, 180, 270]
kim.pensize(15)
kim.speed("fastest")

for _ in range(200):
    kim.color(random.choice(colours))
    kim.forward(30)
    kim.setheading(random.choice(directions))
