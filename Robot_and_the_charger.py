import turtle

t=turtle.Turtle()

#background colour
turtle.bgcolor("red")

#size of pen
t.pen(pencolor="blue",pensize=4)

#coordinates of x and y
pos={"x":0,"y":0}

num=int(input("Enter the number of directions to be moved \n"))

for _ in range(num):
  command = input().split(" ")

  
  if command[0] == "UP":
    pos["y"]+=int(command[1])
    
    t.setheading(90)
    t.forward(int(command[1])*40)
    

  if command[0] == "DOWN":
    pos["y"]-=int(command[1])
    
    t.setheading(270)
    t.forward(int(command[1])*40)
    
        
  if command[0] == "LEFT":
    pos["x"]-=int(command[1])
    
    t.setheading(180)
    t.forward(int(command[1])*40)
    

  if command[0] == "RIGHT":
    pos["x"]+=int(command[1])
    
    t.setheading(360)
    t.forward(int(command[1])*40)
    

#to calculate the parallel distance between starting point and the final destination point
print("The Euclidean distance is",+ int(round((pos["x"]**2+pos["y"]**2)**0.5)))

