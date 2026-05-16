"""
Raphael A. Solis
BSIS 1-04
Final Project in ITE102

IMPORTANT NOTICE!
Install MPV first for audio to play. ^^
"""
import turtle # For Graphics
import time
import os # For audio play to be inserted and play.

# AUDIO UTILITY
def play_audio(filename):
    # Attempts to play audio in the background. Skips if mpv is missing.
    try:
        os.system(f"mpv {filename} &")
    except Exception:
        pass 

# DRAWING FUNCTIONS

def draw_land(land):
    #Draws the green ground/grass area
    land.penup()
    land.goto(-700, -100)
    land.setheading(0)
    land.pendown()
    land.color("#228B22")
    land.begin_fill()
    for _ in range(2):
        land.forward(1400)
        land.right(90)
        land.forward(500)
        land.right(90)
    land.end_fill()

def draw_cloud(cloud, x, y):
    #Draws white clouds using circles
    cloud.penup()
    cloud.goto(x, y)
    cloud.color("white")
    for _ in range(3):
        cloud.begin_fill()
        cloud.circle(15)
        cloud.end_fill()
        cloud.forward(20)

def draw_bird(bird, x, y):
    #Draws simple black birds using arcs
    bird.penup()
    bird.goto(x, y)
    bird.color("black")
    bird.setheading(45)
    bird.pendown()
    bird.circle(15, 90)
    bird.setheading(45)
    bird.circle(15, 90)
    bird.penup()

def draw_flower(flower, x, y):
    #Draws red and yellow flowers using dots
    flower.penup()
    flower.goto(x, y)
    flower.color("red")
    for _ in range(5):
        flower.dot(8)
        flower.forward(3)
    flower.color("yellow")
    flower.goto(x, y)
    flower.dot(5)

def draw_glass_pane(glass_panel, x, y):
    #Draws light blue highlights for window glass
    glass_panel.penup()
    glass_panel.goto(x + 5, y + 5)
    glass_panel.color("#E0F7FA") 
    glass_panel.begin_fill()
    for _ in range(4):
        glass_panel.forward(20)
        glass_panel.left(90)
    glass_panel.end_fill()

def draw_building(building, x, y, color):
    #Draws a city building with windows
    building.penup()
    building.goto(x, y)
    building.pendown()
    building.color("black", color)
    building.begin_fill()
    for _ in range(2):
        building.forward(70)
        building.left(90)
        building.forward(160)
        building.left(90)
    building.end_fill()
    # Draw yellow window lights
    for wy in [y+40, y+90, y+130]:
        building.penup()
        building.goto(x+15, wy)
        building.color("black", "yellow")
        building.begin_fill()
        for _ in range(4):
            building.forward(20)
            building.left(90)
        building.end_fill()

def draw_store(store, x, y, color):
    #Draws a shop structure with a red awning
    store.penup()
    store.goto(x, y)
    store.pendown()
    store.color("black", color)
    store.begin_fill()
    for _ in range(2):
        store.forward(90)
        store.left(90)
        store.forward(110)
        store.left(90)
    store.end_fill()
    # Draw red roof/awning
    store.penup()
    store.goto(x-5, y+110)
    store.pendown()
    store.color("red")
    store.begin_fill()
    for _ in range(2):
        store.forward(100)
        store.right(90)
        store.forward(20)
        store.right(90)
    store.end_fill()


def draw_house(house, x, y):
    #Draws a complete house with roof, door, and windows
    width, height = 120, 140
    house.penup()
    house.goto(x, y)
    house.setheading(0)
    house.pendown()
    house.color("black", "#E0E0E0")
    house.begin_fill()
    for _ in range(2):
        house.forward(width)
        house.left(90)
        house.forward(height)
        house.left(90)
    house.end_fill()
    
    # Draw Roof
    house.penup()
    house.goto(x - 10, y + height)
    house.pendown()
    house.color("black", "#8B0000")
    house.begin_fill()
    house.goto(x + (width / 2), y + height + 50)
    house.goto(x + width + 10, y + height)
    house.goto(x - 10, y + height)
    house.end_fill()
    
    # Draw Door
    house.penup()
    house.goto(x + (width / 2) - 15, y)
    house.pendown()
    house.color("black", "#5C4033")
    house.begin_fill()
    for _ in range(2):
        house.forward(30)
        house.left(90)
        house.forward(45)
        house.left(90)
    house.end_fill()
    
    # Draw Windows
    for offset in [15, width - 45]:
        house.penup()
        house.goto(x + offset, y + height - 50)
        house.pendown()
        house.color("black", "skyblue")
        house.begin_fill()
        for _ in range(4):
            house.forward(30)
            house.left(90)
        house.end_fill()
        draw_glass_pane(house, x + offset, y + height - 50)


def draw_sun(sun, x, y, radius):
    #Draws the sun with its rays
    sun.penup()
    sun.goto(x, y)
    sun.setheading(0)
    sun.pendown()
    sun.color("orange", "yellow")
    sun.begin_fill()
    sun.circle(radius)
    sun.end_fill()
    
    # Draw Sun Rays
    for _ in range(12):
        sun.penup()
        sun.circle(radius, 30)
        sun.right(90)
        sun.forward(5)
        sun.pendown()
        sun.forward(15)
        sun.penup()
        sun.backward(20)
        sun.left(90)


def draw_bedroom(bedroom):
    #Sets up the bedroom scene (walls, floor, furniture)
    bedroom.clear()
    screen.bgcolor("#1a1a2e")
    
    # Floor
    bedroom.penup()
    bedroom.goto(-700, -100)
    bedroom.pendown()
    bedroom.color("#16213e")
    bedroom.begin_fill()
    for _ in range(2):
        bedroom.forward(1400)
        bedroom.right(90)
        bedroom.forward(400)
        bedroom.right(90)
    bedroom.end_fill()
    
    # Bed Frame
    bedroom.penup()
    bedroom.goto(-200, -100)
    bedroom.color("#4e342e")
    bedroom.begin_fill()
    for _ in range(2):
        bedroom.forward(400)
        bedroom.left(90)
        bedroom.forward(60)
        bedroom.left(90)
    bedroom.end_fill()
    
    # Mattress/Bedding
    bedroom.penup()
    bedroom.goto(-190, -40)
    bedroom.color("#533483")
    bedroom.begin_fill()
    for _ in range(2):
        bedroom.forward(380)
        bedroom.left(90)
        bedroom.forward(50)
        bedroom.left(90)
    bedroom.end_fill()
    
    # Pillow
    bedroom.penup()
    bedroom.goto(-185, 10)
    bedroom.color("white")
    bedroom.begin_fill()
    for _ in range(2):
        bedroom.forward(70)
        bedroom.left(90)
        bedroom.forward(35)
        bedroom.left(90)
    bedroom.end_fill()
    
    # Wardrobe/Closet
    bedroom.penup()
    bedroom.goto(250, -100)
    bedroom.color("#3e2723")
    bedroom.begin_fill()
    for _ in range(2):
        bedroom.forward(130)
        bedroom.left(90)
        bedroom.forward(280)
        bedroom.left(90)
    bedroom.end_fill()
    
    # Wardrobe Details (Doors/Handles)
    bedroom.color("black")
    bedroom.width(2)
    bedroom.penup()
    bedroom.goto(315, -100)
    bedroom.pendown()
    bedroom.goto(315, 180)
    bedroom.penup()
    bedroom.goto(305, 50)
    bedroom.dot(6, "gold")
    bedroom.goto(325, 50)
    bedroom.dot(6, "gold")
    
    # Window (Outer)
    bedroom.width(1)
    bedroom.penup()
    bedroom.goto(-550, 200)
    bedroom.color("#000033")
    bedroom.begin_fill()
    for _ in range(2):
        bedroom.forward(120)
        bedroom.right(90)
        bedroom.forward(150)
        bedroom.right(90)
    bedroom.end_fill()
    
    # Window Frame/Panes
    bedroom.color("#E0F7FA")
    bedroom.width(4)
    bedroom.penup()
    bedroom.goto(-550, 200)
    bedroom.pendown()
    for _ in range(2):
        bedroom.forward(120)
        bedroom.right(90)
        bedroom.forward(150)
        bedroom.right(90)
    bedroom.penup()
    bedroom.goto(-490, 200)
    bedroom.pendown()
    bedroom.goto(-490, 50)
    bedroom.penup()
    bedroom.goto(-550, 125)
    bedroom.pendown()
    bedroom.goto(-430, 125)
    
    bedroom.width(1)
    screen.update()

def draw_person(person, x, y, shirt_color, is_girl=False, has_rose=False, is_hugging=False, is_laying=False):
    #Universal character drawing function for all scenes
    person.penup()
    person.goto(x, y)
    person.setheading(0)
    person.color("black", shirt_color)
    # Drawing logic for a laying person (Raphael in bed)
    if is_laying:
        person.begin_fill()
        for _ in range(2):
            person.forward(50)
            person.left(90)
            person.forward(20)
            person.left(90)
        person.end_fill()
        person.penup()
        person.goto(x - 10, y + 10)
        person.pendown()
        person.color("black", "#FFDBAC")
        person.begin_fill()
        person.circle(12)
        person.end_fill()
    # Drawing logic for standing people
    else:
        person.begin_fill()
        if is_girl: # Triangle shape for dress
            person.goto(x - 15, y - 35)
            person.goto(x + 15, y - 35)
            person.goto(x, y)
        else: # Rectangle shape for shirt
            person.goto(x - 10, y)
            for _ in range(2):
                person.forward(20)
                person.left(90)
                person.forward(30)
                person.left(90)
        person.end_fill()
        person.penup()
        person.goto(x, y + (0 if is_girl else 30))
        person.pendown()
        person.color("black", "#FFDBAC")
        person.begin_fill()
        person.circle(10)
        person.end_fill()
    # Arms/Item details
    if is_hugging:
        person.penup()
        person.color("black")
        person.goto(x, y + 15)
        person.setheading(0 if x < 0 else 180)
        person.pendown()
        person.forward(25)
    elif has_rose:
        person.penup()
        person.goto(x + (12 if not is_girl else -12), y + 15)
        person.pendown()
        person.color("blue")
        person.goto(x + (25 if not is_girl else -25), y + 25)
        person.color("red")
        person.dot(8)

def draw_desk(desk, x, y):
    #Draws a classroom desk
    desk.penup()
    desk.goto(x - 30, y - 40)
    desk.pendown()
    desk.color("black", "#5D4033") 
    desk.begin_fill()
    for _ in range(2):
        desk.forward(60)
        desk.right(90)
        desk.forward(10)
        desk.right(90)
    desk.end_fill()

def draw_whiteboard(whiteboard):
    #Draws the classroom whiteboard with text code
    whiteboard.penup()
    whiteboard.goto(-300, 250)
    whiteboard.color("black", "white")
    whiteboard.begin_fill()
    for _ in range(2):
        whiteboard.forward(600)
        whiteboard.right(90)
        whiteboard.forward(180)
        whiteboard.right(90)
    whiteboard.end_fill()
    whiteboard.penup()
    whiteboard.goto(-280, 225)
    whiteboard.color("blue")
    whiteboard.write("ITE102: Python Basics", font=("Courier", 14, "bold"))
    whiteboard.penup()
    whiteboard.goto(-280, 140)
    whiteboard.color("black")
    whiteboard.write("print('Final Project')\nif Raphael == Dreaming:\n    print('Happiness')\nelse:\n    print('Reality')", font=("Courier", 10, "normal"))


def draw_classroom(classroom):
    #Assembles the classroom scene with students and clock
    classroom.clear()
    screen.bgcolor("#DEB887")
    draw_whiteboard(classroom)
    classroom.penup()
    classroom.goto(-700, 0)
    classroom.pendown()
    classroom.color("#8B4513")
    classroom.begin_fill()
    for _ in range(2):
        classroom.forward(1400)
        classroom.right(90)
        classroom.forward(500)
        classroom.right(90)
    classroom.end_fill()
    # Back Row Students
    classmates_back = [(-450, -100, "gray"), (-150, -100, "purple"), (150, -100, "yellow"), (450, -100, "pink")]
    for cx, cy, color in classmates_back:
        draw_desk(classroom, cx, cy)
        draw_person(classroom, cx, cy, color)
    # Front Row Students
    classmates_front = [(-300, -250, "orange"), (0, -250, "cyan")]
    for cx, cy, color in classmates_front:
        draw_desk(classroom, cx, cy)
        draw_person(classroom, cx, cy, color)
    # Raphael's Seat
    draw_desk(classroom, 300, -250)
    draw_person(classroom, 300, -250, "blue")
    # Clock on Wall
    classroom.penup()
    classroom.goto(500, 165)
    classroom.setheading(0)
    classroom.color("white")
    classroom.begin_fill()
    classroom.circle(35)
    classroom.end_fill()
    classroom.color("black")
    classroom.width(2)
    classroom.pendown()
    classroom.circle(35)
    classroom.penup()
    classroom.goto(500, 200)
    classroom.setheading(90)
    classroom.pendown()
    classroom.forward(25)
    classroom.penup()
    classroom.goto(500, 200)
    classroom.setheading(0)
    classroom.pendown()
    classroom.forward(15)
    classroom.width(1)
    screen.update()

def draw_afar_scene(afar_scene, hide_others=False, is_night=False):
    #Draws the city scene used for walking home/reality
    afar_scene.clear()
    if is_night:
        screen.bgcolor("#0f3460")
             # Draw a Crescent Moon (Moved inside the if statement and fixed names/colors)
        afar_scene.penup()
        afar_scene.goto(-500, 300)
        afar_scene.color("yellow")
        afar_scene.begin_fill()
        afar_scene.circle(40)
        afar_scene.end_fill()
        
        afar_scene.penup()
        afar_scene.goto(-480, 310) # Offset to cut out the crescent
        afar_scene.color("#0f3460") # Matches the exact night sky color
        afar_scene.begin_fill()
        afar_scene.circle(40)
        afar_scene.end_fill()
    else:
        screen.bgcolor("#87CEEB")
        draw_sun(afar_scene, 450, 350, 40) 
    draw_cloud(afar_scene, -400, 320)
    draw_cloud(afar_scene, -100, 350)
    draw_cloud(afar_scene, 200, 310)
    draw_bird(afar_scene, -250, 280)
    draw_bird(afar_scene, 50, 300)
    draw_land(afar_scene)
    # Background city buildings
    draw_building(afar_scene, -550, -100, "#7f8c8d")
    draw_building(afar_scene, -400, -100, "#95a5a6")
    draw_store(afar_scene, -150, -100, "#ecf0f1")
    draw_building(afar_scene, 100, -100, "#7f8c8d") 
    draw_building(afar_scene, 450, -100, "#95a5a6")
    # Street flowers
    for tx in [-600, -300, 0, 300, 650]:
        afar_scene.penup()
        afar_scene.goto(tx, -100)
        afar_scene.color("#1b5e20")
        afar_scene.dot(25) 
        draw_flower(afar_scene, tx + 15, -115)
        draw_flower(afar_scene, tx - 20, -125)
    # Character appearance logic
    draw_person(afar_scene, -300, -130, "blue")
    if not hide_others:
        draw_person(afar_scene, 200, -100, "red", is_girl=True)
        draw_person(afar_scene, 230, -130, "yellow", has_rose=True)
    screen.update()

def draw_crying_face(crying_face):
    #Draws a close-up sad face for the heartbreak scene
    crying_face.clear()
    screen.bgcolor("#0a0a0a")
    # Skin
    crying_face.penup()
    crying_face.goto(0, -150)
    crying_face.color("#E2C391")
    crying_face.begin_fill()
    crying_face.circle(155)
    crying_face.end_fill()
    crying_face.penup()
    crying_face.goto(0, -150)
    crying_face.color("#FFDBAC")
    crying_face.begin_fill()
    crying_face.circle(150)
    crying_face.end_fill()
    # Brows
    crying_face.width(4)
    crying_face.color("#4B3621")
    crying_face.penup()
    crying_face.goto(-70, 70)
    crying_face.setheading(20)
    crying_face.pendown()
    crying_face.circle(-40, 50)
    crying_face.penup()
    crying_face.goto(70, 70)
    crying_face.setheading(160)
    crying_face.pendown()
    crying_face.circle(40, 50)
    # Sad Eyes
    crying_face.width(3)
    crying_face.color("black")
    crying_face.penup()
    crying_face.goto(-60, 30)
    crying_face.setheading(-20)
    crying_face.pendown()
    crying_face.circle(30, 40)
    crying_face.penup()
    crying_face.goto(60, 30)
    crying_face.setheading(200)
    crying_face.pendown()
    crying_face.circle(-30, 40)
    # Frown
    crying_face.penup()
    crying_face.goto(-40, -60)
    crying_face.setheading(-30)
    crying_face.pendown()
    crying_face.circle(80, 60)
    screen.update()

def draw_scene(scene, boy_x, girl_x, rose_owner="boy", hugging=False):
    #Combines mountains, house, and people for the dream sequence
    scene.clear()
    draw_sun(scene, 450, 350, 40)
    draw_cloud(scene, -400, 320)
    draw_cloud(scene, -150, 350)
    draw_cloud(scene, 250, 330)
    draw_bird(scene, -200, 280)
    draw_bird(scene, 100, 300)
    
    # Mountains
    scene.penup()
    scene.color("#8B4513")
    scene.goto(-700, -100)
    scene.begin_fill()
    scene.goto(-350, 280)
    scene.goto(100, -100)
    scene.end_fill()
    scene.color("#A0522D")
    scene.goto(-150, -100)
    scene.begin_fill()
    scene.goto(200, 120)
    scene.goto(700, -100)
    scene.end_fill()
    
    # Terrain details
    draw_land(scene)
    draw_house(scene, -450, -100)
    for fx in [-600, -300, 0, 300, 600]:
        draw_flower(scene, fx, -120)
        draw_flower(scene, fx + 40, -140)
        
    # Trees
    for tx in [-580, -320, 120, 550]:
        scene.penup()
        scene.goto(tx - 8, -100)
        scene.pendown()
        scene.color("#5C4033")
        scene.begin_fill()
        for _ in range(2):
            scene.forward(16)
            scene.left(90)
            scene.forward(25)
            scene.left(90)
        scene.end_fill()
        scene.penup()
        scene.goto(tx - 25, -75)
        scene.color("green")
        scene.begin_fill()
        for _ in range(3):
            scene.forward(50)
            scene.left(120)
        scene.end_fill()
        
    # Scene characters
    draw_person(scene, girl_x, -100, "red", is_girl=True, has_rose=(rose_owner == "girl"), is_hugging=hugging)
    draw_person(scene, boy_x, -130, "blue", has_rose=(rose_owner == "boy"), is_hugging=hugging)
    screen.update()


# UTILITY FUNCTIONS

def type_talk(msg, x, y, speed=0.07, hold=2.0):
    #Simulates typewriter-style dialogue text
    current_text = ""
    for char in msg:
        current_text += char
        writer.clear()
        writer.goto(x, y)
        writer.write(current_text, align="center", font=("Arial", 11, "bold italic"))
        screen.update()
        time.sleep(speed)
    time.sleep(hold)
    writer.clear()

def talk(msg, x, y, delay):
    # Static dialogue text with a set delay
    writer.clear()
    writer.goto(x, y)
    writer.write(msg, align="center", font=("Arial", 11, "bold italic"))
    screen.update()
    time.sleep(delay)

def draw_cemetery(cemetery):
    cemetery.clear()
    screen.bgcolor("#1a1a2e") # Deep midnight blue
    
    # Draw Ground (Darker, hilly terrain)
    cemetery.penup()
    cemetery.goto(-700, -100)
    cemetery.pendown()
    cemetery.color("#0d1b1e") 
    cemetery.begin_fill()
    cemetery.goto(700, -100)
    cemetery.goto(700, -500)
    cemetery.goto(-700, -500)
    cemetery.end_fill()

    # Draw a Crescent Moon
    cemetery.penup()
    cemetery.goto(-500, 300)
    cemetery.color("yellow")
    cemetery.begin_fill()
    cemetery.circle(40)
    cemetery.end_fill()
    cemetery.penup()
    cemetery.goto(-480, 310) # Offset to cut out the crescent
    cemetery.color("#1a1a2e")
    cemetery.begin_fill()
    cemetery.circle(40)
    cemetery.end_fill()

    # Background Tombstones (Small/Silhouettes)
    background_stones = [(-400, -100), (-200, -100), (400, -100)]
    for sx, sy in background_stones:
        cemetery.penup()
        cemetery.goto(sx, sy)
        cemetery.color("#2c3e50")
        cemetery.begin_fill()
        for _ in range(2):
            cemetery.forward(40)
            cemetery.left(90)
            cemetery.forward(60)
            cemetery.left(90)
        cemetery.end_fill()

    # Main Tombstone (April's)
    cemetery.penup()
    cemetery.goto(100, -100)
    cemetery.pendown()
    cemetery.color("#95a5a6", "#7f8c8d") 
    cemetery.begin_fill()
    for _ in range(2):
        cemetery.forward(120)
        cemetery.left(90)
        cemetery.forward(180)
        cemetery.left(90)
    cemetery.end_fill()

    # RIP Text
    cemetery.penup()
    cemetery.goto(160, 20)
    cemetery.color("#2c3e50")
    cemetery.write("April", align="center", font=("Courier", 14, "bold"))
    cemetery.goto(160, -10)
    cemetery.write("2006 - 2025", align="center", font=("Courier", 10, "normal"))
    cemetery.goto(160, -40)
    cemetery.write("Gone but not\nforgotten", align="center", font=("Courier", 8, "italic"))

    # A Blue Rose on the ground (The memory)
    cemetery.penup()
    cemetery.goto(130, -115)
    cemetery.pendown()
    cemetery.color("#1b5e20") # Stem
    cemetery.width(2)
    cemetery.goto(150, -105)
    cemetery.color("blue") # Blue rose petals
    cemetery.dot(10)
    cemetery.width(1)
    # Raphael standing by the grave
    draw_person(cemetery, 50, -130, "blue")  # Raphael standing at the grave
    screen.update()


# Main Setup

screen = turtle.Screen()
screen.setup(1280, 1024)
screen.bgcolor("#87CEEB")
screen.tracer(0) # Smooth animation mode
artist = turtle.Turtle()
artist.hideturtle()
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
tear_artist = turtle.Turtle()
tear_artist.hideturtle()

girl_pos = 450
boy_stop = 410

# --- ACT 1: THE DREAM ---
play_audio("BawatPiyesa.flac")

# Animation: Walking together
for x in range(-200, boy_stop + 1, 7):
    draw_scene(artist, x, girl_pos)
    time.sleep(0.01)

# Hugging sequence and dialogue
draw_scene(artist, girl_pos - 20, girl_pos + 10, rose_owner="girl", hugging=True)
writer.color("black") 
type_talk("Raphael... promise me you won't leave?", girl_pos, 80, 0.07, 2.0)
type_talk("I feel so safe here with you.", girl_pos, 50, 0.07, 2.0)
type_talk("I'm not going anywhere. You're my world.", boy_stop, 20, 0.07, 2.5)
type_talk("I'll spend every day making you happy.", boy_stop, -10, 0.07, 2.5)
type_talk("I love you more than words can say.", boy_stop, -40, 0.07, 3.0)
type_talk("I love you too... I never want this to end.", girl_pos, 80, 0.07, 3.0)
type_talk("Let's go inside and watch a movie while eating?", boy_stop, 80, 0.07, 3.0)
type_talk("Sure! Don't forget my cuddles, I love cuddles!", girl_pos, 80, 0.07, 3.0)

# Animation: Walking towards the house
for x in range(girl_pos, -391, -8):
    draw_scene(artist, x - 20, x + 10, rose_owner="none", hugging=True)
    time.sleep(0.01)

# Transition to darkness
writer.clear()
artist.clear()
screen.bgcolor("black")
screen.update()
writer.color("white") 
type_talk("Everything felt so real...", 0, 0, 0.10, 6.0)
type_talk("But dreams always have an end.", 0, -40, 0.10, 6.4)

play_audio("panaginip.flac") # Change Music

for _ in range(2):
    talk(". . .", 0, 0, 2.0)
    writer.clear()
    time.sleep(1.0)

# --- ACT 2: THE REALITY ---

# Creates a flashing transition effect for waking up
screen.bgcolor("white")
screen.update()
time.sleep(0.1)
screen.bgcolor("black")
screen.update()
time.sleep(0.1)
screen.bgcolor("white")
screen.update()

draw_classroom(artist)
writer.color("black")
time.sleep(5.0)

# Classroom scene: Waking up
draw_classroom(artist)
writer.color("black") 
time.sleep(2.0)
talk("Solis! Gising na!", 0, -180, 3.0)
talk("Daydream ka na naman, tapos na lecture ni sir Jeff.", 0, -180, 4.5)
type_talk("...Huh? Nasaan siya?", 300, -290, 0.10, 2.0)

# Reflection on the breakup
draw_afar_scene(artist)
talk("Ah... right. We broke up months ago.", -300, 50, 3.0)
talk("Akala ko paggising ko, nandito ka pa.", -300, 20, 3.5)
talk("Nakalimutan ko, masaya ka na pala sa iba.", -300, -10, 3.5)
type_talk("Akala ko tayo hanggang dulo...", -300, -40, 0.10, 3.4)
type_talk("Te amo muchísimo...\nhanggang sa muling pagtatagpo ng ating tadhana, aking mahal.", -300, -70, 0.10, 6)
type_talk("Ang hiling ko lang ay sana tratuhin ka na niya ng tama\nat ingatan mo rin ang iyong sarili.", -300, -70, 0.10, 6.0)
type_talk("At sana ingatan ka rin niya at mahalin,\nkagaya ng pagmamahal ko sa iyo...", -300, -70, 0.10, 6.5)
type_talk("Paalam, aking minamahal...", -300, -70, 0.10, 2)

# --- ACT 3: HEARTBREAK ---

writer.color("white")
draw_crying_face(artist)
# Tear animation loop
for i in range(0, 120, 4):
    tear_artist.clear()
    for tx in [-45, 55]:
        tear_artist.penup()
        tear_artist.goto(tx, 0 - i)
        tear_artist.color("#00BFFF")
        tear_artist.begin_fill()
        tear_artist.circle(8)
        tear_artist.end_fill()
        tear_artist.pendown()
        tear_artist.goto(tx, 0)
        tear_artist.penup()
        tear_artist.goto(tx + 3, -i + 2)
        tear_artist.color("white")
        tear_artist.dot(3)
    if i == 0:
        writer.goto(0, 240)
        writer.write("This is my final gift of love: letting you go.", align="center", font=("Arial", 11, "bold italic"))
    screen.update()
    time.sleep(0.04)

# Dialogue for moving on
type_talk("I'd rather see you truly happy in his arms...", 0, 210, 0.07, 3.0)
type_talk("Than watch you faking a smile while your eyes betray the sadness inside.", 0, 180, 0.07, 5.4)
type_talk("Mas mainam nalang na manatiling tulog na masaya", 0, -220, 0.08, 5.0)
type_talk("Kesa sa magising sa mundong puno ng poot at pighati..", 0, -250, 0.07, 5.7)
type_talk("May mga kwentong hanggang panaginip lang talaga.", 0, -280, 0.08, 4.0)
type_talk("Wala na siya... may final exam pa akong ite-take.", 0, -310, 0.09, 5.0)

# --- ACT 4: HOMECOMING & REGRET ---

screen.bgcolor("black")
writer.clear()
artist.clear()
tear_artist.clear()
screen.update()
time.sleep(2.0)

# Night city scene: Loneliness
draw_afar_scene(artist, hide_others=True, is_night=True)
writer.color("white")
talk("Pag-uwi ko, ang bigat pa rin ng pakiramdam ko.", 0, 160, 3.4)
talk("Bawat kanto na nilalakaran ko, may alaala nating dalawa.", 0, 160, 4.9)
talk("Dati, sabay pa tayong naglalakad pauwi habang nagtatawanan.", 0, 160, 4.0)
talk("Ngayon, anino ko nalang ang kasabay ko sa ilalim ng mga poste.", 0, 160, 4.5)
talk("Kay lamig ng hangin, pero mas malamig ang katotohanang wala ka na.", 0, 160, 5.0)
talk("Tanging tunog nalang ng sarili kong mga hakbang ang naririnig ko.", 0, 160, 4.0)

# Bedroom scene: Late night thoughts
draw_bedroom(artist)
draw_person(artist, -150, -20, "blue", is_laying=True) 
writer.color("white")
type_talk("Nakahiga na ako, pero hindi ako dalawin ng antok.", 0, 240, 0.07, 3.0)
type_talk("Iniisip ko... saan ba ako nagkamali?", 0, 210, 0.07, 3.0)
type_talk("Ano ba ang meron sa kanya na wala sa akin?", 0, 180, 0.08, 3.5)
type_talk("Wala lang ba sa'yo ang pinagsamahan natin...", 0, 150, 0.08, 3.5)
type_talk("...na ang bilis mo akong ipagpalit sa iba?", 0, 120, 0.08, 4.0)
type_talk("Ganoon ba ako kadaling kalimutan?", 0, 90, 0.08, 3.5)
type_talk("Habang ako, pilit pa ring binubuo ang sarili ko...", 0, 60, 0.08, 3.5)
type_talk("...mula sa mga piyesang iniwan mo.", 0, 60, 0.08, 4.0)
type_talk("If I stayed that night, would things be different?", 0, 90, 0.08, 4.0)
type_talk("If I focused on 'us' more than my pride...", 0, 60, 0.08, 4.0)
talk("Maybe 'I love you' wasn't enough.", 0, -180, 4.0)
talk("Maybe I was just a chapter, while you were my whole book.", 0, -210, 4.0)
talk("Ang dami kong regrets... ang daming 'Sana'.", 0, -240, 5.0)
talk("Sana hindi nalang tayo nagtagpo, kung iiwan mo lang din pala ako.", 0, -270, 5.0)
time.sleep(3.0)

# --- THE FINAL REVELATION: THE AWAKENING ---
screen.bgcolor("black")
writer.clear()
artist.clear()
screen.update()
time.sleep(2.0)

# Back in the bedroom - The Parents' voices enter
draw_bedroom(artist)
draw_person(artist, -150, -20, "blue", is_laying=True) 
writer.color("white")

talk("Anak? Raphael? Gising na, tanghali na.", 0, 240, 3.5)
talk("Ma... Pa... Bakit po kayo nandito?", -150, -50, 3.0)
talk("Kanina pa kami kumakatok. Umiiyak ka na naman sa tulog mo.", 0, 210, 4.0)
talk("Nanaginip po ako... tungkol sa school. Kasama ko po si April.", -150, -50, 4.0)

# The Confrontation - Pitch changes to serious
writer.color("#FF6347") # A slightly reddish white to show tension
talk("Raphael, makinig ka sa amin nang maigi...", 0, 150, 4.0)
talk("Wala na si April. Isang taon na ang nakakalipas.", 0, 120, 5.0)
talk("Hindi mo na siya maibabalik kahit sa panaginip mo.", 0, 90, 4.5)

# The Denial
writer.color("white")
type_talk("...Hindi. Hindi totoo 'yan. Kanina lang, nagtatawanan pa kami.", -150, -50, 0.08, 4.0)
talk("Maging totoo ka sa sarili mo, anak. Alam mo kung ano ang nangyari.", 0, 240, 4.5)


# THE CRASH FLASHBACK (Visual Trauma)
os.system("pkill mpv") # Silence before the crash
time.sleep(1.0)
# 1. Clear the bedroom shapes and set background to white
artist.clear() 
screen.bgcolor("white")
screen.update()
time.sleep(0.05)

# 2. Set background to red for the impact
screen.bgcolor("red")
screen.update()
time.sleep(0.1)

# 3. Complete blackout
screen.bgcolor("black")
screen.update()
# Memory dialogue over black screen
talk("Lasing ka noon, Raphael. Pinipilit mong mag-drive.", 0, 50, 4.5)
talk("'Raphael, pakiusap... huminto ka na. Lasing ka na, hindi na tayo ligtas.'", 0, 20, 5.0)
talk("Pero ang lakas ng loob mo. Sabi mo, 'Kaya ko 'to.'", 0, -10, 4.0)
talk("Isang malakas na busina... ang nakakasilaw na ilaw ng truck...", 0, -40, 4.5)
talk("Sa isang iglap, ikaw ang nabuhay... pero siya ang nawala.", 0, -70, 6.0)
play_audio("SaSusunodNaHabangBuhay.flac")

# THE CEMETERY: REALITY SETS IN
draw_cemetery(artist)
writer.color("white")
type_talk("Patawad, mhie... sana ako nalang ang kinuha.", 0, 240, 0.07, 4.0)
type_talk("Ang huling naramdaman mo ay takot, dahil sa akin.", 0, 210, 0.08, 4.5)
type_talk("Binigay ko sa'yo ay wakas, imbes na kinabukasan.", 0, 180, 0.08, 4.5)
type_talk("Araw-araw kong pagsisihan na hindi ako nakinig sa'yo.", 0, 150, 0.08, 4.0)
type_talk("Hihintayin ko ang araw na mapapatawad mo ako...", 0, 120, 0.08, 4.0)
type_talk("...kahit alam kong hinding-hindi ko na mapapatawad ang sarili ko.", 0, 90, 0.10, 6.0)

# ANIMATED HEARTBREAK FACE 
writer.color("white")
draw_crying_face(artist)
for i in range(0, 150, 3): # Slower, heavier tears
    tear_artist.clear()
    for tx in [-45, 55]:
        tear_artist.penup()
        tear_artist.goto(tx, 0 - i)
        tear_artist.color("#00BFFF")
        tear_artist.begin_fill()
        tear_artist.circle(8)
        tear_artist.end_fill()
        tear_artist.pendown()
        tear_artist.goto(tx, 0)
        tear_artist.penup()
        tear_artist.goto(tx + 3, -i + 2)
        tear_artist.color("white")
        tear_artist.dot(3)
    if i == 0:
        writer.goto(0, 240)
        writer.write("This is my lifetime debt of regret.", align="center", font=("Arial", 11, "bold italic"))
    screen.update()
    time.sleep(0.08)

time.sleep(5.0)

# --- ACT 5: FINAL CREDITS ---

screen.bgcolor("black")
writer.clear()
artist.clear()
tear_artist.clear()
screen.update()
time.sleep(1.0)
writer.color("white")
talk("Ang buhay ay weather-weather lang...", 0, 80, 4.5)
talk("Sabi ko pa noon, magiging asawa mo ako…", 0, 40, 5.0)
talk("Pero sabi ng tadhana, 'Heck nawhh.'", 0, 0, 4.8)
type_talk("Some dreams are only meant to stay dreams.", 0, -40, 0.05, 10.0)


# Heartfelt closing thoughts
talk("Akala ko ikaw na ang huling piyesa ng buhay ko.", 0, 0, 6.5)
talk("Pero naging bahagi ka lang pala ng isang magandang alaala.", 0, -40, 6.3)
talk("Salamat sa sandaling panahong naramdaman kong akin ka.", 0, -80, 6.7)

# Animated message sequences
PostEnd = "Hindi man tayo nagkatuluyan hanggang dulo, masaya naman ako at nakilala kita."
display_text = ""
for char in PostEnd:
    display_text += char
    writer.clear()
    writer.goto(0, -80)
    writer.write(display_text, align="center", font=("Arial", 15, "bold italic"))
    screen.update()
    time.sleep(0.09)
    
End = "Salamat sa maliligayang alaala at sa mga life lesson na naibigay mo sa akin."
display_text = ""
for char in End:
    display_text += char
    writer.clear()
    writer.goto(0, -80)
    writer.write(display_text, align="center", font=("Arial", 15, "bold italic"))
    screen.update()
    time.sleep(0.09)

# Project and dedication credits
current_credits = "Project by: Raphael Solis | BSIS 1-04"
display_text = ""
for char in current_credits:
    display_text += char
    writer.clear()
    writer.goto(0, -80)
    writer.write(display_text, align="center", font=("Arial", 15, "bold italic"))
    screen.update()
    time.sleep(0.08)

dedication_text = "Thank you for being our teacher in this school year, Sir Jeff!"
full_display = display_text + "\n\n"
for char in dedication_text:
    full_display += char
    writer.clear()
    writer.goto(0, -80)
    writer.write(full_display, align="center", font=("Arial", 15, "bold italic"))
    screen.update()
    time.sleep(0.09)

time.sleep(2.0)

# Final Special Thanks screen
writer.clear()
writer.goto(0, 120)
writer.color("white")
writer.write("SPECIAL THANKS TO:", align="center", font=("Arial", 14, "bold underline"))

writer.goto(0, 70)
writer.write("Arabella Mendoza", align="center", font=("Arial", 12, "bold"))
writer.goto(0, 50)
writer.write("The one who inspired the 'Dream' scene.", align="center", font=("Arial", 10, "italic"))

writer.goto(0, 10)
writer.write("To my friends,", align="center", font=("Arial", 12, "bold"))
writer.goto(0, -10)
writer.write("For always being there and keeping me sane.", align="center", font=("Arial", 10, "italic"))

writer.goto(0, -50)
writer.color("cyan")
writer.write("To the classmate in the front row,", align="center", font=("Arial", 11, "bold"))
writer.goto(0, -70)
writer.write("Thanks for waking me up. Reality is hard, but lessons are harder.", align="center", font=("Arial", 10, "italic"))

writer.goto(0, -120)
writer.color("white")
writer.write("And to my parents for supporting me!", align="center", font=("Arial", 10, "normal"))

screen.update()
time.sleep(6.0)

# Roles & Final Dedications
writer.clear()
writer.goto(0, 80)
writer.color("white")
writer.write("Director & Lead Programmer: Raphael Solis", align="center", font=("Arial", 11, "bold"))

writer.goto(0, 50)
writer.write("Story & Narrative Design: Raphael Solis", align="center", font=("Arial", 11, "bold"))

writer.goto(0, 20)
writer.write("Graphical Assets: Raphael Solis", align="center", font=("Arial", 11, "bold"))

writer.goto(0, -30)
writer.color("pink")
writer.write("Inspiration: Parents, Dreams, and a little bit of Heartbreak.", align="center", font=("Arial", 12, "italic"))

writer.goto(0, -80)
writer.color("yellow")
writer.write("Thanks God to be the glory.", align="center", font=("Arial", 13, "bold"))

screen.update()
time.sleep(8.0)

# Final Exit Thought
writer.clear()
writer.goto(0, 0)
writer.color("gray")
type_talk("End of Project.", 0, 0, 0.1, 2.0)

writer.goto(0, -40)
writer.write("Moving on... but checking the code one last time.", align="center", font=("Arial", 25, "italic"))

screen.update()
time.sleep(7.0)
    
screen.mainloop()