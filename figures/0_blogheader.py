from figures import *
from defaults import *

width = 150
height = 150

beginfigure("0_blogheader", 6*width, height)

save()
margin = 10
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-1, -1, 5, 5])

grid = Grid([-1, 6, 5], [-1, 6, 5])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()
axes = Axes()
axes.draw()

axes.sethticks([1, 3, 3])
axes.setvticks([2, 4, 5])
axes.setvticksize(1)
axes.drawticks()
axes.sethticksize(10)

label = Label("$x$", [4.5, 0.2])
label.draw()

label = Label("$y$", [0.3, 4.5])
label.draw()

label = Label("$f$", [4, 4])
label.draw()

label = Label("$a$", [0.9, -0.5])
label.draw()

def f(x):
    return 0.1*x*(x+2)*(x-3) + 2

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([-1,5])
graph.draw()

def g(x):
    return f(1) + (f(2.5)-f(1))/(2.5-1)*(x-1)

graph = Graph(Function(g))
graph.setcolor(magenta)
graph.setlinewidth(graphwidth)
graph.setdomain([0.2,4.3])
graph.draw()

def g(x):
    return f(1) + (f(2.0)-f(1))/(2.0-1)*(x-1)

graph = Graph(Function(g))
graph.setcolor(magenta)
graph.setlinewidth(graphwidth)
graph.setdomain([0.0,3.7])
graph.draw()

def g(x):
    return f(1) + (f(1.5)-f(1))/(1.5-1)*(x-1)

graph = Graph(Function(g))
graph.setcolor(magenta)
graph.setlinewidth(graphwidth)
graph.setdomain([-0.2,2.9])
graph.draw()

a = 1
dx = 1.4
tangentline = Function(f).tangentline(a)
tangent = Graph(tangentline)
tangent.setdomain([a-dx, a+dx])
tangent.setlinewidth(graphwidth)
tangent.setcolor(tangentlinecolor)
tangent.draw()

point = Point([1, f(1)], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

point = Point([2.5, f(2.5)], 2)
point.setfillcolor(magenta)
point.fill()
point.draw()

point = Point([2.0, f(2.0)], 2)
point.setfillcolor(magenta)
point.fill()
point.draw()

point = Point([1.5, f(1.5)], 2)
point.setfillcolor(magenta)
point.fill()
point.draw()

box = Box([0.3, f(1)-0.7, 1.4, 1.4], color = darkgray)
box.draw()

restore()
save()
margin = 10

################

setupcoordinates([width+margin, margin, 2*width-margin, height-margin],
                 [0.3,0.7,1.7,2.1])

outline = Box([0.3,0.7,1.4,1.4], color=darkgray) # arguments are lower left corner, width and heigh
outline.draw()

def f(x):
    return 0.1*x*(x+2)*(x-3) + 2

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
##graph.setdomain([-1,5])
graph.draw()

def g(x):
    return f(1) + (f(1.5)-f(1))/(1.5-1)*(x-1)

graph = Graph(Function(g))
graph.setcolor(magenta)
graph.setlinewidth(graphwidth)
##graph.setdomain([-0.2,2.9])
graph.draw()

a = 1
dx = 1.4
tangentline = Function(f).tangentline(a)
tangent = Graph(tangentline)
##tangent.setdomain([a-dx, a+dx])
tangent.setlinewidth(graphwidth)
tangent.setcolor(tangentlinecolor)
tangent.draw()

point = Point([1, f(1)], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

point = Point([1.5, f(1.5)], 2)
point.setfillcolor(magenta)
point.fill()
point.draw()

restore()
save()
margin = 10

######################

setupcoordinates([2*width + margin, margin, 3*width-margin, height-margin],
                 [-5, -5, 5, 5])

grid = Grid([-5, 10, 5], [-5, 10, 5])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([-4, 1, 4]) # you can do this in one line with setticks([], [])
axes.setvticks([-4, 1, 4])
#axes.drawticks()

axes.setlabels([-4, 4, 4], # you can do this separately with seth(v)labels
               [-4, 4, 4])
#axes.drawlabels()

def f(x,y):
    return x*x*x - y*y*y - 6*x*y

Implicit(f, 0, color=graphcolor).draw()

line = Line([-4.5,1.5], [-1.5,4.5], color = tangentlinecolor, linewidth = graphwidth)
line.draw()

point = Point([-3, 3], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()


label = Label(r"$x^3 - y^3 = 6xy$", [0.2,3], alignment = "lb", offset = [2, 2])
label.draw()


label = Label(r"$x$", [4.2,0.2], alignment = "lb", offset = [2, 2])
label.draw()

restore()
save()
margin = 10

######################

setupcoordinates([3*width+margin,margin,4*width-margin,height-margin], 
                 [-1, -1, 3, 2])

grid = Grid([-1,4,3], [-1,3,2], color = gridcolor)
grid.setlinewidth = gridwidth
grid.draw()

axes = Axes()
axes.draw()

axes.setticks([0,1,2], [0,1,2])
#axes.drawticks()

import math
f = Function(lambda x:math.cos(2.5*x)+0.5)
a = f.solve(1)
b = f.solve(1.7)
x0 = 2.8

rs = RiemannSum(f, 12, #  g = Function(lambda x: x*x*x), 
                domain = [0.2,x0], fillcolor = boxcolor,
                style = RiemannSum.LEFT) 
                               # RiemannSum(f, g, 10) makes the boxes
                               #   between the graphs of f and g
rs.fill()
rs.draw()


graph = Graph(f, color = blue, linewidth = graphwidth)
graph.draw()

label = Label(r"$y = f(x)$", [0.1,1.5], alignment = "lb", offset = [2, 2] )
label.draw()

line = Line([0.1,-0.6],[2.9,-0.6], linewidth = 1, color=black)
line.draw()

x1 = 0.2
line = Line([x1,-0.55],[x1,-0.65], color=black, linewidth = 1)
line.draw()

label = Label(r"$a$", [0.2,-0.95], alignment = "cb", offset = [0, 2] )
label.draw()

line = Line([a,-0.55],[a,-0.65], color=black, linewidth = 1)
line.draw()

label = Label(r"$b$", [a,-0.95], alignment = "cb", offset = [0, 2] )
label.draw()

line = Line([b,-0.55],[b,-0.65], color=black, linewidth = 1)
line.draw()

label = Label(r"$c$", [b,-0.95], alignment = "cb", offset = [0, 2] )
label.draw()

line = Line([x0,-0.55],[x0,-0.65], color=black, linewidth = 1)
line.draw()

label = Label(r"$d$", [x0,-0.95], alignment = "cb", offset = [0, 2] )
label.draw()



label = Label(r"$A_1$", [0.42,0.5], alignment = "cc", offset = [0, 0] )
#label.draw()

label = Label(r"$A_2$", [1.25,-0.2], alignment = "cc", offset = [0, 0] )
#label.draw()

label = Label(r"$A_3$", [2.35,0.5], alignment = "cc", offset = [0, 0] )
#label.draw()






restore()
#################

save()
margin = 10
setupcoordinates([4*width+margin,margin,5*width-margin,height-margin], 
                 [-0.5,-0.5,3.5,4.5])

grid = Grid([-0.5,4,3.5], 
            [-0.5,5,4.5], 
            color = lightgray)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([0,1,3]) # you can do this in one line with setticks([], [])
axes.setvticks([0,1,3])
#axes.drawticks()

axes.setlabels([1,1,3], # you can do this separately with seth(v)labels
               [1,2,3])
#axes.drawlabels()

f = Function(lambda x: 0.5*(x-1)**2 + 1)

area = AreaBetweenCurves(f, fillcolor = lightblue, domain=[0.5,3])
area.fill()
area.draw()

graph = Graph(f, color = graphcolor, linewidth = graphwidth)
graph.draw()

label = Label("$a$", [0.5,-0.5], alignment = "cb", offset = [0, 2] )
label.draw()

label = Label("$b$", [3,-0.5], alignment = "cb", offset = [0, 2] )
label.draw()

label = Label(r"$\int_a^b f(x) \, dx$", [1.75,0.5], alignment = "cc", offset = [0, 0] )
label.draw()

label = Label(r"$y = f(x)$", [3.4,4], alignment = "rb", offset = [-2, 2] )
label.draw()


restore()

##############

save()
margin = 10
setupcoordinates([5*width+margin,margin,6*width-margin,height-margin], 
                 [-0.5,-0.5,3.5,4.5])

grid = Grid([-0.5,4,3.5], 
            [-0.5,5,4.5], 
            color = lightgray)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([0,1,3]) # you can do this in one line with setticks([], [])
axes.setvticks([0,1,3])
#axes.drawticks()

axes.setlabels([1,1,3], # you can do this separately with seth(v)labels
               [1,2,3])
#axes.drawlabels()

f = Function(lambda x: 0.5*(x-1)**2 + 1)

area = AreaBetweenCurves(f, fillcolor = lightblue, domain=[0.5,3])
area.fill()
area.draw()

f = Function(lambda x: 1.54167)

area = AreaBetweenCurves(f, fillcolor = lightgreen, domain=[0.5,3])
area.fill()
area.draw()

graph = Graph(f, color = darkgreen, linewidth = graphwidth)
graph.draw()

f = Function(lambda x: 0.5*(x-1)**2 + 1)
graph = Graph(f, color = lightblue, linewidth = 1)
graph.draw()

label = Label("$a$", [0.5,-0.5], alignment = "cb", offset = [0, 2] )
label.draw()

label = Label(r"$f_{\mbox{\tiny{AVG}}[a,b]}$", [0, 1.54], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label(r"$(b-a) \cdot f_{\mbox{\tiny{AVG}}[a,b]}$", [1.75, 0.5], alignment = "cc", offset = [0,0] )
label.draw()

label = Label("$b$", [3,-0.5], alignment = "cb", offset = [0, 2] )
label.draw()

label = Label(r"$y = f(x)$", [3.4,4], alignment = "rb", offset = [-2, 2] )
label.draw()
restore()

##################



endfigure()
