import pandas as pd
from tkinter import Scrollbar
from turtle import Turtle, Screen, write
import turtle

# setting up Screen with image on it 
screen = Screen()
screen.title("States Memorising game")
turt = Turtle()
writer = Turtle()
turtle.addshape('blank_states_img.gif')
turt.shape('blank_states_img.gif')
screen.setup(722, 492)

num = 0
while num < 50:
    #/ taking in inputs from the screen
    def answer():
        answer1 = screen.textinput(f"Guess: {num}/50 states guessed", "Which state you think isn't named yet?").title()
        return answer1

    answer1 = answer()

    #Converting csv to df 
    df = pd.read_csv('50_states.csv')
    # print(df)

    # print(df[df['state'] == "Alabama"]['x'])
    # print(df[df['state'] == "Alabama"]['y'])

    if answer1 in df['state'].to_list():
        writer.goto(int(df[df['state'] == answer1]['x']), int(df[df['state'] == answer1]['y']))
        writer.write(answer1)
        num+=1
    else:
        print("Not Hello!")

writer.goto(0, 230)
writer.write("Thanks for playing, Hope You enjoyed it", align="center")



#This is used to keep the screen running 
turtle.mainloop()
