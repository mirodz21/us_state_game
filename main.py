import turtle

import pandas
import turtle
from turtle import Turtle,Screen

img = "blank_states_img.gif"

screen = Screen()
screen.bgcolor("black")
screen.title("US State Game")

screen.addshape(img)
turtle.shape(img)

data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()
guessed_states = []

while len(guessed_states) < len(state_list):
    ans = screen.textinput(f"{len(guessed_states)}/{len(state_list)} States Correct","Enter a state",  ).title()
    if ans in guessed_states:
        pass
    if ans == "Exit":
        unguessed_states = [n for n in state_list if n not in guessed_states]
        pandas.DataFrame(unguessed_states).to_csv("unguessed_states.csv")
        break
    elif ans in state_list:
        guessed_states.append(ans)
        t = Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == ans]
        t.goto(state_data.x.item(),state_data.y.item())
        t.write(ans)

