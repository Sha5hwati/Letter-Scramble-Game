import sys
from game import *
from pygame.locals import *

w = 900
h = 500
b = 40
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Calibri (Body)', 30)
screen = pygame.display.set_mode((w, h))

def home_screen(screen):
    screen.fill(WHITE)
    pygame.display.set_caption('Dictionary')
    logo = pygame.image.load('images/logo.PNG')
    screen.blit(logo, (w/4, h/12))
    start_text = myfont.render("Click to continue", False, (0, 0, 0))
    screen.blit(start_text, (1.2*w/3, 5.5*h/7))


def main():
    # home_screen(screen)

    start_game = game()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == MOUSEBUTTONDOWN:
                x, y = event.pos
                print("x: " + str(x) + " y: " + str(y))
                if SideBar().help_rect.collidepoint(x, y):
                    print("Help icon clicked")
                if SideBar().shuffle_rect.collidepoint(x, y):
                    start_game.on_click_shuffle()
            pygame.display.flip()


if __name__ == '__main__':
    main()
