import turtle

# Function to draw the maze walls
def draw_maze():
    # Set up the turtle screen
    screen = turtle.Screen()
    screen.setup(600, 600)
    screen.title("Maze Game")

    # Create the maze turtle
    maze_turtle = turtle.Turtle()
    maze_turtle.speed(10)  # Fastest turtle speed

    # Draw the maze walls
    maze_turtle.penup()
    maze_turtle.goto(-250, 250)
    maze_turtle.pendown()
    maze_turtle.pensize(3)
    maze_turtle.color("black")

    for _ in range(4):
        maze_turtle.forward(500)
        maze_turtle.right(90)

    # Inner walls
    maze_turtle.penup()
    maze_turtle.goto(-150, 250)
    maze_turtle.pendown()
    maze_turtle.forward(200)
    maze_turtle.right(90)
    maze_turtle.forward(300)
    maze_turtle.left(90)
    maze_turtle.forward(200)

    maze_turtle.penup()
    maze_turtle.goto(-150, -50)
    maze_turtle.pendown()
    maze_turtle.forward(200)

    maze_turtle.penup()
    maze_turtle.goto(50, 250)
    maze_turtle.pendown()
    maze_turtle.forward(200)
    maze_turtle.right(90)
    maze_turtle.forward(300)
    maze_turtle.left(90)
    maze_turtle.forward(200)

    # Exit
    maze_turtle.penup()
    maze_turtle.goto(250, -50)
    maze_turtle.pendown()
    maze_turtle.pensize(6)
    maze_turtle.color("green")
    maze_turtle.right(90)
    maze_turtle.forward(50)

    # Hide the turtle
    maze_turtle.hideturtle()

    # Function to exit the maze
    def exit_maze():
        screen.bye()

    # Bind the exit_maze function to the mouse click event
    screen.onclick(exit_maze)

    # Start the turtle main loop
    turtle.mainloop()

# Call the draw_maze function to start the game
draw_maze()
