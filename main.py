import pygame
import os
import threading
import time



class Game():
    def __init__(self):
        self.tilstand = 0
        self.menu_element = "start"
        self.screen_width=1280
        self.screen_height=720
        self.screen=pygame.display.set_mode((self.screen_width, self.screen_height))
        self.clock = pygame.time.Clock()
        self.FPS=30
        self.highscore = 0
        self.thread = myThread(0.1)
        self.thread.start()
        self.player_bullets=[]
        self.ammo = 90
        self.level = 0
        self.zombieque = 0
        self.enemy_list = []
        self.spawner_cooldown = 0
    #    self.enemy2_bullets=[]


    def zombie_spawner(self):
        if len(self.enemy_list) == 0:
            self.level += 1
            self.zombieque = self.level*2


        if self.zombieque > 0 and self.spawner_cooldown == 0:
            self.enemy_list.append(Enemy1())
            self.zombieque -= 1
            self.spawner_cooldown = 27
        elif self.spawner_cooldown > 0:
            self.spawner_cooldown -= 1




class Treasure():
    def __init__(self):
        self.health = 1000



class Healing():
    def __init__(self):
        self.healing = 20
        self.times = 5
        self.healingtimes = True

class Bullets():
    def __init__(self, x=2, y=2, right=True):
        self.y = y+15
        self.damage = 15
        self.radius = 16
        if right==True:
            self.speed = 10
            self.x = x+35
        else:
            self.speed = -10
            self.x = x

    def update(self):
        self.x += self.speed

    def new_player_bullet(game, player):
        if len(game.player_bullets) > 8 or game.ammo == 0:
            pass
        else:
            game.player_bullets.append(Bullets(x=player.x, y=player.y, right=player.right))
            game.ammo -=1


    # def new_enemy2_bullet(game, enemy2):
    #     if len(game.enemy2_bullets) > 0:
    #         pass
    #     else:
    #         game.enemy2_bullets.append(Bullets(x=enemy2.x, y=enemy2.y))
    #



class Enemy1():
    def __init__(self):
        self.walkRight = [pygame.image.load('enemies/R1E.png'), pygame.image.load('enemies/R2E.png'), pygame.image.load('enemies/R3E.png'), pygame.image.load('enemies/R4E.png'), pygame.image.load('enemies/R5E.png'), pygame.image.load('enemies/R6E.png'), pygame.image.load('enemies/R7E.png'), pygame.image.load('enemies/R8E.png'), pygame.image.load('enemies/R9E.png'), pygame.image.load('enemies/R10E.png'), pygame.image.load('enemies/R11E.png')]
        self.walkLeft = [pygame.image.load('enemies/L1E.png'), pygame.image.load('enemies/L2E.png'), pygame.image.load('enemies/L3E.png'), pygame.image.load('enemies/L4E.png'), pygame.image.load('enemies/L5E.png'), pygame.image.load('enemies/L6E.png'), pygame.image.load('enemies/L7E.png'), pygame.image.load('enemies/L8E.png'), pygame.image.load('enemies/L9E.png'), pygame.image.load('enemies/L10E.png'), pygame.image.load('enemies/L11E.png')]
        self.x = 0
        self.y = 645
        self.width = 32
        self.height = 32
        self.path = [self.x, 601]  # Her bestemmer jeg hvor fjenden starter og slutter
        self.walkCount = 0
        self.hitCount = 0
        self.vel = 1
        self.hit=False
        self.health = 50
        self.visible = True
        self.hitbox = (self.x + 17, self.y + 2, 31, 57) #hitbox





    def draw_enemy1(self):
        self.update()
        if self.visible:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0

            if self.vel > 0:
                game.screen.blit(self.walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            else:
                game.screen.blit(self.walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1


#Tegner healthbar
            pygame.draw.rect(game.screen, (0,255,0), (self.hitbox[0], self.hitbox[1] - 20, self.health, 10))

            self.hitbox = (self.x + 10, self.y + 2, 31, 57)

            #pygame.draw.rect(game.screen, (255,0,0), self.hitbox,2) Tegn hitbox


    def update(self):
        if self.vel > 0:
            if self.x < self.path[1] + self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
        else:
            if self.x > self.path[0] - self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0

            if self.hitCount +1 >= 12:
                self.hitCount = 0

            if self.x == 600:
                self.vel=0
                self.hitCount+=1
                self.hit=True

            if self.x==600 and self.hit==True and self.walkCount==6:
                treasure.health -=5







# class Enemy2():
#
#     def __init__(self):
#         self.walkRight = [pygame.image.load('enemies/R1E.png'), pygame.image.load('enemies/R2E.png'), pygame.image.load('enemies/R3E.png'), pygame.image.load('enemies/R4E.png'), pygame.image.load('enemies/R5E.png'), pygame.image.load('enemies/R6E.png'), pygame.image.load('enemies/R7E.png'), pygame.image.load('enemies/R8E.png'), pygame.image.load('enemies/R9E.png'), pygame.image.load('enemies/R10E.png'), pygame.image.load('enemies/R11E.png')]
#         self.walkLeft = [pygame.image.load('enemies/L1E.png'), pygame.image.load('enemies/L2E.png'), pygame.image.load('enemies/L3E.png'), pygame.image.load('enemies/L4E.png'), pygame.image.load('enemies/L5E.png'), pygame.image.load('enemies/L6E.png'), pygame.image.load('enemies/L7E.png'), pygame.image.load('enemies/L8E.png'), pygame.image.load('enemies/L9E.png'), pygame.image.load('enemies/L10E.png'), pygame.image.load('enemies/L11E.png')]
#         self.attack = [pygame.image.load('enemies/R8E.png'), pygame.image.load('enemies/R9E.png'), pygame.image.load('enemies/R10E.png'), pygame.image.load('enemies/R11E.png')]
#         self.brain= pygame.image.load('pictures/brain.png')
#         self.brain= pygame.transform.scale(self.brain, (18, 22))
#         self.x = 0
#         self.y = 645
#         self.width = 32
#         self.height = 32
#         self.path = [self.x, 0]  # Her bestemmer jeg hvor fjenden starter og slutter
#         self.walkCount = 0
#         self.hitCount = 0
#         self.vel = 3
#         self.hit=False
#         self.health = 50
#
#     # def draw_enemy2(self, game):
#     #
#     #     if self.walkCount + 1 >= 33:
#     #         self.walkCount = 0
#     #
#     #     if self.vel > 0:
#     #         game.screen.blit(self.walkRight[self.walkCount//3], (self.x,self.y))
#     #         self.walkCount += 1
#     #     else:
#     #         game.screen.blit(self.walkLeft[self.walkCount//3], (self.x,self.y))
#     #         self.walkCount += 1
#     #
#     #     #Tjekker om enemy er ved kiste
#     #     if self.hitCount +1 >= 12:
#     #         self.hitCount = 0
#     #
#     #     if self.walkCount==6:
#     #         Bullets.new_enemy2_bullet(game, enemy2)
#
#
#
#
#     def Vector_till_player(self):
#         self.dirvect = pygame.math.Vector2(player.x - enemy.x, player.y - enemy.y)
#


class Player():
    def __init__(self):

        self.walkRight = [pygame.image.load('player/R1.png'), pygame.image.load('player/R2.png'), pygame.image.load('player/R3.png'), pygame.image.load('player/R4.png'), pygame.image.load('player/R5.png'), pygame.image.load('player/R6.png'), pygame.image.load('player/R7.png'), pygame.image.load('player/R8.png'), pygame.image.load('player/R9.png')]
        self.walkLeft = [pygame.image.load('player/L1.png'), pygame.image.load('player/L2.png'), pygame.image.load('player/L3.png'), pygame.image.load('player/L4.png'), pygame.image.load('player/L5.png'), pygame.image.load('player/L6.png'), pygame.image.load('player/L7.png'), pygame.image.load('player/L8.png'), pygame.image.load('player/L9.png')]
        self.character = pygame.image.load('player/standing.png')

        self.attackR = pygame.image.load('player/fireball.png')
        self.attackR = pygame.transform.scale(self.attackR, (32, 36))

        self.attackL = pygame.image.load('player/fireball2.png')
        self.attackL = pygame.transform.scale(self.attackL, (32, 36))

        self.health = 100
        self.vel = 5
        self.vel2 = 1
        self.x = 1200
        self.y = 640

        self.isAttack = False
        self.left=False
        self.right=False
        self.standing=False
        self.walkCount=0


    def player_creation(self):
        self.keys = pygame.key.get_pressed()

        if self.keys[pygame.K_LEFT] :
            player.x-= player.vel
            player.left=True
            player.right=False
            self.standing=False

        elif self.keys[pygame.K_RIGHT]:
            player.x+= player.vel
            player.left=False
            player.right=True
            self.standing=False
        else:
            player.walkCount = 0


        if self.keys[pygame.K_SPACE]:
            Bullets.new_player_bullet(game, player)




    def player_draw(self):
        if player.walkCount +1 >= 27:
            player.walkCount = 0
        if player.left:
            game.screen.blit(self.walkLeft[self.walkCount//3],  (self.x,self.y))
            player.walkCount += 1
        elif player.right:
            game.screen.blit(self.walkRight[self.walkCount//3], (self.x,self.y))
            player.walkCount += 1
        elif player.character:
            game.screen.blit(self.character,  (self.x,self.y))



class myThread (threading.Thread):
   def __init__(self, time):
      threading.Thread.__init__(self)
      self.time = time

   def run(self):
      print (f"Starting timer for {self.time} seconds")
      time.sleep(self.time)
      print("timer complete")






game=Game()
treasure=Treasure()
healing=Healing()
player=Player()
#enemy=Enemy1()
#enemy2=Enemy2()
done=False


# Game Initialization
pygame.init()
dir = os.getcwd()
print("cwd: " + dir)



# Game Initialization
pygame.init()
# Center the Game Application
os.environ['SDL_VIDEO_CENTERED'] = '1'


# Game Resolution
path = os.path.join(dir, "Pictures/Menu_wallpaper.png")
bg22 = pygame.image.load(path)

path2 = os.path.join(dir, "Pictures/map(2).png")
map = pygame.image.load(path2)

path4 = os.path.join(dir, "Pictures/pixel_heart2.png")
heart2 = pygame.image.load(path4)
heart2 = pygame.transform.scale(heart2,(50,50))

path5 = os.path.join(dir, "Pictures/treasure.png")
treasure2 = pygame.image.load(path5)
treasure2 = pygame.transform.scale(treasure2,(75,75))

path6 = os.path.join(dir, "Pictures/kills.png")
kills = pygame.image.load(path6)
kills = pygame.transform.scale(kills,(95,95))

path7 = os.path.join(dir,"Pictures/banner.png")
banner = pygame.image.load(path7)
banner = pygame.transform.scale(banner,(500,100))

path8 = os.path.join(dir,"Pictures/scoreboard.png")
scoreboard = pygame.image.load(path8)
scoreboard = pygame.transform.scale(scoreboard,(200,300))

path9 = os.path.join(dir,"Pictures/bullet.png")
ammo = pygame.image.load(path9)
ammo = pygame.transform.scale(ammo,(72,84))


path10 = os.path.join(dir,"Pictures/ammochest.png")
ammo_chest = pygame.image.load(path10)
ammo_chest = pygame.transform.scale(ammo_chest,(100,86))



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

    newFont2=pygame.font.Font("Retro.ttf", 42)
    newText2=newFont2.render(str(player.health), 0, white)

    newFont3=pygame.font.Font("Retro.ttf", 42)
    newText3=newFont3.render(str(healing.times), 0, white)

    newFont4=pygame.font.Font("Retro.ttf", 42)
    newText4=newFont4.render(str(treasure.health), 0, white)

    newFont5=pygame.font.Font("Retro.ttf", 42)
    newText5=newFont5.render(str(game.highscore), 0, white)

    newFont6=pygame.font.Font("Retro.ttf", 65)
    newText6=newFont6.render(str(game.level), 0, white)

    newFont7=pygame.font.Font("Retro.ttf", 42)
    newText7=newFont7.render(str(game.ammo), 0, white)



    game.screen.blit(map,(0,0))
    game.screen.blit(newText3,(60,60))
    game.screen.blit(heart2, (0,50))
    game.screen.blit(treasure2,(0,120))
    game.screen.blit(newText4, (85,150))
    game.screen.blit(newText5, (85,250))
    game.screen.blit(kills, (-10, 225))
    game.screen.blit(banner, (385, 25))
    game.screen.blit(newText6, (625,45))
    game.screen.blit(scoreboard, (1050,30))
    game.screen.blit(ammo, (25,325))
    game.screen.blit(newText7, (105,365))
    game.screen.blit(ammo_chest, (375,395))

    #Platform
    if treasure.health < 0:
        game.tilstand=2



#Tjekker playerens Health
    if player.health == 0:
        game.tilstand=2






#Tjekker om spilleren går op på stigen
    if player.x < 305 and player.x > 280 and player.keys[pygame.K_UP]:
        player.y -= player.vel

#Tjekker om karakteren er på stigen
    if player.y <640 and player.y > 410 and player.keys[pygame.K_LEFT]:
        player.vel = 0
    elif player.y <640 and player.y > 410 and player.keys[pygame.K_RIGHT]:
        player.vel = 0
    else:
        player.vel = 5

#Tjekker om spilleren går ned på stigen
    if player.x < 305 and player.x > 280 and player.keys[pygame.K_DOWN]:
        player.y += player.vel
    elif player.y < 415:
        player.y = 410
    elif player.y > 640:
        player.y = 640

#Tjekker om spileren er uden for platformen
    if player.x > 750 and player.y <=410:
        player.y=640
        player.health -= 15
    elif player.x <=260 and player.y <=410:
        player.y=640
        player.health -= 20





#tjekker om karakteren er ved hjertet(Healthstation)
#Healing

    if player.x > 694 and player.x < 697 and player.y < 412 and player.y > 408 and healing.healingtimes==True:

        if not game.thread.is_alive():
            game.thread=myThread(5)
            game.thread.start()
            treasure.health = 1000
            healing.times -=1
        else:
            print("nooooooooooooo")

    if healing.times == 0:
        healing.healingtimes = False
        healing.healing = 0



#Tjekker om spilleren er ved ammokassen

    if player.x > 365 and player.x < 405 and player.y == 410:
        game.ammo = 90



# Forloop for player_bullet
    for bullet in game.player_bullets:
        if bullet.speed > 0:
            game.screen.blit(player.attackR, (bullet.x, bullet.y))
        else:
            game.screen.blit(player.attackL, (bullet.x, bullet.y))
        bullet.update()
        if bullet.x > game.screen_width:
            game.player_bullets.remove(bullet)
            print("fjernet")
        elif bullet.x < 0:

            print("fjernet")

        for enemy in game.enemy_list:
            if bullet.y - bullet.radius < enemy.hitbox[1] + enemy.hitbox[3] and bullet.y + bullet.radius > enemy.hitbox[1]:
                if bullet.x + bullet.radius > enemy.hitbox[0] and bullet.x - bullet.radius < enemy.hitbox[0] + enemy.hitbox[2]:
                    print("Fjern")
                    enemy.health -= 5
                    game.player_bullets.remove(bullet)
                    break

    for enemy in game.enemy_list:
        enemy.update()
        if enemy.health < 0:
            game.highscore +=1
            game.enemy_list.remove(enemy)

    game.zombie_spawner()


#Tjekker highscores
    if game.highscore >= 25 and game.highscore < 50:
        player.attackR = pygame.image.load('player/waterball2.png')
        player.attackR = pygame.transform.scale(player.attackR, (32, 36))

        player.attackL = pygame.image.load('player/waterball.png')
        player.attackL = pygame.transform.scale(player.attackL, (32, 36))

        Bullets.damage = 20


    if game.highscore >= 50 and game.highscore < 75:
        player.attackR = pygame.image.load('player/plasmaball2.png')
        player.attackR = pygame.transform.scale(player.attackR, (32, 36))

        player.attackL = pygame.image.load('player/plasmaball.png')
        player.attackL = pygame.transform.scale(player.attackL, (32, 36))

        Bullets.damage = 30


    if game.highscore >= 75:
        player.attackR = pygame.image.load('player/greenball2.png')
        player.attackR = pygame.transform.scale(player.attackR, (32, 36))

        player.attackL = pygame.image.load('player/greenball.png')
        player.attackL = pygame.transform.scale(player.attackL, (32, 36))

        Bullets.damage = 45


#forLop for enemy2_bullet
    # for bullet in game.enemy2_bullets:
    #     if bullet.speed > 0:
    #         game.screen.blit(enemy2.brain, (bullet.x, bullet.y))
    #     else:
    #         game.screen.blit(enemy2.brain, (bullet.x, bullet.y))
    #     bullet.update()
    #
    #     if bullet.x > game.screen_width:
    #         game.enemy2_bullets.remove(bullet)
    #         print("fjernet")
    #     elif bullet.x < 0:
    #         game.enemy2_bullets.remove(bullet)
    #         print("fjernet")
    #     elif bullet.x > player.x + 5 or bullet.x == player.x:
    #         game.enemy2_bullets.remove(bullet)
    #         player.health -= 5
    #         print("fjernet")
    #     if player.y < 640:
    #         game.enemy2_bullets.remove(bullet)
    #         print("fjernet")













    player.player_creation()
    player.player_draw()
    for enemy in game.enemy_list:
        enemy.draw_enemy1()

    #enemy2.draw_enemy2(game)
    pygame.display.update()


def end_game(game):
    newFont5=pygame.font.Font("Retro.ttf", 120)
    newText5=newFont5.render(str("YOU LOST"), 0, black)
    game.screen.blit(newText5, (500, 150))
    pygame.display.update()


#While game_loop
while not done:
    if game.tilstand==0:
        main_menu(game)
    if game.tilstand==1:
        draw_game(game)
    if game.tilstand==2:
        end_game(game)





self.clock.tick(self.FPS)
main_menu()
pygame.quit()
quit()
