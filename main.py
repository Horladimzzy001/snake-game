from turtle import Turtle, Screen


tim = Turtle()

decf = 0
screen = Screen()

def move_forward():
    tim.forward(20)

screen.listen()

screen.onkey(key="space", fun=move_forward)

screen.exitonclick()

#still not done with this code
for items in range(13):
    decf += 1
    print(items)

print(decf)
