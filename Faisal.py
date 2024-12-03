import turtle

def draw_k(t):
    t.penup()
    t.goto(-50, 0)
    t.setheading(90)  # Ensure the turtle is facing upwards
    t.pendown()
    t.forward(100)
    t.backward(50)
    t.right(45)
    t.forward(70)
    t.backward(70)
    t.right(90)
    t.forward(70)

def draw_a(t):
    t.penup()
    t.goto(30, 0)
    t.setheading(75)  # Set the initial angle for the left side of 'A'
    t.pendown()
    t.forward(100)  # Draw the left side
    t.right(150)  # Turn to draw the right side
    t.forward(100)  # Draw the right side
    t.backward(50)  # Move back to draw the crossbar
    t.right(105)  # Adjust angle for the crossbar
    t.forward(25)  # Draw the crossbar

def draw_f(t):
    t.penup()
    t.goto(100, 0)
    t.setheading(90)  # Ensure the turtle is facing upwards
    t.pendown()
    t.forward(100)
    t.right(90)
    t.forward(50)
    t.backward(50)
    t.right(90)
    t.forward(50)
    t.left(90)
    t.forward(30)

def draw_i(t):
    t.penup()
    t.goto(170, 0)
    t.setheading(90)  # Ensure the turtle is facing upwards
    t.pendown()
    t.forward(100)

def main():
    # Create a turtle object
    t = turtle.Turtle()
    
    # Make lines bolder by increasing pen size
    t.pensize(3)
    # Set the pen color to blue
    t.pencolor("blue")
    # Set the drawing speed (1 is slowest, 10 is fastest, 0 is no animation)
    t.speed(1)  # Adjust this value to control animation speed

    # Draw letters
    draw_k(t)
    draw_a(t)
    draw_f(t)
    draw_i(t)

    # Hide the turtle and display
    t.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()
