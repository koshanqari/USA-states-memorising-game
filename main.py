from typing import Text
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

#Converting csv to df 
df = pd.read_csv('50_states.csv')
all_states = df['state'].to_list()

#guessed states
guessed_states = []

#game loop
num = 0
while num < 50:
    #/ taking in inputs from the screen
    def answer():
        answer1 = screen.textinput(f"Guess: {num}/50 states guessed", "Which state you think isn't named yet?").title()
        return answer1
    answer1 = answer()

    
    if answer1 == 'Exit':
        writer.goto(0, -30)
        writer.write("Your CSV file containing names of status \n which you missed has been generated", align="center", font=('arial',10,'bold'))
        break
    elif answer1 in df['state'].to_list():
        writer.goto(int(df[df['state'] == answer1]['x']), int(df[df['state'] == answer1]['y']))
        guessed_states.append(answer1)
        writer.write(answer1)
        num+=1
    else:
        print("Not Hello!")

data = {
    "Missed states": list(set(all_states) - set(guessed_states))
}
df2=  pd.DataFrame(data)
df2.to_csv("Missed States.csv")

writer.goto(0, 0)
writer.write("Thanks for playing, Hope You enjoyed it", align="center", font=('arial',15,'bold'))



#This is used to keep the screen running 
turtle.mainloop()
