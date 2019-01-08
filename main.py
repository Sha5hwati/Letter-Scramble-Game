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
    screen.blit(logo, (w/4.5, h/12))
    start_text = myfont.render("Click to continue", False, (0, 0, 0))
    screen.blit(start_text, (w/3 + 100, 5.5*h/7))


def main():
    home = True
    while home:
        home_screen(screen)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == MOUSEBUTTONDOWN:
                home = False
        pygame.display.update()

    start_game = game()
    sidebar = SideBar()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == MOUSEBUTTONDOWN:
                x, y = event.pos
                if sidebar.help_rect.collidepoint(x, y):
                    print("Help icon clicked")
                if sidebar.shuffle_rect.collidepoint(x, y):
                    start_game.on_click_shuffle()
                if start_game.new_word_rect.collidepoint(x, y):
                    start_game.on_click_new_word()
                if start_game.submit_rect.collidepoint(x, y):
                    if start_game.submit_status():
                        sidebar.add_score()
                if start_game.check_clicked_shuffled_letters(x, y):
                    start_game.update_display()
                if start_game.clear_rect.collidepoint(x, y):
                    start_game.clear_submission()
            pygame.display.flip()


if __name__ == '__main__':
    main()
