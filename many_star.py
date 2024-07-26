from turtle import*
import colorsys

bgcolor("black")
speed(0)
pensize(1.5)

n = 50
h = 9

for i in range(270):
    c = colorsys.hsv_to_rgb(h,1,1)
    h += 1/n
    color(c)
    forward(i*2)
    left(145)
done()
