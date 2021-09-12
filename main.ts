let Sprites = sprites.create(assets.image`player`, SpriteKind.Player)
tiles.setTilemap(tilemap`level1`)
let Ai = sprites.create(assets.image`Ai`, SpriteKind.Enemy)
scene.cameraFollowSprite(Ai)
tiles.placeOnRandomTile(Sprites, assets.tile`block`)
tiles.placeOnRandomTile(Ai, assets.tile`black`)
Ai.say("Calculate 1 number from 0 to 100.")
pause(5000)
let a = 100
let b = 0
let c = 1
let x = randint(b, a + 1)
Ai.say(x)
controller.up.onEvent(ControllerButtonEvent.Pressed, function on_event_pressed() {
    
    a = x - 1
    x = randint(b, a + 1)
    Ai.say(x)
    c = c + 1
})
controller.down.onEvent(ControllerButtonEvent.Pressed, function on_event_pressed1() {
    
    b = x + 1
    x = randint(b, a + 1)
    Ai.say(x)
    c = c + 1
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function on_event_pressed2() {
    
    Ai.say(c)
    pause(1000)
    game.over(true)
})
