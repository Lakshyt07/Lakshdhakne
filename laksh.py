import turtle

t=turtle.Turtle()
wn=turtle.screen()
wn.bgcolor ('black')
t.color('red')
t.speed(0)
for i in range(100):
    t.forward(200)
    t.left(124)
    t.right(90)
    t.circle(200,100)