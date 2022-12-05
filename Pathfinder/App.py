import pygame as py
import Grid

# Constants
SCREENWIDTH = 500
SCREENHEIGHT = 500
SCREENSIZE = (SCREENWIDTH, SCREENHEIGHT)
FRAMERATE = 30
SCREENCOLOR = (0, 0, 0)


# Initialize game variables
clock = py.time.Clock()
screen = py.display.set_mode(SCREENSIZE)

# Set up game

Map = Grid.Grid(Screen = screen, Dimension = 10)


py.init()

# Main Game Loop
app_running = True
while app_running:
    #Handle Events
    for event in py.event.get():
        if event.type == py.QUIT:
            app_running = False

    #Draw
    screen.fill(SCREENCOLOR)
    Map.Draw()
   
    py.display.flip()
    #Update
   
    clock.tick(FRAMERATE)

py.quit()