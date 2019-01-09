import pygame
from game import *
from pygame.locals import *
from tkinter import *
from tkinter import messagebox

W = 900
H = 500
B = 40
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()
pygame.font.init()
SCREEN = pygame.display.set_mode((W, H))
FONT = pygame.font.SysFont('Calibri (Body)', 30)


class Start:

    def __init__(self):
        self.__sidebar = None
        self.__game = None
        self.__start_time = 0

    def __home_screen(self):
        SCREEN.fill(WHITE)
        pygame.display.set_caption('Letter Scramble Game')
        logo = pygame.image.load('images/logo.PNG')
        SCREEN.blit(logo, (W/4.5, H/12))
        start_text = FONT.render("Click to Start", False, (0, 0, 0))
        SCREEN.blit(start_text, (W/3 + 120, 5*H/7))

    def __get_time(self):
        counting_time = pygame.time.get_ticks() - self.__start_time
        minutes = "{:.2f}".format(counting_time/60000)
        return minutes

    def __game_end(self):
        score = str(self.__sidebar.get_score())
        total = str(self.__game.get_total())
        new = str(self.__game.get_total() - self.__sidebar.get_score())
        Tk().withdraw()
        messagebox.showinfo("Game Over", str(self.__game.get_meaning()) +
                            "\n\nYour Score is: " + score + " out of " + total
                            + "\nYou have learned " + new + " new words!! :D")

    def __help(self):
        Tk().withdraw()
        messagebox.showinfo("Instructions", "Rearrange as many words as you can in 1.00 minutes to form a valid "
                                            "english words. You can learn a new word by clicking on NEXT. getting it's "
                                            "meaning and moving on to the next word. Use SHUFFLE symbol in the sidebar"
                                            " to get a new arrangement of the word for help.")

    def home_loop(self):
        home = True
        while home:
            self.__home_screen()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit(0)
                if event.type == MOUSEBUTTONDOWN:
                    home = False
            pygame.display.update()

    def game_loop(self):
        self.__game = Game()
        self.__sidebar = SideBar()
        self.__start_time = pygame.time.get_ticks()
        while True:
            pygame.draw.rect(SCREEN, WHITE, (W - 130, 0, 130, 40))
            minutes = self.__get_time()
            current = FONT.render(str(minutes), False, (0, 0, 0))
            SCREEN.blit(current, (W - 100, 0))

            if str(minutes) >= "2.01":
                self.__game_end()
                main()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit(0)
                if event.type == MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if self.__sidebar.help_rect.collidepoint(x, y):
                        self.__help()
                    if self.__sidebar.shuffle_rect.collidepoint(x, y):
                        self.__game.on_click_shuffle()
                    if self.__game.new_word_rect.collidepoint(x, y):
                        self.__game.display_meaning(False)
                        self.__game.on_click_new_word()
                    if self.__game.submit_rect.collidepoint(x, y):
                        if self.__game.submit_status():
                            self.__sidebar.add_score()
                    if self.__game.check_clicked_shuffled_letters(x, y):
                        self.__game.update_display()
                    if self.__game.clear_rect.collidepoint(x, y):
                        self.__game.clear_submission()
                pygame.display.flip()
            pygame.display.update()


def main():
    play_game = Start()
    play_game.home_loop()
    play_game.game_loop()


if __name__ == '__main__':
    main()
