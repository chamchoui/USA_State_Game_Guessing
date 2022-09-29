from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title("US State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle = Turtle()
turtle.shape(image)
state = 0


data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list() # convert all states into a list
guessed_state = []
#since kita dh tahu brp total negeri USA = 50
#so
while len(guessed_state) < 50: #guna len utk tahu length of the state list
    answer_state = screen.textinput(title=f"{len(guessed_state)}/ 50 Correct Guess the State", prompt="What's other state's name?").title()
    # state_count = len(data.state == "state" )
    # print(state_count)
    if answer_state == "Exit":
        missing_state = []
        for state in all_states:#loop thru all the list
            #check kalau state yg missing, xtahu
            if state not in guessed_state:
                missing_state.append(state)
        missing_data = pandas.DataFrame(missing_state)
        missing_data.to_csv("state_to_learn.csv")
        #jom print
        print(missing_state)
        break
    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state] #pull out the row
        t.goto(int(state_data.x), int(state_data.y))# correspond to state's x,y turtle coodinate
        #write name of the state
        t.write(state_data.state.item()) #t.write(answer_state) pon boleh juga sebab dh iterate ambil State name je
        if len(guessed_state) == 50:
            turtle.bye()

guessed_state.to_csv("state_to_learn.csv")
# screen.exitonclick()

#if answer_state is one of the states in all the states of the 50_states.csv
    #if user got it right:
        #create a turtle to write the name of the state on the state's x,y coordinate