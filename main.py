import pygame
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
    start_text = myfont.render("Click to Start", False, (0, 0, 0))
    screen.blit(start_text, (w/3 + 120, 5*h/7))


def get_time(start_time):
    counting_time = pygame.time.get_ticks() - start_time
    minutes = "{:.2f}".format(counting_time/60000)
    return minutes


def game_end(start_game, sidebar):
    score = str(sidebar.score)
    total = str(start_game.total_words)
    new = str(start_game.total_words - sidebar.score)
    Tk().withdraw()
    messagebox.showinfo("Game Over", str(start_game.get_meaning()) +
                        "\n\nYour Score is: " + score + " out of " + total
                        + "\nYou have learned " + new + " new words!! :D")


def help():
    Tk().withdraw()
    messagebox.showinfo("Instructions", "Rearrange as many words as you can in 1.00 minutes to form a valid english "
                                        "words. You can learn a new word by clicking on NEXT. getting it's meaning and "
                                        "moving on to the next word. Use SHUFFLE symbol in the sidebar to get a new "
                                        "arrangement of the word for help.")


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
    start_time = pygame.time.get_ticks()
    while True:
        pygame.draw.rect(screen, (255, 255, 255), (w-130, 0, 130, 40))
        minutes = get_time(start_time)
        current = myfont.render(str(minutes), False, (0, 0, 0))
        screen.blit(current, (w - 100, 0))

        if str(minutes) >= "1.01":
            game_end(start_game, sidebar )
            main()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == MOUSEBUTTONDOWN:
                x, y = event.pos
                if sidebar.help_rect.collidepoint(x, y):
                    help()
                if sidebar.shuffle_rect.collidepoint(x, y):
                    start_game.on_click_shuffle()
                if start_game.new_word_rect.collidepoint(x, y):
                    start_game.display_new_word_meaning()
                    start_game.on_click_new_word()
                if start_game.submit_rect.collidepoint(x, y):
                    if start_game.submit_status():
                        sidebar.add_score()
                if start_game.check_clicked_shuffled_letters(x, y):
                    start_game.update_display()
                if start_game.clear_rect.collidepoint(x, y):
                    start_game.clear_submission()
            pygame.display.flip()
        pygame.display.update()


if __name__ == '__main__':
    main()
