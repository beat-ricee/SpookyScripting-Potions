import pgzrun  # first line/at the top

# Sounds from Freesound


WIDTH = 500
HEIGHT = 200

potiong = Actor("potiong")
potiong.center = WIDTH / 2, HEIGHT / 2
wand = Actor("wand")
wand.topright = 0, 10
purpleGIF = [
    "purple(1)",
    "purple(2)",
    "purple(3)",
    "purple(4)",
    "purple(5)",
    "purple(6)",
    "purple(7)",
    "purple(8)",
    "purple(9)",
    "purple(10)",
    ]
purple_frame = 0
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
    "green2purple1",
    "green2purple2",
    "green2purple3",
    "green2purple4",
    "green2purple5",
    "green2purple6",
    "green2purple7",
    "green2purple8",
    "green2purple9",
    "green2purple10",
]

pumpkin_start = Actor("pumpkin_start")
pumpkin_start.bottomright = WIDTH, HEIGHT


def draw():
    screen.fill((196, 164, 132))
    wand.draw()
    potiong.draw()
    pumpkin_start.draw()


def update():
    global green_frame
    global purple_frame
    wand.left += 2
    if wand.left > WIDTH:
        wand.right = 0
    if potion_color == "static":
        potiong.image = "potiong"
    elif potion_color == "green":
        potiong.image = greenGIF[green_frame // 5]
        green_frame += 1
        green_frame %= len(greenGIF) * 5
    elif potion_color == "green2purple":
        potiong.image = green2purpleGIF[green2purple_frame // 5]
        green2purple_frame += 1
        green2purple_frame = len(green2purpleGIF):
        potion_color == "purple"
    elif potion_color == "purple":
        pass


def on_mouse_down(pos):
    global potion_color
    if wand.collidepoint(pos):
        potion_color = "green"
    if pumpkin_start.collidepoint(pos):
        # screen.fill

        pass
        # sounds.shuffle_cards.play()
        # wand.center


pgzrun.go()  # last line/at the bottom
