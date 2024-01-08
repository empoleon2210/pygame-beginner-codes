import random
WIDTH = 500
HEIGHT = 500
score = 0
game_over = False
fox = Actor('fox')
fox.pos = 100, 100

coin = Actor('coin')
coin.pos  = 200, 200
def draw():
    screen.fill('Green')
    fox.draw()
    coin.draw()
    screen.draw.text('Score: ' + str(score), color = 'black', topleft = (10,10))

    if game_over:
        screen.fill('Pink')
        screen.draw.text('Final Score: ' + str(score), color = 'white', topleft = (10,10), fontsize =60)
def place_coin():
    coin.x = random.randint(20, WIDTH)
    coin.y = random.randint(20, HEIGHT)

def time_up():
    global game_over
    game_over = True
def update():
    global score

    if keyboard.left:
        fox.x = fox.x-5
    elif keyboard.right:
        fox.x = fox.x +5
    elif keyboard.up:
        fox.y = fox.y -5
    elif keyboard.down:
        fox.y = fox.y+5
    
    coin_collected = fox.colliderect(coin)
    if coin_collected:
        
        score += 10
        place_coin()
clock.schedule(time_up, 5)
place_coin()