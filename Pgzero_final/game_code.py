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
    # les mouvements de la rocket et navette spaciale
    global ship
    if (keyboard.left):
        ship.x -= 2
        rocket_fire.x -= 2
    elif (keyboard.right):
        ship.x += 2
        rocket_fire.x += 2
    elif keyboard.space :
        animate( rocket_fire, pos = (ship.x, 0))
        screen.clear()
    elif keyboard.r:
        rocket_fire.pos = (ship.x, ship.y)
        
def move_alien():
    # mouvement de l'alien et verifier si la rocket a touche l'alien
    
    alien.right += 2
    if alien.left > WIDTH:
        alien.right = 0
    
    collide = rocket_fire.colliderect(alien)
    
    if collide == 0:
        print("missed me")
        alien.image = 'alien'
    elif collide == 1:
        alien.image = "pi"
    

def update():
    draw()
    rocket_movement()
    move_alien()
    
pgzrun.go()