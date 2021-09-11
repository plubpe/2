let Sprites = sprites.create(assets.image`player`, SpriteKind.Player)
tiles.setTilemap(tilemap`level1`)
let Ai = sprites.create(assets.image`Ai`, SpriteKind.Enemy)
scene.cameraFollowSprite(Ai)
tiles.placeOnRandomTile(Sprites, assets.tile`block`)
tiles.placeOnRandomTile(Ai, assets.tile`black`)
Ai.say("Calculate 1 number from 0 to 100.")
pause(5000)
let x = 50
Ai.say(x)
let a = 49
let d = 0
let c = 0
let b = 1
let g = 0
controller.up.onEvent(ControllerButtonEvent.Pressed, function on_event_pressed() {
    
    if (b == 1) {
        x = randint(0, 49)
        Ai.say(x)
        a = x
    }
    
})
controller.down.onEvent(ControllerButtonEvent.Pressed, function on_event_pressed1() {
    
    if (b == 1) {
        x = randint(51, 100)
        Ai.say(x)
        c = x
    }
    
})
// def on_event_pressed():
// global b,a,x,c,d
// if b==1:
// x = randint(0, a)  
// Ai.say(x)
// a=x
// else :
// x = randint(c,d)
// Ai.say(x)
// d=c
// Sprites.say(d)
// a=x
// if x > 100:
// x = 100
// Ai.say(x)
// b = b+1
// controller.up.on_event(ControllerButtonEvent.PRESSED, on_event_pressed)
// def on_event_pressed1():
// global b,a,x,c,d,g
// if b==1:
// c=51
// x = randint(c, 100)
// Ai.say(x)
// elif x < d:
// g = randint(1, 10)
// x = x+g
// Ai.say(x)
// c=x
// elif x > 100:
// x = 100
// Ai.say(x)
// b = b+1
// controller.down.on_event(ControllerButtonEvent.PRESSED, on_event_pressed1)
controller.A.onEvent(ControllerButtonEvent.Pressed, function on_event_pressed2() {
    Ai.say(b)
    pause(500)
    game.over(true)
})
