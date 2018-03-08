"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Ji Li.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:
    two_circles()
    circle_and_rectangle(100,200,50,100,150,300,50)
    lines(10,10,100,300,200,10,10,100)


def two_circles():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    window = rg.RoseWindow()

    ca = rg.Point(80, 100)
    cb = rg.Point(200, 200)
    ra = 50
    rb = 100

    circle1 = rg.Circle(ca, ra)
    circle2 = rg.Circle(cb, rb)
    circle2.fill_color = 'blue'
    circle1.attach_to(window)
    circle2.attach_to(window)

    window.render()
    window.close_on_mouse_click()

    # -------------------------------------------------------------------------
    # DONE: 2. Implement this function, per its doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.txt  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # -------------------------------------------------------------------------


def circle_and_rectangle(x1, y1, a1, b1, a2, b2, radius):
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """
    window = rg.RoseWindow()

    color = 'blue'
    centerc = rg.Point(x1, y1)
    circle = rg.Circle(centerc,radius)
    circle.fill_color = color

    p1 = rg.Point(a1, b1)
    p2 = rg.Point(a2, b2)
    rtg = rg.Rectangle(p1, p2)

    circle.attach_to(window)
    rtg.attach_to(window)


    print(circle.outline_thickness)
    print(circle.fill_color)
    print(circle.center)
    print(centerc.x)
    print(centerc.y)
    print(rtg.outline_thickness)
    print(rtg.fill_color)
    print(rtg.corner_2)
    print(p2.x)
    print(p2.y)

    window.render()
    window.close_on_mouse_click()






    circle = rg.Circle


    # -------------------------------------------------------------------------
    # DONE: 3. Implement this function, per its doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # -------------------------------------------------------------------------


def lines(x1, y1, x2, y2, xa, ya, xb, yb):
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    window = rg.RoseWindow()

    P1 = rg.Point(x1, y1)
    P2 = rg.Point(x2, y2)
    L1 = rg.Line(P1, P2)
    L1.attach_to(window)

    Pa = rg.Point(xa, ya)
    Pb = rg.Point(xb, yb)
    L2 = rg.Line(Pa, Pb)
    L2.color = 'pink'
    L2.thickness = 5
    L2.attach_to(window)

    mp = L2.get_midpoint()

    print(L2.get_midpoint())
    print(mp.x)
    print(mp.y)

    window.render()
    window.close_on_mouse_click()



    # -------------------------------------------------------------------------
    # DONE: 4. Implement and test this function.
    # -------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
