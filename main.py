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
        self.x = 50
        self.y = 450
        self.isJump = False
        self.jumpCount = 10
        self.left=False
        self.right=False
        self.walkCount=0


    def player_creation(self):
        self.keys = pygame.key.get_pressed()

        if self.keys[pygame.K_LEFT] and self.x > self.vel:
            self.x-= self.vel
            self.left=True
            self.right=False

        elif self.keys[pygame.K_RIGHT] and self.x < 500-self.screen_width:
            self.x+= self.vel
            self.left=False
            self.right=True
        else:
            self.left=False
            self.right=False
            self.walkCount = 0


        if not(self.isJump):
            if self.keys[pygame.K_SPACE]:
                self.isJump = True
                self.left=False
                self.right=False
                self.walkCount = 0
        else:
            if self.jumpCount >= -10:
                self.neg = 1
                if self.jumpCount < 0:
                    self.neg = -1
                self.y -= (self.jumpCount**2)*0.5*self.neg
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = 10

        def player_draw(self):
            if self.walkCount +1 >= 27:
                self.walkCount = 0
            if self.left:
                self.screen.blit(self.walkLeft[self.walkCount//3],  (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                self.screen.blit(self.walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            else:
                self.screen.blit(self.character,  (self.x,self.y))

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
    pygame.draw.rect(game.screen, white, pygame.Rect(300,470,475,10))

    #floor
    pygame.draw.rect(game.screen, white, pygame.Rect(0,705,1280,10))


    game.player_draw()

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
