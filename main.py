import pygame
from pygame.locals import *
import os


class Game():
    def __init__(self):
        self.tilstand = 0
        self.menu_element = "start"
        self.screen_width=1280
        self.screen_height=720
        self.screen=pygame.display.set_mode((self.screen_width, self.screen_height))
        self.clock = pygame.time.Clock()
        self.FPS=30

class Treasure():
    def __init__(self):
        self.health = 100


class Collisionbox():
    def __init__(self):
        pass


class Player():
    def __init__(self):
        self.walkRight = [pygame.image.load('player/R1.png'), pygame.image.load('player/R2.png'), pygame.image.load('player/R3.png'), pygame.image.load('player/R4.png'), pygame.image.load('player/R5.png'), pygame.image.load('player/R6.png'), pygame.image.load('player/R7.png'), pygame.image.load('player/R8.png'), pygame.image.load('player/R9.png')]
        self.walkLeft = [pygame.image.load('player/L1.png'), pygame.image.load('player/L2.png'), pygame.image.load('player/L3.png'), pygame.image.load('player/L4.png'), pygame.image.load('player/L5.png'), pygame.image.load('player/L6.png'), pygame.image.load('player/L7.png'), pygame.image.load('player/L8.png'), pygame.image.load('player/L9.png')]
        self.character = pygame.image.load('player/standing.png')


        self.health = 100
        self.vel = 5
        self.vel2 = 4
        self.x = 0
        self.y = 640

        self.isJump = False
        self.jumpCount = 10
        self.left=False
        self.right=False
        self.walkCount=0


    def player_creation(self):
        self.keys = pygame.key.get_pressed()

        if self.keys[pygame.K_LEFT] :
            player.x-= player.vel
            player.left=True
            player.right=False

        elif self.keys[pygame.K_RIGHT]:
            player.x+= player.vel
            player.left=False
            player.right=True
        else:
            player.left=False
            player.right=False
            player.walkCount = 0


        if not(player.isJump):
            if self.keys[pygame.K_SPACE]:
                player.isJump = True
                player.left=False
                player.right=False
                player.walkCount = 0
        else:
            if player.jumpCount >= -10:
                self.neg = 1
                if self.jumpCount < 0:
                    self.neg = -1
                player.y -= (player.jumpCount**2)*0.2*self.neg
                player.jumpCount -= 1
            else:
                player.isJump = False
                player.jumpCount = 10

    def player_draw(self):
        if player.walkCount +1 >= 27:
            player.walkCount = 0
        if player.left:
            game.screen.blit(self.walkLeft[self.walkCount//3],  (self.x,self.y))
            player.walkCount += 1
        elif player.right:
            game.screen.blit(self.walkRight[self.walkCount//3], (self.x,self.y))
            player.walkCount += 1
        else:
            game.screen.blit(self.character,  (self.x,self.y))
            print(self.y)





game=Game()
treasure=Treasure()
collisionbox = Collisionbox()
player=Player()


done=False
# Game Initialization
pygame.init()



asd = pygame.mouse.get_pos()
print(asd)
# Center the Game Application
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Game Resolution

bg22 = pygame.image.load("Pictures\Menu_wallpaper.png")
map = pygame.image.load("Pictures\map(2).png")

# Text Renderer
def text_format(message, textFont, textSize, textColor):
    newFont=pygame.font.Font(textFont, textSize)
    newText=newFont.render(message, 0, textColor)

    return newText


# Farver
white=(255, 255, 255)
black=(0, 0, 0)
gray=(50, 50, 50)
red=(255, 0, 0)
green=(0, 255, 0)
blue=(0, 0, 255)
yellow=(255, 255, 0)

# Game Fonts
font = "Retro.ttf"


# Game Framerate


# Main Menu
def main_menu(game):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                game.menu_element="start"
            elif event.key==pygame.K_DOWN:
                game.menu_element="quit"
            if event.key==pygame.K_RETURN:
                if game.menu_element=="start":
                    game.tilstand=1
                if game.menu_element=="quit":
                    pygame.quit()
                    quit()

        # Main Menu UI
        game.screen.blit(bg22,(0,0))

        if game.menu_element=="start":
            text_start=text_format("START", font, 75, white)
        else:
            text_start = text_format("START", font, 75, black)
        if game.menu_element=="quit":
            text_quit=text_format("QUIT", font, 75, white)
        else:
            text_quit = text_format("QUIT", font, 75, black)


        start_rect=text_start.get_rect()
        quit_rect=text_quit.get_rect()

        # Main Menu Text

        game.screen.blit(text_start, (game.screen_width/2 - (start_rect[2]/2), 300))
        game.screen.blit(text_quit, (game.screen_width/2 - (quit_rect[2]/2), 360))
        pygame.display.update()


def draw_game(game):

    pygame.event.pump()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            print(pygame.mouse.get_pos())




    game.screen.blit(map,(0,0))
    #Platform


#MOvement

    if player.x < 305 and player.x > 280 and player.keys[pygame.K_UP]:
        player.y -= player.vel
    if player.x < 305 and player.x > 280 and player.keys[pygame.K_DOWN]:
        player.y += player.vel
    if player.y < 415:
        player.y = 410
    if player.y > 640:
        player.y = 640


    player.player_creation()
    player.player_draw()

    pygame.display.update()


while not done:
    if game.tilstand==0:
        main_menu(game)
    if game.tilstand==1:
        draw_game(game)





#Initialize the Game

self.clock.tick(self.FPS)
main_menu()
pygame.quit()
quit()
