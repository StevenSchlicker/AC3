from figures import *

width = 200
height = 200
beginfigure("example4", width, height)

save()
margin = 5
setupcoordinates([margin,margin,width-margin,height-margin], 
                 [-0.1,-0.1,1.1,1.1])

grid = Grid([-1,0.25, 1], 
            [-1,0.25,1], 
            color = lightlightgray)
grid.draw()

grid = Grid([0, 1, 1], [0,1,1], color = gray)
grid.draw()

axes = Axes()
axes.draw()

f = Function(lambda x:x*x)

rs = RiemannSum(f, 10, #  g = Function(lambda x: x*x*x), 
                domain = [0,1], fillcolor = orange,
                style = RiemannSum.TRAP) 
                               # RiemannSum(f, g, 10) makes the boxes
                               #   between the graphs of f and g
rs.fill()
rs.draw()

graph = Graph(f, color = blue, linewidth = 2)
graph.draw()

restore()
endfigure()
