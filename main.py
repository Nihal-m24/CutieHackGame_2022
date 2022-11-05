import pygame
import math
import random

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((800, 800))
bg = pygame.image.load("background.png")

pygame.display.set_caption("Citrus Invaders")

icon = pygame.image.load("orange.png")
pygame.display.set_icon(icon)

#Sound
shooting_sound = pygame.mixer.Sound("shooting_effect.wav")

#MOVING THE SPACESHIP
clock = pygame.time.Clock()
enemyDirection = 1
enemySpeed_x = 5
enemySpeed_y = 4

playerImg = pygame.image.load('battleship.png')
Player_size = (200, 200)
image = pygame.transform.scale(playerImg, Player_size)
playerX = 370
playerY = 700
playerX_change = 0
playerY_change = 0

enemyImg = pygame.image.load('spaceship.png')
enemyX = random.randrange(20, 600)
enemyY = random.randrange(60, 70)
bulletImg = pygame.image.load('fire.png')
bulletX = playerX
bulletY = playerY
bulletY_change = 10
bullet_state = "ready"

enemy_hp = 100
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10

lives = 5
livesImg = pygame.image.load('lives.png')


def display_lives():
    global lives
    startX = 10
    startY = 50
    for i in range(lives):
        screen.blit(livesImg, (startX, startY))
        startX += 50


def show_hp():
    health = font.render("Boss Health", True, (255, 255, 255))
    red = (200, 60, 60)
    screen.blit(health, (500, 10))
    #display_health = int(health/100*200)
    pygame.draw.rect(screen, (255, 255, 255), (495, 45, 260, 35))
    pygame.draw.rect(screen, red, (500,50,enemy_hp/100*250,25))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))
    pygame.mixer.Sound.play(shooting_sound)

# pygame.mixer.music.stop()


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(
        (enemyX + 60) - bulletX, 2) + math.pow(enemyY - bulletY, 2)))
    if distance < 100:
        return True
    return False


def obstacle(obs_startx, obs_starty):
    obs_pic = pygame.image.load("energy.png")
    screen.blit(obs_pic, (obs_startx, obs_starty))


#asteroid function
aIMG = pygame.image.load("asteroid.png")


def asteroid_ob(a_x, a_y):
    a_size = (40, 40)

    a_pic = pygame.transform.scale(aIMG, a_size)
    screen.blit(a_pic, (a_x, a_y))


#attempt moving asteroids

# def isCollision(enemyX, enemyY, bulletX, bulletY):
#     distance = math.sqrt((math.pow(
#         (enemyX + 60) - bulletX, 2) + math.pow(enemyY - bulletY, 2)))
#     if distance < 100:
#         return True
#     return False

running = True
obs_startx = random.randrange(0, 800)
obs_starty = 60
a_x = 250
a_y = 100
being_hit = False
being_hit_copy = False

bg = pygame.image.load("background.png")
while running:
  #FRAME RATE
    clock.tick(120)
    screen.fill((0, 0, 0))

    # screen.blit(bg, (0,0))
    obstacle_speed = 10
    obs = 0
    y_change = 0

    obs_width = 80
    obs_height = 80

    if enemyX <= 20 or enemyX >= 580:
        enemyDirection *= -1
        enemySpeed_x = random.randrange(0, 8) * enemyDirection
        enemySpeed_y = random.randrange(0, 8) * enemyDirection

        if enemySpeed_x == 0 and enemySpeed_x == 0:
          enemySpeed_x = random.randrange(2, 8) * enemyDirection
          enemySpeed_y = random.randrange(2, 8) * enemyDirection

    if enemyY <= 70 or enemyY >= 150:
      enemyDirection *= -1
      enemySpeed_x = random.randrange(0, 8) * enemyDirection
      enemySpeed_y = random.randrange(4, 8) * enemyDirection

      if enemySpeed_x == 0 and enemySpeed_y == 0:
           enemySpeed_x = random.randrange(2, 8) * enemyDirection
           enemySpeed_y = random.randrange(4, 8) * enemyDirection

    enemyX += enemySpeed_x
    enemyY += enemySpeed_y

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                playerX_change = -6
            if event.key == pygame.K_d:
                playerX_change = 6
            if event.key == pygame.K_w:
                playerY_change = -6
            if event.key == pygame.K_s:
                playerY_change = 6
            if event.key == pygame.K_SPACE:
                fire_bullet(playerX + 3 * playerX_change,
                            playerY + 2 * playerY_change)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                playerX_change = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                playerY_change = 0

    playerX += playerX_change
    playerY += playerY_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    if playerY <= 400:
        playerY = 400
    elif playerY >= 700:
        playerY = 700

    if bulletY <= 0:
        bulletX = playerX
        bulletY = playerY
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    collision = isCollision(enemyX, enemyY, bulletX, bulletY)
    if collision:
        enemy_hp -= 1
        bulletY = playerY
        bulletX = playerX
        bullet_state = "ready"
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    show_hp()
    display_lives()

    #asteroid position
    asteroid_ob(a_x, a_y)

    
    obstacle(obs_startx, obs_starty)
    obs_starty += obstacle_speed

    if obs_starty > 800:
        obs_startx = random.randrange(playerX - 30, playerX + 30)
        obs_starty = 100
    if 50 > math.sqrt(
        (math.pow(playerX -
                  (obs_startx), 2) + math.pow(playerY - obs_starty, 2))):
        being_hit = True
        if being_hit_copy == False:
            lives -= 1
    else:
        being_hit = False
        being_hit_copy = False
    being_hit_copy = being_hit
    pygame.display.update()
