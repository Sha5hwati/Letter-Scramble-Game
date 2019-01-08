import pygame
from PyDictionary import PyDictionary
from random_word import RandomWords
from itertools import permutations
import random
from sidebar import *
from main import myfont, screen, w, h

class game:
    dictionary = PyDictionary()
    LIGHT_TEAL = (175, 238, 238)
    LENGTH = 4
    word = ""
    shuffled_word = ""
    submission = ""
    shuffled_word_positions = []
    chosen = []

    def __init__(self):
        screen.fill(self.LIGHT_TEAL)
        self.new_word_icon = pygame.image.load('images/next.png')
        self.new_word_rect = self.new_word_icon.get_rect()
        self.submit_icon = pygame.image.load('images/submit.png')
        self.submit_rect = self.submit_icon.get_rect()
        self.clear_icon = pygame.image.load('images/clear.png')
        self.clear_rect = self.clear_icon.get_rect()
        self.on_click_new_word()

    def on_click_shuffle(self):
        self.shuffle()
        self.display_word()

    def get_meaning(self):
        meanings = ""
        if self.word != "":
            mean = self.dictionary.meaning(str(self.word))
            if mean:
                for keys in mean:
                    val = mean[keys][0]
                    meanings = "" + str(self.word) + ": " + str(val)
        return meanings

    def get_word(self):
        r = RandomWords()
        self.word = r.get_random_word(hasDictionaryDef="true", minLength=3, maxLength=6)
        self.word = self.word.upper()

    def shuffle(self):
        words = list(map("".join, permutations(self.word)))
        ran = random.randint(0, len(words)-1)
        while words[ran] == self.word:
            ran = random.randint(0, len(words)-1)
        print(self.word + " " + words[ran])
        self.shuffled_word = words[ran]

    def clear_word(self):
        start_x = (1.5*int(w))/len(self.word)
        for i in range(0, len(self.word)):
            pygame.draw.line(screen, self.LIGHT_TEAL, (start_x + i*90, h/3 + 50), (start_x + i*90 + 80, h/3 + 50))
            rect = pygame.Rect(pygame.Rect(start_x + i * 90, h / 2, 80, 70))
            pygame.draw.rect(screen, self.LIGHT_TEAL, rect)

    def display_word(self):
        start_x = (1.5*int(w))/len(self.shuffled_word)
        for i in range(0, len(self.word)):
            rect = pygame.Rect(pygame.Rect(start_x + i*90, h/2, 80, 70))
            pygame.draw.rect(screen, (0, 0, 0), rect)
            letter_font = pygame.font.SysFont('Calibri (Body)', 60)
            letter = letter_font.render(str(self.shuffled_word[i]), False, (255, 245, 255))
            screen.blit(letter, (start_x + i*90 + 20, h/2 + 10))
            self.shuffled_word_positions.append(rect)
            self.chosen.append(False)
        self.display_blank()
        self.submit_button()
        self.clear_button()
        self.new_word_button()

    def display_blank(self):
        start_x = (1.5*int(w))/len(self.shuffled_word)
        for i in range(0, len(self.word)):
            pygame.draw.line(screen, (0, 0, 0), (start_x + i*90, h/3 + 50), (start_x + i*90 + 80, h/3 + 50))

    def on_click_new_word(self):
        if len(self.submission) != 0:
            self.clear_submission()
        if len(self.word) != 0:
            self.clear_word()
        self.shuffled_word_positions.clear()
        self.get_word()
        self.shuffle()
        self.display_word()

    def new_word_button(self):
        self.new_word_icon = pygame.transform.scale(self.new_word_icon, (100, 50))
        screen.blit(self.new_word_icon, (w/3, h/2+100))
        self.new_word_rect = self.new_word_icon.get_rect(x=w/3, y=h/2+100)

    def clear_button(self):
        self.clear_icon = pygame.transform.scale(self.clear_icon, (100, 50))
        screen.blit(self.clear_icon, (w / 3 + 130, h / 2 + 100))
        self.clear_rect = self.clear_icon.get_rect(x=w / 3 + 130, y=h / 2 + 100)

    def submit_button(self):
        self.submit_icon = pygame.transform.scale(self.submit_icon, (100, 50))
        screen.blit(self.submit_icon, (w / 3 + 260, h / 2 + 100))
        self.submit_rect = self.submit_icon.get_rect(x=w / 3 + 260, y=h / 2 + 100)

    def check_clicked_shuffled_letters(self, x, y):
        for pos in range(0, len(self.shuffled_word_positions)):
            if self.shuffled_word_positions[pos].collidepoint(x, y):
                if self.chosen[pos] is False:
                    self.submission += self.shuffled_word[pos]
                    self.chosen[pos] = True
                    return True
                if self.chosen[pos]:
                    print("Letter already chosen")
                    return False
        return False

    def update_display(self):
        start_x = (1.5*int(w))/len(self.shuffled_word)
        for i in range(0, len(self.submission)):
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(start_x + i * 90, h / 3 - 30, 80, 70))
            letter_font = pygame.font.SysFont('Calibri (Body)', 60)
            letter = letter_font.render(str(self.submission[i]), False, (255, 245, 255))
            screen.blit(letter, (start_x + i * 90 + 20, h / 3 - 20))

    def clear_submission(self):
        start_x = (1.5*int(w))/len(self.shuffled_word)
        for i in range(0, len(self.submission)):
            pygame.draw.rect(screen, self.LIGHT_TEAL, pygame.Rect(start_x + i * 90, h / 3 - 30, 80, 70))
        for i in range(0, len(self.chosen)):
            self.chosen[i] = False
        self.submission = ""

    def submit_status(self):
        if self.submission == self.word:
            print("Correct submission")
            self.on_click_new_word()
            return True
        else:
            print("Incorrect submission")
            self.clear_submission()
            return False
