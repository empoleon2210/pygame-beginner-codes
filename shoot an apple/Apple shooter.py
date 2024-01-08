import random
apple = Actor('apple')
WIDTH = 400
HEIGHT = 400
def draw():
    screen.clear #clears the screen don't know the functionality yet
    apple.draw()
def place_apple():
    apple.x = random.randint(0,400)
    apple.y = random.randint(0,400)
def on_mouse_down(pos):
    if apple.collidepoint(pos):
        print('Good Shot!')
        place_apple()
    else:
        print('You missed!')
        print('Loser')
        quit()
place_apple()