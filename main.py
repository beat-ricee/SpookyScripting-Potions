import pgzrun  # first line/at the top

wand = Actor("wand")
wand.topright = 0, 10

WIDTH = 500
HEIGHT = 200

def draw():
    screen.fill((196, 164, 132))
    wand.draw()


def update():
    wand.left += 2
    if wand.left > WIDTH:
        wand.right = 0


def on_mouse_down(pos):
    if wand.collidepoint(pos):
        print("Eek!")
    else:
        print("You missed me!")

pgzrun.go()  # last line/at the bottom
