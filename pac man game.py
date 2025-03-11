import turtle
import random

# Screen setup
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("PAC-MAN GAME")
screen.tracer(0)


# Pac-Man setup
pacman = turtle.Turtle()
pacman.shape("circle")
pacman.color("yellow")
pacman.penup()
pacman.goto(0, -250)

# Food setup
food = turtle.Turtle()
food.shape("circle")
food.color("white")
food.penup()
food.shapesize(0.5, 0.5)
food.speed(0)
food.goto(random.randint(-280, 280), random.randint(-280, 280))

# Score setup
score = 0
score_turtle = turtle.Turtle()
score_turtle.color("white")
score_turtle.penup()
score_turtle.hideturtle()
score_turtle.goto(0, 260)
score_turtle.write(f"SCORE: {score}", align="center", font=("Arial", 24, "normal"))

#initializing pac-man size
pacman_size=20
pacman.shapesize(stretch_wid=pacman_size/20,stretch_len=pacman_size/20)

# Move directions
speed = 15
#collision detection
def is_collision(t1,t2):
    distance=t1.distance(t2)
    return distance<(pacman_size+10)


def go_up():
    if pacman.heading() != 270:
        pacman.setheading(90)

def go_down():
    if pacman.heading() != 90:
        pacman.setheading(270)

def go_left():
    if pacman.heading() != 0:
        pacman.setheading(180)

def go_right():
    if pacman.heading() != 180:
        pacman.setheading(0)

# Keyboard bindings
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")

# Game loop
def game_loop():
    global score,pacman_size

    # Move Pac-Man
    pacman.forward(speed)

    # Check for collision with walls
    if pacman.xcor() > 290 or pacman.xcor() < -290 or pacman.ycor() > 290 or pacman.ycor() < -290:
        pacman.goto(0, -250)
        pacman.setheading(90)
        score = 0
        score_turtle.clear()
        score_turtle.write(f"SCORE: {score}", align="center", font=("Arial", 24, "normal"))

    # Check for collision with food
    if is_collision(pacman, food):
        pacman_size += 2  # Increase Pac-Man's size
        pacman.shapesize(stretch_wid=pacman_size / 20, stretch_len=pacman_size / 20)
        # Reposition the food
        food.goto(random.randint(-280, 280), random.randint(-280, 280))
        # Update score
        score += 10
        score_turtle.clear()
        score_turtle.write(f"SCORE: {score}", align="center", font=("Arial", 24, "normal"))

    # Refresh screen
    screen.update()

    # Repeat the game loop
    screen.ontimer(game_loop, 100)

# Start the game loop
game_loop()

# Main event loop
screen.mainloop()








