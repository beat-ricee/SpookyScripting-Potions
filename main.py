import pgzrun  # first line/at the top

# Sounds from Freesound


WIDTH = 500
HEIGHT = 200

potiong = Actor("potiong")
potiong.center = WIDTH / 2, HEIGHT / 2
wand = Actor("wand")
wand.topright = 0, 10
bat = Actor("bat")
bat.bottomleft = 0, HEIGHT
pumpkin_start = Actor("pumpkin_start")
pumpkin_start.bottomright = WIDTH, HEIGHT
eyeball = Actor("eyeball")
eyeball.bottomleft = 150, HEIGHT

is_wand_started = False


greenGIF = [
    "greens/green1",
    "greens/green2",
    "greens/green3",
    "greens/green4",
    "greens/green5",
    "greens/green6",
    "greens/green7",
    "greens/green8",
    "greens/green9",
    "greens/green10",
]
green_frame = 0
potion_color = "static"
green2purpleGIF = [
    "green2purples/green2purple1",
    "green2purples/green2purple2",
    "green2purples/green2purple3",
    "green2purples/green2purple4",
    "green2purples/green2purple5",
    "green2purples/green2purple6",
    "green2purples/green2purple7",
    "green2purples/green2purple8",
    "green2purples/green2purple9",
    "green2purples/green2purple10",
]
green2purple_frame = 0
purpleGIF = [
    "purples/purple (1)",
    "purples/purple (2)",
    "purples/purple (3)",
    "purples/purple (4)",
    "purples/purple (5)",
    "purples/purple (6)",
    "purples/purple (7)",
    "purples/purple (8)",
    "purples/purple (9)",
    "purples/purple (10)",
]
purple_frame = 0


def draw():
    screen.fill((196, 164, 132))
    wand.draw()
    potiong.draw()
    pumpkin_start.draw()
    bat.draw()
    eyeball.draw()


def update():
    global green_frame
    global purple_frame
    global green2purple_frame
    global potion_color

    if potion_color == "static":
        potiong.image = "potiong"
    elif potion_color == "green":
        potiong.image = greenGIF[green_frame // 5]
        green_frame += 1
        green_frame %= len(greenGIF) * 5
    elif potion_color == "green2purple":
        potiong.image = green2purpleGIF[green2purple_frame // 5]
        green2purple_frame += 1
        if green2purple_frame == len(green2purpleGIF) * 5:
            potion_color = "purple"
    elif potion_color == "purple":
        potiong.image = purpleGIF[purple_frame // 5]
        purple_frame += 1
        purple_frame %= len(purpleGIF) * 5

    if is_wand_started:
        wand.left += 2
        if wand.left > WIDTH:
            wand.right = 0


def on_mouse_down(pos):
    global potion_color
    global is_wand_started
    if wand.collidepoint(pos):
        potion_color = "green"
    if bat.collidepoint(pos):
        potion_color = "green2purple"
    if pumpkin_start.collidepoint(pos):
        is_wand_started = True

    pass

    # sounds.shuffle_cards.play()
    # wand.center


pgzrun.go()  # last line/at the bottom
