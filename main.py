Sprites = sprites.create(assets.image("""player"""), SpriteKind.player)
tiles.set_tilemap(tilemap("""level1"""))
Ai = sprites.create(assets.image("""Ai"""), SpriteKind.enemy)
scene.camera_follow_sprite(Ai)
tiles.place_on_random_tile(Sprites,assets.tile("""block"""))
tiles.place_on_random_tile(Ai,assets.tile("""black"""))
Ai.say("Calculate 1 number from 0 to 100.")
pause(5000)
x = 50
Ai.say(x)
a = 49
d = 0
c = 0
b = 1
g = 0

def on_event_pressed():
    global b,a,x,c,d
    if b==1:
        x = randint(0, a)  #0,49,0,38,0,25
        Ai.say(x)
        a=x
    else :
        x = randint(c,d)
        Ai.say(x)
        d=c
        Sprites.say(d)
        a=x
        if x > 100:
            x = 100
            Ai.say(x)
    b = b+1
controller.up.on_event(ControllerButtonEvent.PRESSED, on_event_pressed)

def on_event_pressed1():
    global b,a,x,c,d,g
    if b==1:
        c=51
        x = randint(c, 100)
        Ai.say(x)
    elif x < d:
        g = randint(1, 10)
        x = x+g
        Ai.say(x)
        c=x
    elif x > 100:
        x = 100
        Ai.say(x)
    b = b+1
controller.down.on_event(ControllerButtonEvent.PRESSED, on_event_pressed1)

def on_event_pressed2():
    Ai.say(b)
    pause(500)
    game.over(True)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_event_pressed2)