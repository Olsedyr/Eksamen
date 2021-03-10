import pygame
from pygame.locals import *
import os

class Game():
    def __init__(self):
        self.tilstand = 0
        self.menu_element = "start"


game=Game()


done=False
# Game Initialization
pygame.init()

# Center the Game Application
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Game Resolution
screen_width=1280
screen_height=720
screen=pygame.display.set_mode((screen_width, screen_height))
bg = pygame.image.load("Pictures\Menu_wallpaper.png")

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
clock = pygame.time.Clock()
FPS=30

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
        screen.blit(bg,(0,0))

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

        screen.blit(text_start, (screen_width/2 - (start_rect[2]/2), 300))
        screen.blit(text_quit, (screen_width/2 - (quit_rect[2]/2), 360))
        pygame.display.update()


def draw_game(game):
    pygame.event.pump()
    screen.fill(white)
    pygame.display.update()


while not done:
    if game.tilstand==0:
        main_menu(game)
    if game.tilstand==1:
        draw_game(game)




#Initialize the Game
clock.tick(FPS)
main_menu()
pygame.quit()
quit()
