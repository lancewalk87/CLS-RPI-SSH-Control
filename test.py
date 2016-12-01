import RPi.GPIO as GPIO
import time
import curses

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#elem
ans = ["On", "on", "yes", "Yes"]
resp = input("Shall we begin? ")

#GPIO
GPIO.setup(40, GPIO.OUT)

#functions
def On():
    GPIO.output(40, True)

def Off():
    GPIO.output(40, False)

#operators
if resp in ans:
    screen = curses.initscr()
    try:
        curses.noecho()
        curses.curs_set(0)
        screen.keypad(1)
        screen.addstr("Left = On\nRight = Off\n")
        event = screen.getch()
    finally:
        curses.endwin()
                
    while True:
        curses.noecho()
        curses.curs_set(0)
        screen.keypad(1)

        if event == curses.KEY_LEFT:
            On()
            screen.addstr("Turning Light On\n\n")
        elif event == curses.KEY_RIGHT:
            Off()
            screen.addstr("Turning Light Off\n\n")
        else:
            print("Terminating Script")
                
        event = screen.getch()


    else:
        print("Terminating Script")