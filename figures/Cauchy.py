from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("Cauchy", 3*width, height)

margin = 10
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-3, -3, 3, 3])

axes = Axes()
axes.draw()

r = 1.5

line = Line([-1,-2], [-1-1/r**2-1/r,-2], color = gray, linewidth = 1.25)
line.draw()

circle = Circle([0,0], r, color = graphcolor)
circle.draw()

p1 = Point([0,0], 1.5)
p1.setfillcolor(pointcolor)
p1.fill()
p1.draw()

circle = Circle([-1,-2], 1/r**2 + 1/r, color = tangentlinecolor)
circle.draw()

p1 = Point([-1,-2], 1.5)
p1.setfillcolor(pointcolor)
p1.fill()
p1.draw()

label = Label(r"$f(x)$", [-1.6,-2], alignment = "cb", offset = [0, 2])
label.draw()

label = Label(r"$A$", [-1,-2], alignment = "lt", offset = [0, -2])
label.draw()

restore()

save()
setupcoordinates([width + margin, margin, 2*width-margin, height-margin],
                 [-3, -3, 3, 3])

axes = Axes()
axes.draw()

line = Line([0,0], [math.sqrt(3),1], color = gray, linewidth = 1.25)
line.draw()

circle = Circle([0,0], 2, color = graphcolor)
circle.draw()

p1 = Point([0,0], 1.5)
p1.setfillcolor(pointcolor)
p1.fill()
p1.draw()

circle = Circle([-1,-2], 0.75, color = tangentlinecolor)
circle.draw()



p1 = Point([-1,-2], 1.5)
p1.setfillcolor(pointcolor)
p1.fill()
p1.draw()

label = Label(r"$x$", [0.5,0.5], alignment = "lb", offset = [2, 2])
label.draw()

label = Label(r"$0$", [0,0], alignment = "lb", offset = [2, 2])
#label.draw()

label = Label(r"$A$", [-1,-2], alignment = "lt", offset = [0, -2])
label.draw()

restore()

save()
setupcoordinates([2*width + margin, margin, 3*width-margin, height-margin],
                 [-3, -3, 3, 3])

axes = Axes()
axes.draw()

r = 2.75

line = Line([0,0], [-1,-2], color = gray, linewidth = 1.25)
line.draw()

circle = Circle([0,0], r, color = graphcolor)
circle.draw()

p1 = Point([0,0], 1.5)
p1.setfillcolor(pointcolor)
p1.fill()
p1.draw()

circle = Circle([-1,-2], 1/r**2 + 1/r, color = tangentlinecolor)
circle.draw()

p1 = Point([-1,-2], 1.5)
p1.setfillcolor(pointcolor)
p1.fill()
p1.draw()

label = Label(r"$|a_{n-1}|$", [-0.5,-1], alignment = "rb", offset = [-2, 2])
label.draw()

label = Label(r"$0$", [0,0], alignment = "lb", offset = [2, 2])
#label.draw()

label = Label(r"$A$", [-1,-2], alignment = "lt", offset = [0, -2])
label.draw()

restore()


endfigure()
