import pygame

def main():
    pygame.init()
    
    screen_width, screen_height = 500, 500
    screen = pygame.display.set_mode((screen_width, screen_height))
    
    pygame.display.set_caption('Colour chaning sprite')

    # Mapping out the colour names to RGB values:

    colours = {
        'red': pygame.Color('red'),
        'green': pygame.Color('green'),
        'blue': pygame.Color('blue'),
        'yellow': pygame.Color('yellow'),
        'white': pygame.Color('white'),
    }

    current_colour = colours['white']

    x, y = 30, 30
    sprite_width, sprite_height = 60, 60

    clock = pygame.time.Clock()

    done = False
    
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        pressed = pygame.key.get_pressed()
        
        if pressed[pygame.K_LEFT]: x -= 3 
        if pressed[pygame.K_RIGHT]: x += 3 
        if pressed[pygame.K_UP]: y -= 3 
        if pressed[pygame.K_DOWN]: y += 3 

        x = min(max(0, x), screen_width - sprite_width)
        y = min(max(0, y), screen_height - sprite_height)

        # Change colour based on boundary contact:

        if x == 0: current_colour = colours['blue']
        
        elif x == screen_width - sprite_width: current_colour = colours['yellow']
        elif y == 0: current_colour = colours['red']
        elif y == screen_height - sprite_height: current_colour = colours['green']

        else: 
            current_colour = colours['white']

        screen.fill((0, 0, 0)) # black
        pygame.draw.rect(screen, current_colour, (x, y, sprite_width, sprite_height))

        pygame.display.flip()
        clock.tick(90)
    pygame.quit()


if __name__ == "__main__":
    main()