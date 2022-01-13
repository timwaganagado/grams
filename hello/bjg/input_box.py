import pygame 


def main():
    screen = pygame.display.set_mode((640, 480))
    font = pygame.font.Font(None, 32)
    input_box = pygame.Rect(100, 100, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    betable = ''
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        print(betable)
                        betable = ''
                    elif event.key == pygame.K_BACKSPACE:
                        betable = betable[:-1]
                    else:
                        betable += event.unicode

        screen.fill((255, 255, 255))
        # Render the current betable.
        txt_surface = font.render(betable, True, color)
        # Resize the box if the betable is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the betable.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pygame.draw.rect(screen, color, input_box, 2)

        pygame.display.flip()
        



pygame.init()
main()
pygame.quit()