import pgzrun

WIDTH = 1000
HEIGHT = 500

ship = Actor('ship' , ( 500, 400))
rocket_fire = Actor('rocket_fire', (500, 400))
alien = Actor('alien' , center = (100, 100))

def draw():
    screen.clear()
    screen.blit('space_back' , (0,0))
    ship.draw()
    rocket_fire.draw()
    alien.draw()
    
def rocket_movement():
    global ship
    if (keyboard.left):
        ship.x -= 2
        rocket_fire.x -= 2
