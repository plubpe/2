Sprites = sprites.create(assets.image("""player"""), SpriteKind.player)
tiles.set_tilemap(tilemap("""level1"""))
Ai = sprites.create(assets.image("""Ai"""), SpriteKind.enemy)
scene.camera_follow_sprite(Ai)
tiles.place_on_random_tile(Sprites,assets.tile("""block"""))
tiles.place_on_random_tile(Ai,assets.tile("""black"""))
Ai.say("Calculate 1 number from 0 to 100.")
pause(5000)
a = 100
b = 0
c = 1
x = randint(b, a+1)
Ai.say(x)

def on_event_pressed():
    global a,b,c,x
    a=x-1
    x = randint(b, a+1)
    Ai.say(x)
    c=c+1
controller.up.on_event(ControllerButtonEvent.PRESSED, on_event_pressed)

def on_event_pressed1():
    global a,b,c,x
    b=x+1
    x = randint(b, a+1)
    Ai.say(x)
    c=c+1
controller.down.on_event(ControllerButtonEvent.PRESSED, on_event_pressed1)

def on_event_pressed2():
    global c
    Ai.say(c)
    pause(1000)
    game.over(True)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_event_pressed2)

#def on_event_pressed():
    #global b,a,x,c,d
    #if b==1:
        #x = randint(0, 49)
        #Ai.say(x)
        #a=x
    #elif x < 49:
        #x = randint(c, a)
        #Ai.say(x)
        #c=x
    #elif c > 49:
        #x = randint(c, a)
        #Ai.say(x)
        #c=x
    #elif a == 25:
        #x = randint(c, a)
        #Ai.say(x)
        #c=x
    #b=b+1
#controller.up.on_event(ControllerButtonEvent.PRESSED, on_event_pressed)

#def on_event_pressed1():
    #global b,a,x,c,d
    #if b==1:
        #x = randint(51, 100)
        #Ai.say(x)
        #c=x
        #a=100
    #elif x < 100:
        #x = randint(c, a) 
        #Ai.say(x)
        #c=x
    #elif a < 49:
        #x = randint(c, a)
        #Ai.say(x)
        #a=x
    #elif c == 75:
        #x = randint(c, a)
        #Ai.say(x)
        #a=x
    #b=b+1
#controller.down.on_event(ControllerButtonEvent.PRESSED, on_event_pressed1)

#def on_event_pressed():
    #global b,a,x,c,d
    #if b==1:
        #x = randint(0, a)  
        #Ai.say(x)
        #a=x
    #else :
        #x = randint(c,d)
        #Ai.say(x)
        #d=c
        #Sprites.say(d)
        #a=x
        #if x > 100:
            #x = 100
            #Ai.say(x)
    #b = b+1
#controller.up.on_event(ControllerButtonEvent.PRESSED, on_event_pressed)

#def on_event_pressed1():
    #global b,a,x,c,d,g
    #if b==1:
        #c=51
        #x = randint(c, 100)
        #Ai.say(x)
    #elif x < d:
        #g = randint(1, 10)
        #x = x+g
        #Ai.say(x)
        #c=x
    #elif x > 100:
        #x = 100
        #Ai.say(x)
    #b = b+1
#controller.down.on_event(ControllerButtonEvent.PRESSED, on_event_pressed1)
