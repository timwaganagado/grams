import pygame
import pygame.freetype
from itertools import cycle

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    # just some demo data for you to type
    data = cycle(['This is an example.', 'This is another, longer sentence.'])
    current = next(data)
    current_idx = 0 # points to the current letter, as you have already guessed
    
    font = pygame.freetype.Font(None, 50)
    # the font in the new freetype module have an origin property.
    # if you set this to True, the render functions take the dest position 
    # to be that of the text origin, as opposed to the top-left corner
    # of the bounding box
    font.origin = True
    font_height = font.get_sized_height()
    
    # we want to know how much space each letter takes during rendering.
    # the item at index 4 is the 'horizontal_advance_x'
    M_ADV_X = 4
    
    # let's calculate how big the entire line of text is
    text_surf_rect = font.get_rect(current)
    # in this rect, the y property is the baseline
    # we use since we use the origin mode
    baseline = text_surf_rect.y
    # now let's create a surface to render the text on
    # and center it on the screen
    text_surf = pygame.Surface(text_surf_rect.size)
    text_surf_rect.center = screen.get_rect().center
    # calculate the width (and other stuff) for each letter of the text
    metrics = font.get_metrics(current)

    while True:
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                return
            if e.type == pygame.KEYDOWN:
                if e.unicode == current[current_idx].lower():
                    # if we press the correct letter, move the index
                    current_idx += 1
                    if current_idx >= len(current):
                        # if the sentence is complete, let's prepare the
                        # next surface
                        current_idx = 0
                        current = next(data)
                        text_surf_rect = font.get_rect(current)
                        baseline = text_surf_rect.y
                        text_surf = pygame.Surface(text_surf_rect.size)
                        text_surf_rect.center = screen.get_rect().center
                        metrics = font.get_metrics(current)

        # clear everything                        
        screen.fill('white')
        text_surf.fill('white')
        
        x = 0
        # render each letter of the current sentence one by one
        for (idx, (letter, metric)) in enumerate(zip(current, metrics)):
            # select the right color
            if idx == current_idx:
                color = 'lightblue'
            elif idx < current_idx:
                color = 'lightgrey'
            else:
                color = 'black'
            # render the single letter
            font.render_to(text_surf, (x, baseline), letter, color)
            # and move the start position
            x += metric[M_ADV_X]
          
        screen.blit(text_surf, text_surf_rect)
        pygame.display.flip()

if __name__ == '__main__':
    main()