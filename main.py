import pygame
import math
import random

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((800, 800))
bg = pygame.image.load("background.png")
explosion = pygame.image.load("explosion.png")
# screen.draw.text("hello world", (100, 100), color=(200, 200, 200), background="gray")
pygame.display.set_caption("Citrus Invaders")

icon = pygame.image.load("orange.png")
pygame.display.set_icon(icon)

# Sound
shooting_sound = pygame.mixer.Sound("shooting_effect.wav")
win_sound = pygame.mixer.Sound("win_sound.wav")
loss_sound = pygame.mixer.Sound("loss_sound.mp3")

# MOVING THE SPACESHIP
clock = pygame.time.Clock()
enemyDirection = 1
enemyDirection_y = -1

# Timer
timer = pygame.time.Clock()
gamePlay = ""

enemySpeed_x = 5
enemySpeed_y = 4

playerImg = pygame.image.load('battleship.png')
Player_size = (200, 200)
image = pygame.transform.scale(playerImg, Player_size)
playerX = 370
playerY = 700
playerX_change = 0
playerY_change = 0

enemyImg = pygame.image.load('main_orange.png')
# enemyImg_scaled = pygame.transform.scale(enemyImg,300,300)
enemyX = random.randrange(20, 600)
enemyY = random.randrange(60, 70)
bulletImg = pygame.image.load('fire.png')
bulletX = playerX
bulletY = playerY
bulletY_change = 10
bullet_state = "ready"

# enemy_hp = 100
enemy_hp = 20
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10

lives = 5
livesImg = pygame.image.load('lives.png')


def display_lives():
    global lives
    startX = 10
    startY = 10
    for i in range(lives):
        screen.blit(livesImg, (startX, startY))
        startX += 50


def show_hp():
    health = font.render("Boss Health", True, (255, 255, 255))
    red = (200, 60, 60)
    screen.blit(health, (500, 10))
    # display_health = int(health/100*200)
    pygame.draw.rect(screen, (255, 255, 255), (495, 45, 260, 35))
    pygame.draw.rect(screen, red, (500, 50, enemy_hp / 20 * 250, 25))  # change back to 20


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))
    pygame.mixer.Sound.play(shooting_sound)


#


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(
        (enemyX + 60) - bulletX, 2) + math.pow(enemyY - bulletY, 2)))

    if distance < 100:
        return True
    return False


def obstacle(obs_startx, obs_starty):
    obs_pic = pygame.image.load("Seed.png")
    obs_size = (25, 45)
    seed = pygame.transform.scale(obs_pic, obs_size)

    screen.blit(seed, (obs_startx, obs_starty))


# asteroid function


aIMG = pygame.image.load("annoyingOrange.png")


def asteroid(a_x, a_y):
    a_size = (70, 50)

    a_pic = pygame.transform.scale(aIMG, a_size)
    screen.blit(a_pic, (a_x, a_y))


def life(life_x, life_y):
    heart_pic = pygame.image.load("heart.png")
    screen.blit(heart_pic, (life_x, life_y))


def wall_event_func(wall1_x, wall2_x, wall_y):
    wall_pic = pygame.image.load("wall.png")
    screen.blit(wall_pic, (wall1_x, wall_y))
    screen.blit(wall_pic, (wall2_x, wall_y))


def game_over():
    end_screen = True
    gamePlayMinute = '{minutes:02d}'.format(minutes=minutes)
    gamePlaySeconds = '{seconds:02d}'.format(seconds=seconds)
    game_overIMG = pygame.image.load("GameOver.png")
    victoryIMG = pygame.image.load("victory.png")

    while end_screen:
        screen.fill((0, 0, 0))
        win = font.render("Congratulations", True, (255, 255, 255))

        timeText = font.render("You Played For " + gamePlayMinute + " Minutes and " + gamePlaySeconds + " Seconds",
                               True, (255, 250, 250))
        if lives == 0:
            pygame.mixer.Sound.play(loss_sound)
            screen.blit(game_overIMG, (0, 0))
            screen.blit(timeText, (50, 450))
        if enemy_hp == 0:
            pygame.mixer.Sound.play(win_sound)
            screen.blit(victoryIMG, (0, 0))
            screen.blit(timeText, (50, 450))
        pygame.display.update()

        pygame.mixer.music.stop()


# attempt moving asteroids

# def isCollision(enemyX, enemyY, bulletX, bulletY):
#     distance = math.sqrt((math.pow(
#         (enemyX + 60) - bulletX, 2) + math.pow(enemyY - bulletY, 2)))
#     if distance < 100:
#         return True
#     return Falseasds


# asteroids code
left_right = random.randint(0, 1)
side = random.randint(0, 1)
a_x = 0
a_y = 0
if left_right == 0:
    if side == 0:
        a_x = 0
    else:
        a_x = 800
    a_y = random.randint(0, 800)
else:
    if side == 0:
        a_y = 800
    else:
        a_y = 0
    a_x = random.randint(0, 800)

new_asteroid = 0

running = True
obs_startx = random.randrange(0, 800)
obs_starty = 60

being_hit = False
being_hit_copy = False

being_hit_a = False
being_hit_copy_a = False

bg = pygame.image.load("background.png")

life_hit = False
life_hit_copy = False
life_given = False
life_moving = False
life_x = 800
life_y = random.randint(380, 680)

wall_event = False
wall_event_ongoing = False
wall_y = 0
wall_hit = False
wall_hit_copy = False

while running:
    # FRAME RATE
    clock.tick(60)
    screen.fill((0, 0, 0))
    screen.blit(bg, (0,0 ))
    ticks = pygame.time.get_ticks()
    millis = ticks % 1000
    seconds = int(ticks / 1000 % 60)
    minutes = int(ticks / 60000 % 24)
    # wall event
    if not wall_event:
        if enemy_hp == 13:
            wall_event_ongoing = True
            wall_event = True
    if wall_event:
        if (playerX < 350 or playerX > 500) and (playerY > wall_y - 100 and playerY < wall_y + 100):
            wall_hit = True
            if wall_hit_copy == False:
                lives -= 1
        else:
            wall_hit = False
            wall_hit_copy = False

        wall_speed = 1.5
        wall_y += wall_speed
        wall1_x = 0
        wall2_x = 500
        wall_event_func(wall1_x, wall2_x, wall_y)

        if wall_y > 800:
            wall_event = False

    # life
    if not life_given:
        if enemy_hp == 10:
            life_moving = True

    if life_moving:
        life_x -= 4
        life(life_x, life_y)
        if 40 > math.sqrt((math.pow(playerX - (life_x), 2) + math.pow(playerY - life_y, 2))):
            lives += 1
            life_given = True
            life_moving = False

    # asteroid
    if new_asteroid == 3:
        left_right = random.randint(0, 1)
        side = random.randint(0, 1)
        if left_right == 0:
            if side == 0:
                a_x = 0
            else:
                a_x = 800
            a_y = random.randint(0, 800)
        else:
            if side == 0:
                a_y = 800
            else:
                a_y = 0
            a_x = random.randint(0, 800)
            new_asteroid = 0
    if new_asteroid == 0:
        ax_change = (playerX + random.randint(-200, 200) - a_x) / 100
        ay_change = (playerY + random.randint(-200, 200) - a_y) / 100
        new_asteroid = 1
    if a_x > 800 or a_x < 0 or a_y > 800 or a_y < 0:
        new_asteroid = 3
    asteroid(a_x, a_y)
    a_x += ax_change
    a_y += ay_change
    if 50 > math.sqrt((math.pow(playerX - (a_x), 2) + math.pow(playerY - a_y, 2))):
        being_hit_a = True
        if being_hit_copy_a == False:
            lives -= 1
    else:
        being_hit_a = False
        being_hit_copy_a = False
    # screen.blit(bg, (0,0))
    obstacle_speed = 10
    obs = 0
    y_change = 0

    obs_width = 80
    obs_height = 80

    pos = int(1600 / 3)
    if enemyX == pos & enemySpeed_x > 0:
        print("test")
        if random.randint(0, 5) == 0:
            enemySpeed_x *= -1

    if enemyX <= 20 or enemyX >= 600:
        enemySpeed_x *= -1
    if enemyY <= 20 or enemyY >= 150:
        enemySpeed_y *= -1

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
                fire_bullet(enemyX + 3 * playerX_change,
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
        explosion_size = (90, 90)
        explosion_pic = pygame.transform.scale(explosion, explosion_size)
        screen.blit(explosion_pic, [enemyX + 40, enemyY + 25])
        bulletY = playerY
        bulletX = playerX
        bullet_state = "ready"
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    show_hp()
    display_lives()

    # asteroid position
    # asteroid_ob(a_x, a_y)

    obstacle(obs_startx, obs_starty)
    obs_starty += obstacle_speed

    if obs_starty > 800:
        obs_startx = random.randrange((enemyX + 100) - 50, (enemyX + 100) + 50)
        obs_starty = enemyY + 30
    # energy collision
    if 50 > math.sqrt((math.pow(playerX - (obs_startx), 2) + math.pow(playerY - obs_starty, 2))):
        being_hit = True
        if being_hit_copy == False:
            lives -= 1
    else:
        being_hit = False
        being_hit_copy = False

    if lives == 0 or enemy_hp == 0:
        running = False
        game_over()

    being_hit_copy = being_hit
    being_hit_copy_a = being_hit_a
    wall_hit_copy = wall_hit

    pygame.display.update()
    # End of Loop
