import pygame
import random
from time import sleep

WIDTH = 800
HEIGHT = 1080

# Initialize Pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))


# Set up font
font = pygame.font.Font(None, 36)

# Load player and enemy images
player_image = pygame.image.load("player.png").convert_alpha()
player_rect = player_image.get_rect()

enemy_image = pygame.image.load("enemy.png").convert_alpha()
enemy_rect = enemy_image.get_rect()

enemy2_image = pygame.image.load("player2.png").convert_alpha()
enemy2_rect = enemy2_image.get_rect()

# Create player sprite
player = pygame.sprite.Sprite()
player.image = player_image
player.rect = player_rect

# Create enemy sprite group
enemies = pygame.sprite.Group()
enemies2 = pygame.sprite.Group()

# Counter for enemy spawn
counter = 0
TARGET_SPAWN_RATE = 1000 # Change this value to adjust the donut spawn rate
ENEMY_SPAWN_RATE = 1000

# Function to spawn enemies
def spawn_enemy():
    global counter
    global TARGET_SPAWN_RATE
    global ENEMY_SPAWN_RATE
    if counter % ENEMY_SPAWN_RATE == 0:
        enemy2 = pygame.sprite.Sprite()
        enemy2.image = enemy2_image
        enemy2.rect = enemy2_rect.copy()
        enemy2.rect.x = random.randint(0, WIDTH - enemy2_rect.width)
        enemy2.rect.y = 0
        enemies2.add(enemy2)
        TARGET_SPAWN_RATE = TARGET_SPAWN_RATE - 7

    if counter % TARGET_SPAWN_RATE == 0:
        enemy = pygame.sprite.Sprite()
        enemy.image = enemy_image
        enemy.rect = enemy_rect.copy()
        enemy.rect.x = random.randint(0, WIDTH - enemy_rect.width)
        enemy.rect.y = 0
        enemies.add(enemy)
        TARGET_SPAWN_RATE = TARGET_SPAWN_RATE - 7
    
    counter += 1
    #print(TARGET_SPAWN_RATE)


# variables
win = False
score = 0    
# Game loop

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((255, 255, 255))

    #print score
    score_text = font.render(f"Score: {score}", True, (0, 255, 0))
    score_rect = score_text.get_rect()
    score_rect.centerx = screen.get_rect().centerx - (WIDTH/2 - 60)
    score_rect.centery = screen.get_rect().centery - (HEIGHT/2 - 30)
    screen.blit(score_text, score_rect)

  # get mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()
    # set player position to mouse position
    player.rect.centerx = mouse_x
    player.rect.centery = HEIGHT - 140

    # Spawn enemies
    spawn_enemy()
    

    # Update enemy positions
    for enemy in enemies:
        enemy.rect.y += 1
    for enemy in enemies2:
        enemy.rect.y += 1
    
    
    if TARGET_SPAWN_RATE < 150:
        win=True
        running=False

    # Check for enemy-player collision
    enemy_hit_list = pygame.sprite.spritecollide(player, enemies, True)
    if enemy_hit_list:
        score = score + 10
    print(enemy_hit_list)
    # Check for enemy-player collision
    enemy_hit_list2 = pygame.sprite.spritecollide(player, enemies2, True)
    if enemy_hit_list2:
        score = score - 50
    print(enemy_hit_list2)

    #for enemy in enemy_hit_list:
        
        #running = False

    # Draw sprites
    screen.blit(player.image, player.rect)
    enemies.draw(screen)
    enemies2.draw(screen)

    if not running:
        if win:
            print(f"You score was: {score}")
            if score > 99:
                you_win_text = font.render(f"You score was: {score}!!!!", True, (0, 255, 0))
            else:
                you_win_text = font.render(f"You score was: {score}, bruh you need to get atleast 100", True, (255, 0, 0))
            you_win_rect = you_win_text.get_rect()
            you_win_rect.centerx = screen.get_rect().centerx
            you_win_rect.centery = screen.get_rect().centery
            screen.blit(you_win_text, you_win_rect)

        else:
            game_over_text = font.render("GAME OVER", True, (255, 0, 0))
            game_over_rect = game_over_text.get_rect()
            game_over_rect.centerx = screen.get_rect().centerx
            game_over_rect.centery = screen.get_rect().centery
            screen.blit(game_over_text, game_over_rect)


    # Update display
    pygame.display.update()
    

# Quit Pygame
sleep(4)
pygame.quit()
