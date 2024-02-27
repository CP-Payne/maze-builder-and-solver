from graphics import Window, Line, Point

def main():
    win = Window(800, 600)

    start = Point(5, 5)
    end = Point(25, 25)

    line = Line(start, end)

    win.draw_line(line, "black")

    win.wait_for_close()

main()