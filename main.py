from vars_and_methods import *

def main():
    # Keep track of coordinates for movement
    white = pygame.Rect(100, 250, white_amongus_wei, white_amongus_hei)
    red = pygame.Rect(700, 250, red_amongus_wei, red_amongus_hei)

    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(fps) # limit fps
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                quit()

        keys_pressed = pygame.key.get_pressed()
        wasd_movement(keys_pressed, white)
        arrow_movement(keys_pressed, red)

        draw(white, red)

    main()
        

if __name__ == '__main__':
    main()
