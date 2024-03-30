# Importing Turlte and pandas
import turtle
import pandas as pd

# Setting up Screen and title
screen = turtle.Screen()
screen.title("Indian States Guesser Game")

# Seting up the Indian map
image = "India states guesser.gif"
screen.addshape(image)

turtle.shape(image)

# Getting data from csv
data = pd.read_csv("states_data (1).csv")
states = data["state"].tolist()

# Empty list of guessed states
guessed_state = []


# Game loop (until length of list < 35)
while len(guessed_state) < 36:

    # input from the player
    answer_state = screen.textinput(title=f"{len(guessed_state)}/29 states",
                                    prompt="Guess the state " ).title()

    # to get the index
    count = 2

    #  exiting the game
    if answer_state == "Exit":
        missing_states = []
        for state in states:
            if state not in guessed_state:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    else:
        # adding state to thelist of guessed state if guessed by player
        for i in data["state"]:
            if i in answer_state:
                guessed_state.append(i)

                # getting x and y coordinates of the states
                x_cor = data.x[count-2]
                y_cor = data.y[count-2]

                # Moving the text to the position on maps
                t = turtle.Turtle()
                t.hideturtle()
                t.penup()
                t.goto(x_cor,y_cor)
                t.write(i)
            else:
                count = count + 1


turtle.mainloop()
screen.exitonclick()
