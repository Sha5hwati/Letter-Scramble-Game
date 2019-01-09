from PyDictionary import PyDictionary
from itertools import permutations
import random
from sidebar import *
from tkinter import *
from tkinter import messagebox
from main import SCREEN, W, H, WHITE, BLACK, FONT


class Game:
    __dictionary = PyDictionary()
    __LIGHT_TEAL = (175, 238, 238)
    __RED = (255, 0, 0)
    __word = ""
    __shuffled_word = ""
    __submission = ""
    __shuffled_word_positions = []
    __chosen = []
    __words = []
    __total_words = 0

    def __init__(self):
        SCREEN.fill(self.__LIGHT_TEAL)
        self.__read_words()
        self.extra = 0
        self.__new_word_icon = pygame.image.load('images/next.png')
        self.new_word_rect = self.__new_word_icon.get_rect()
        self.__submit_icon = pygame.image.load('images/submit.png')
        self.submit_rect = self.__submit_icon.get_rect()
        self.__clear_icon = pygame.image.load('images/clear.png')
        self.clear_rect = self.__clear_icon.get_rect()
        self.on_click_new_word()
        self.__submit_button()
        self.__clear_button()
        self.__new_word_button()

    def __read_words(self):
        text_file = open("words.txt", "r")
        self.__words = text_file.readlines()
        text_file.close()

    def get_meaning(self):
        meanings = ""
        if self.__word != "":
            mean = self.__dictionary.meaning(str(self.__word))
            if mean is not None:
                for keys in mean:
                    val = mean[keys][0]
                    meanings = "" + str(self.__word) + ": " + str(val)
        return meanings

    def __get_word(self):
        position = random.randint(0, len(self.__words))
        self.__word = self.__words[position].strip()
        while len(self.__word) < 3 or len(self.__word) > 6 or self.get_meaning() == "":
            position = random.randint(0, len(self.__words))
            self.__word = self.__words[position].strip()
        self.__word = self.__word.upper()

    def __clear_word(self):
        start_x = (1.5*int(W))/len(self.__word)
        for i in range(0, len(self.__word)):
            pygame.draw.line(SCREEN, self.__LIGHT_TEAL, (start_x + i*90, H/3 + 50), (start_x + i*90 + 80, H/3 + 50))
            rect = pygame.Rect(pygame.Rect(start_x + i * 90, H/2, 80, 70))
            pygame.draw.rect(SCREEN, self.__LIGHT_TEAL, rect)

    def __display_word(self):
        start_x = (1.5*int(W))/len(self.__shuffled_word)
        for i in range(0, len(self.__word)):
            rect = pygame.Rect(pygame.Rect(start_x + i*90, H/2, 80, 70))
            pygame.draw.rect(SCREEN, BLACK, rect)
            letter_font = pygame.font.SysFont('Calibri (Body)', 60)
            letter = letter_font.render(str(self.__shuffled_word[i]), False, (255, 245, 255))
            SCREEN.blit(letter, (start_x + i*90 + 20, H/2 + 10))
            self.__shuffled_word_positions.append(rect)

    def __clear_chosen(self):
        self.__chosen.clear()
        for i in range(0, len(self.__word)):
            self.__chosen.append(False)

    def __display_blank(self):
        start_x = (1.5*int(W))/len(self.__shuffled_word)
        for i in range(0, len(self.__word)):
            pygame.draw.line(SCREEN, (0, 0, 0), (start_x + i*90, H/3 + 50), (start_x + i*90 + 80, H/3 + 50))

    def __shuffle(self):
        words = list(map("".join, permutations(self.__word)))
        ran = random.randint(0, len(words)-1)
        while words[ran] == self.__word:
            ran = random.randint(0, len(words)-1)
        self.__shuffled_word = words[ran]

    def __new_word_button(self):
        self.__new_word_icon = pygame.transform.scale(self.__new_word_icon, (100, 50))
        SCREEN.blit(self.__new_word_icon, (W/3, H/2+100))
        self.new_word_rect = self.__new_word_icon.get_rect(x=W/3, y=H/2+100)

    def __clear_button(self):
        self.__clear_icon = pygame.transform.scale(self.__clear_icon, (100, 50))
        SCREEN.blit(self.__clear_icon, (W/3 + 130, H/2 + 100))
        self.clear_rect = self.__clear_icon.get_rect(x=W / 3 + 130, y=H/2 + 100)

    def __submit_button(self):
        self.__submit_icon = pygame.transform.scale(self.__submit_icon, (100, 50))
        SCREEN.blit(self.__submit_icon, (W / 3 + 260, H / 2 + 100))
        self.submit_rect = self.__submit_icon.get_rect(x=W / 3 + 260, y=H / 2 + 100)

    def on_click_shuffle(self):
        self.__shuffle()
        self.__display_word()
        self.__display_blank()
        self.__clear_chosen()

    def on_click_new_word(self):
        if len(self.__submission) != 0:
            self.clear_submission()
        if len(self.__word) != 0:
            self.__clear_word()
        self.__shuffled_word_positions.clear()
        self.__total_words += 1
        self.__get_word()
        self.on_click_shuffle()

    def check_clicked_shuffled_letters(self, x, y):
        for pos in range(0, len(self.__shuffled_word_positions)):
            if self.__shuffled_word_positions[pos].collidepoint(x, y):
                if self.__chosen[pos] is False:
                    self.__submission += self.__shuffled_word[pos]
                    self.__chosen[pos] = True
                    return True
                if self.__chosen[pos]:
                    text = FONT.render("Letter already chosen", False, (0, 0, 0))
                    SCREEN.blit(text, (W / 2, 10))
                    pygame.display.update()
                    pygame.time.delay(800)
                    pygame.draw.rect(SCREEN, self.__LIGHT_TEAL, (W / 2, 0, 240, 30))
                    pygame.display.update()
                    return False
        return False

    def display_meaning(self, correct):
        meaning = self.get_meaning()
        if correct:
            title = "Yay!! Correct Submission :D "
        else:
            title = "You learned a new word :) "
        root = Tk()
        root.withdraw()
        if meaning == "":
            meaning += self.__word
        messagebox.showinfo(title, str(meaning))

    def __display_incorrect(self):
        text = FONT.render("INCORRECT", False, (0, 0, 0))
        SCREEN.blit(text, (W/2, 10))
        pygame.display.update()
        pygame.time.delay(800)
        pygame.draw.rect(SCREEN, self.__LIGHT_TEAL, (W/2, 0, 150, 30))
        pygame.display.update()

    def submit_status(self):
        if self.__submission == self.__word:
            self.display_meaning(True)
            self.on_click_new_word()
            return True
        else:
            self.__display_incorrect()
            self.clear_submission()
            return False

    def update_display(self):
        start_x = (1.5*int(W))/len(self.__shuffled_word)
        for i in range(0, len(self.__submission)):
            pygame.draw.rect(SCREEN, BLACK, pygame.Rect(start_x + i * 90, H / 3 - 30, 80, 70))
            letter_font = pygame.font.SysFont('Calibri (Body)', 60)
            letter = letter_font.render(str(self.__submission[i]), False, WHITE)
            SCREEN.blit(letter, (start_x + i * 90 + 20, H / 3 - 20))

        for i in range(0, len(self.__chosen)):
            if self.__chosen[i]:
                pygame.draw.line(SCREEN, self.__RED, (start_x + i * 90, H / 2), (start_x + i * 90 + 80, H / 2 + 70))

    def clear_submission(self):
        start_x = (1.5*int(W))/len(self.__shuffled_word)
        for i in range(0, len(self.__submission)):
            pygame.draw.rect(SCREEN, self.__LIGHT_TEAL, pygame.Rect(start_x + i * 90, H / 3 - 30, 80, 70))
        for i in range(0, len(self.__chosen)):
            self.__chosen[i] = False
        self.__submission = ""
        self.__display_word()

    def get_total(self):
        return self.__total_words
