#File imports
import pygame
import time


############### Main settings

pygame.init()

display_width = 800
display_height = 600

font_size = 25

#colors
black = (0,0,0)
white = (255,255,255)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('The Origami Warrior')
clock = pygame.time.Clock()

############## Text Display functions
def display_image(filename, pos):
    gameDisplay.fill(white)
    img = pygame.image.load(filename)
    gameDisplay.blit(img, pos)

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def single_text(text, waitTime):
    largeText = pygame.font.Font('freesansbold.ttf', font_size)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (int((display_width/2)),int((display_height/16)))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(int(waitTime))

def paragraph_text(surface, text, pos, font, waitTime, color = pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()] # A 2D array with a row on each line
    space = font.size(' ')[0] # the width of a space
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, True, color)
            word_width, word_height = word_surface.get_size()
            if (x + word_width) >= int(max_width / 6 * 5):
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (int(x), int(y)))
            x += word_width + space
        x = pos[0]  # Reset the x.
        
        y += word_height  # Start on new row.
    
    pygame.display.update()

    time.sleep(int(waitTime))


pos = (display_width / 6, display_height / 16)
font = pygame.font.Font('freesansbold.ttf', font_size)

gameDisplay.fill(white)

# Creation text.

# Once, the great Paper Master came and folded Oru. With valley fold, mountain fold, and squash fold the master created the three Great Folds. 
# First was Orisue with its folds of life. Then came Orikata with its folds of truth. Finally, the great paper folder shaped Orimon with its folds of beauty.
# Then great Paper Master filled Oru with countless kinds of creatures. The Papari, the people of the fold, lived in peace.

display_image('./IntroImages/PlanetOru.png', (200,150))
text = "Once, the great Paper Master came and folded Oru."
single_text(text, 3)

# display_image('./IntroImages/PlanetOru.png', (200,150))
# text = "With valley fold, mountain fold, and \n squash fold the master created the three Great Folds." 
# paragraph_text(gameDisplay, text, pos, font, 3)

# text = "First was Orisue with its folds of life."

# single_text(text, 3)

# text = "Then came Orikata with its folds of truth."

# single_text(text, 3)

# text = "Finally, the great paper folder shaped Orimon with its folds of beauty." 
# paragraph_text(gameDisplay, text, pos, font, 3)

# text = "Then great Paper Master filled Oru with countless kinds of creatures." 
# paragraph_text(gameDisplay, text, pos, font, 3)

# text = "The Papari, the people of the fold, lived in peace."
# single_text(text, 3)

# text = "All was well."
# single_text(text, 6)


# # Disaster text.

# # Then the Polymoids descended. These plastic monsters invaded all of Oru. 
# # Villages were buried, homes crushed, people sealed in great swaths of terrible plastic.
# # It seemed that all was lost. 
# # In this darkest hour, Papyrus, the Origami Warrior arose. Using his mastery of the secret art of Origami,
# # the warrior vanquished the Polymoids and drove them from Oru. Fearing that the Polymoids would someday return,
# # Papyrus recorded his knowledge in a Book. But Papyrus's fears were well founded. A secret agent of the Polymoids
# # attempted to steal the book before Papyrus could share his knowledge. 

# text = "Then the Polymoids descended." 
# single_text(text, 4)

# text = "These plastic monsters invaded all of Oru. Villages were buried, homes crushed, people sealed in great swaths of terrible plastic. It seemed that all was lost."
# paragraph_text(gameDisplay, text, pos, font, 3)

# text = "In this darkest hour, Papyrus, the Origami Warrior arose. Using his mastery of the secret art of Origami, the warrior vanquished the Polymoids and drove them from Oru."
# paragraph_text(gameDisplay, text, pos, font, 4)

# text = "Fearing that the Polymoids would someday return, Papyrus recorded his knowledge in a Book. But Papyrus's fears were well founded."
# paragraph_text(gameDisplay, text, pos, font, 3)

# text = "A secret agent of the Polymoids attempted to steal the book before Papyrus could share his knowledge. "
# paragraph_text(gameDisplay, text, pos, font, 3)

# # Book of Papyrus text. 

# # Thus, it was decided that the book must be split up to protect its secrets. Each of the three lands took a section of the book. 
# # Each page was given to different cities throughout the land. Each city treasured its newfound knowledge and became masters of their
# # page's fold. With the knowledge of Origami so well known throughout Oru, the Polymoids decided invading Oru would be in vain. 
# # They retreated into the far reaches and were never seen again. 

# text = "Thus, it was decided that the book must be split up to protect its secrets. Each of the three lands took a section of the book."
# paragraph_text(gameDisplay, text, pos, font, 3)

# text = "Each page was given to different cities throughout the land. Each city treasured its newfound knowledge and became masters of their page's fold."
# paragraph_text(gameDisplay, text, pos, font, 4)

# text = "With the knowledge of Origami so well known throughout Oru, the Polymoids decided invading Oru would be in vain. They retreated into the far reaches and were never seen again."
# paragraph_text(gameDisplay, text, pos, font, 3)

# # Forgotten text

# # Papyrus warned those that should come after him to gaurd the pages. But over time, the Origami Warrior became a legend, and then a myth. 
# # People forgot the folds that they had learned.


# text = "Papyrus warned those that should come after him to gaurd the pages. But over time, the Origami Warrior became a legend, and then a myth."
# paragraph_text(gameDisplay, text, pos, font, 3)

# text = "People forgot the folds that they had learned." 
# single_text(text, 4)


# # Meanwhile, the Polymoids still continued to watch. Among the Papari, a few remember the last words of Papyrus. He said that someday, 
# # another might have to master the folds as he had. Someday, the Origami Warrior must rise again.

# text = "Meanwhile, the Polymoids still continued to watch. Among the Papari, a few remember the last words of Papyrus. He said that someday, another might have to master the folds as he had. Someday, the Origami Warrior must rise again."
# paragraph_text(gameDisplay, text, pos, font, 4)

pygame.quit()
quit()