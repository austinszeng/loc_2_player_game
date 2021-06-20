import pygame
import os

wid, hei = 800, 600 # 16:9 aspect ratio
win = pygame.display.set_mode((wid, hei)) # initialize screen for display
pygame.display.set_caption("bro bro bro")

fps = 60
spd = 8

# WASD CHARACTERS

# white among us
white_amongus_img = pygame.image.load(os.path.join('Assets', 'white-among-us.png')) 
white_amongus_wei = 50
white_amongus_hei = 60
white_amongus = pygame.transform.scale(white_amongus_img, (white_amongus_wei, white_amongus_hei))


# ARROW CHARACTERS

# red among us
red_amongus_img = pygame.image.load(os.path.join('Assets', 'red-among-us.png'))
red_amongus_wei = 70
red_amongus_hei = 80
red_amongus = pygame.transform.flip(pygame.transform.scale(red_amongus_img, (red_amongus_wei, red_amongus_hei)), True, False)


# METHODS

wall_coords = pygame.Rect(wid/2-3, 0, 6, hei)
def draw(white, red):
    win.fill((30, 30, 30))
    win.blit(white_amongus, (white.x, white.y))
    win.blit(red_amongus, (red.x, red.y))
    pygame.draw.rect(win, (200, 200, 0), wall_coords)
    pygame.display.update()

def wasd_movement(keys_pressed, white): # future implementation of more characters
        # white among us
        if keys_pressed[pygame.K_a] and white.x - spd > 0:
            white.x -= spd
        if keys_pressed[pygame.K_d] and white.x + spd + white.width < wall_coords.x: 
            white.x += spd
        if keys_pressed[pygame.K_w] and white.y - spd > 0: 
            white.y -= spd 
        if keys_pressed[pygame.K_s] and white.y + spd + white.height < hei: 
            white.y += spd

def arrow_movement(keys_pressed, red):
        # red among us
        if keys_pressed[pygame.K_LEFT] and red.x - spd > wall_coords.x:
            red.x -= spd
        if keys_pressed[pygame.K_RIGHT] and red.x + spd + red.width < wid: 
            red.x += spd
        if keys_pressed[pygame.K_UP] and red.y - spd > 0: 
            red.y -= spd 
        if keys_pressed[pygame.K_DOWN] and red.y + spd + red.height < hei: 
            red.y += spd