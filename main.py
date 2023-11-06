import pgzrun  # first line/at the top

# Sounds from Freesound


WIDTH = 500
HEIGHT = 200

in_menu = True

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
eyeball_play = Actor("eyeball_play")
eyeball_play.center = WIDTH / 2, (HEIGHT / 2) + 16
welcome = Actor("welcome")
welcome.center = WIDTH / 2, (HEIGHT / 2) - 20
spider_restart = Actor("spider_restart")
spider_restart.bottomright = (WIDTH / 2) + 150, HEIGHT + 20
rules = Actor("rules")
rules.topleft = 0, HEIGHT / 2
author = Actor("author")
author.bottomright = WIDTH, HEIGHT


is_wand_started = False
is_bat_started = False


greenGIF = [
    "greens/green (1)",
    "greens/green (2)",
    "greens/green (3)",
    "greens/green (4)",
    "greens/green (5)",
    "greens/green (6)",
    "greens/green (7)",
    "greens/green (8)",
    "greens/green (9)",
    "greens/green (10)",
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
blueGIF = [
    "blues/blue (1)",
    "blues/blue (2)",
    "blues/blue (3)",
    "blues/blue (4)",
    "blues/blue (5)",
    "blues/blue (6)",
    "blues/blue (7)",
    "blues/blue (8)",
    "blues/blue (9)",
    "blues/blue (10)",
]
blue_frame = 0


def draw():
    screen.fill((196, 164, 132))
    if in_menu:
        eyeball_play.draw()
        welcome.draw()
        rules.draw()
        author.draw()
    else:
        wand.draw()
        potiong.draw()
        pumpkin_start.draw()
        bat.draw()
        eyeball.draw()
        spider_restart.draw()


def update():
    global green_frame
    global purple_frame
    global green2purple_frame
    global potion_color
    global blue_frame

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
            green2purple_frame = 0
            potion_color = "purple"
    elif potion_color == "purple":
        potiong.image = purpleGIF[purple_frame // 5]
        purple_frame += 1
        purple_frame %= len(purpleGIF) * 5
    elif potion_color == "blue":
        potiong.image = blueGIF[blue_frame // 5]
        blue_frame += 1
        blue_frame %= len(blueGIF) * 5

    if is_wand_started:
        wand.left += 2
        if wand.left > WIDTH:
            wand.right = 0

    if is_bat_started:
        bat.bottom -= 2
        if bat.bottom < 0:
            bat.top = HEIGHT


def on_mouse_down(pos):
    global potion_color
    global is_wand_started
    global in_menu
    global is_bat_started
    if wand.collidepoint(pos):
        potion_color = "green"
        is_bat_started = True
    if bat.collidepoint(pos):
        potion_color = "green2purple"
    if pumpkin_start.collidepoint(pos):
        is_wand_started = True
    if spider_restart.collidepoint(pos):
        potion_color = "static"
        is_wand_started = False
        in_menu = True
        is_bat_started = False
    if eyeball_play.collidepoint(pos):
        in_menu = False
    if eyeball.collidepoint(pos):
        potion_color = "blue"
        #print("Eyeball clicked")

    # sounds.shuffle_cards.play()
    # wand.center


pgzrun.go()  # last line/at the bottom
