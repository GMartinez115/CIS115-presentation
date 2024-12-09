import pygame, random

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 550
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Monkey Game")

FPS = 60
clock = pygame.time.Clock()

#variables
PLAYER_STARTING_HP = 5
PLAYER_VELOCITY = 15
BANANA_STARTING_VELOCITY = 6.0
BOMB_STARTING_VELOCITY = 4.5
RED_BOMB_VELOCITY = 3.0
BUFFER_DISTANCE = 100

score = 0
player_HP = PLAYER_STARTING_HP
banana_velocity = BANANA_STARTING_VELOCITY
bomb_velocity = BOMB_STARTING_VELOCITY

BLACK = (0, 0, 0)

#load images and text
jungle_background = pygame.image.load("Jungle.png")
jungle_rect = jungle_background.get_rect()

monkey_image = pygame.image.load("Monkey.png")
monkey_rect = monkey_image.get_rect()
monkey_rect.centerx = WINDOW_WIDTH // 2
monkey_rect.bottom = WINDOW_HEIGHT

banana_image = pygame.image.load("Banana.png")
banana_rect = banana_image.get_rect()
banana_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT - 800)

bomb_image = pygame.image.load("Bomb.png")
bomb_rect = bomb_image.get_rect()
bomb_rect.center = (random.randint(20, WINDOW_WIDTH - 30), WINDOW_HEIGHT - 1300)

bomb2_image = pygame.image.load("Bomb2.png")
bomb2_rect = bomb2_image.get_rect()
bomb2_rect.center = (random.randint(20, WINDOW_WIDTH - 30), WINDOW_HEIGHT - 1700)

bomb3_image = pygame.image.load("Bomb3.png")
bomb3_rect = bomb3_image.get_rect()
bomb3_rect.center = (random.randint(40, WINDOW_WIDTH - 80), WINDOW_HEIGHT - 2100)

custom_font = pygame.font.Font('Retro Gaming.ttf', 17)
custom_font2 = pygame.font.Font('Retro Gaming.ttf', 20)

custom_text = custom_font2.render("Get banana return to monke", True, BLACK)
custom_text_rect = custom_text.get_rect()
custom_text_rect.center = (WINDOW_WIDTH//2 + 15, WINDOW_HEIGHT//6 - 75)

score_text = custom_font.render("SCORE: " + str(score), True, BLACK)
score_rect = custom_text.get_rect()
score_rect.topleft = (10, 5)

lives_text = custom_font.render("HP: " + str(player_HP), True, BLACK)
lives_rect = lives_text.get_rect()
lives_rect.topright = (WINDOW_WIDTH - 10, 5)

game_over_text = custom_font2.render("GAMEOVER", True, BLACK)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 - 105)

continue_text = custom_font2.render("R.I.P Monkey", True, BLACK)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 - 80)

#music and sounds
music = pygame.mixer.music.load('BGM.mp3')
banana_sound = pygame.mixer.Sound('Banana_sound.mp3')
bomb_sound = pygame.mixer.Sound('explode_sound.mp3')


pygame.mixer.music.play(-1)

#game loop
running = True
while running:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    #movement for monkey
    if keys[pygame.K_LEFT] and monkey_rect.x > 5:
        monkey_rect.x -= PLAYER_VELOCITY
    if keys[pygame.K_RIGHT] and monkey_rect.x < 500:
        monkey_rect.x += PLAYER_VELOCITY

    #code to make banana and bombs fall down
    if banana_rect.y > WINDOW_HEIGHT:
        banana_rect.x = random.randint(10, 560)
        banana_rect.y = WINDOW_HEIGHT - 700
    else:
        banana_rect.y += banana_velocity

    if bomb_rect.y > WINDOW_HEIGHT:
        bomb_rect.x = random.randint(10, 560)
        bomb_rect.y = WINDOW_HEIGHT - 1000
    else:
        bomb_rect.y += bomb_velocity

    if bomb2_rect.y > WINDOW_HEIGHT:
        bomb2_rect.x = random.randint(10, 560)
        bomb2_rect.y = WINDOW_HEIGHT - 1000
    else:
        bomb2_rect.y += bomb_velocity

    if bomb3_rect.y > WINDOW_HEIGHT:
        bomb3_rect.x = random.randint(40, 520)
        bomb3_rect.y = WINDOW_HEIGHT - 1300
    else:
        bomb3_rect.y += RED_BOMB_VELOCITY

    #collisions
    if monkey_rect.colliderect(banana_rect):
        score += 1
        banana_sound.play()
        bomb_velocity += 0.5
        banana_rect.x = random.randint(20, WINDOW_WIDTH - 40)
        banana_rect.y = WINDOW_HEIGHT - 700
        #bonus
        if score % 10 == 0:
            score += 20

    if monkey_rect.colliderect(bomb_rect):
        player_HP -= 1
        bomb_sound.play()
        bomb_rect.x = random.randint(20, 560)
        bomb_rect.y = WINDOW_HEIGHT - 1000

    if monkey_rect.colliderect(bomb2_rect):
        player_HP -= 1
        bomb_sound.play()
        bomb2_rect.x = random.randint(20, 560)
        bomb2_rect.y = WINDOW_HEIGHT - 1000

    if monkey_rect.colliderect(bomb3_rect):
        player_HP = 0
        bomb_sound.play()

    #score and lives
    score_text = custom_font.render("SCORE: " + str(score), True, BLACK)
    lives_text = custom_font.render("HP: " + str(player_HP), True, BLACK)

    #game over
    if player_HP == 0:
        display_surface.blit(game_over_text, game_over_rect)
        display_surface.blit(continue_text, continue_rect)
        pygame.display.update()

        pygame.mixer.music.stop()
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    score = 0
                    player_HP = PLAYER_STARTING_HP
                    monkey_rect.centerx = WINDOW_WIDTH // 2
                    monkey_rect.bottom = WINDOW_HEIGHT
                    banana_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT - 800)
                    banana_velocity = BANANA_STARTING_VELOCITY
                    bomb_rect.center = (random.randint(20, WINDOW_WIDTH - 30), WINDOW_HEIGHT - 1300)
                    bomb2_rect.center = (random.randint(20, WINDOW_WIDTH - 30), WINDOW_HEIGHT - 1700)
                    bomb3_rect.center = (random.randint(40, WINDOW_WIDTH - 80), WINDOW_HEIGHT - 2100)
                    bomb_velocity = BOMB_STARTING_VELOCITY
                    pygame.mixer.music.play(-1, 0.0)
                    is_paused = False
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False

    #blit images and text
    display_surface.blit(jungle_background, jungle_rect)
    display_surface.blit(monkey_image, monkey_rect)
    display_surface.blit(banana_image, banana_rect)
    display_surface.blit(bomb_image, bomb_rect)
    display_surface.blit(bomb2_image, bomb2_rect)
    display_surface.blit(bomb3_image, bomb3_rect)
    display_surface.blit(custom_text, custom_text_rect)
    display_surface.blit(score_text, score_rect)
    display_surface.blit(lives_text, lives_rect)

    #hit boxes
    #pygame.draw.rect(display_surface, (255, 255, 0), monkey_rect, 1)
    #pygame.draw.rect(display_surface, (255, 255, 0), banana_rect, 1)
    #pygame.draw.rect(display_surface, (255, 255, 0), bomb_rect, 1)
    #pygame.draw.rect(display_surface, (255, 255, 0), bomb2_rect, 1)
    #pygame.draw.rect(display_surface, (255, 255, 0), bomb3_rect, 1)


    pygame.display.update()

    clock.tick(FPS)


pygame.quit()
