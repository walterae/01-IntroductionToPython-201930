"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Audrey Walters.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# TODO: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()

#Define turtle jack who draws with a blue pen at a speed of 5

jack = rg.SimpleTurtle('turtle')
jack.pen = rg.Pen('blue', 3)
jack.speed = 5

for j in range (50): #Move jack in an expanding star shape
    jack.forward(j)
    jack.right(50)
    jack.backward(j-10)

#Define turtle jill who draws with a red pen at a speed of 8

jill = rg.SimpleTurtle('turtle')
jill.pen = rg.Pen('red', 1)
jill.speed = 8
radius = 100  #radius of circle

#Change inital orientation of jill

jill.left(90)
jill.forward(10)
jill.right(180)
jill.forward(60)

for j in range (6): #move jill in a decreasing circle shape

    jill.draw_circle(radius) #Draw circle
    jill.backward(5) #Move jill backwards after drawing the circle
    radius = radius - 10


window.close_on_mouse_click()

