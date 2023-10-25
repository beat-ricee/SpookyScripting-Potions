import pgzrun  # first line/at the top

# Sounds from Freesound


WIDTH = 500
HEIGHT = 200

potiong = Actor("potiong")
potiong.center = WIDTH / 2, HEIGHT / 2
wand = Actor("wand")
wand.topright = 0, 10


def draw():
    screen.fill((196, 164, 132))
    wand.draw()
    potiong.draw()


def update():
    wand.left += 2
    if wand.left > WIDTH:
        wand.right = 0


def on_mouse_down(pos):
    if wand.collidepoint(pos):
        GreenGIF.draw()
        
        pass
        # sounds.shuffle_cards.play()
        # wand.center


pgzrun.go()  # last line/at the bottom
