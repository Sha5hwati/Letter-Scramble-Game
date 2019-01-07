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

    def __init__(self):
        screen.fill(self.LIGHT_TEAL)
        self.sidebar = SideBar()
        self.on_click_shuffle()

    def on_click_shuffle(self):
        self.get_word()
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
        ran = random.randint(0, len(words))
        while words[ran] == self.word:
            ran = random.randint(0, len(words))
        print(self.word + " " + words[ran])
        self.shuffled_word = words[ran]

    def display_word(self):
        start_x = (1.5*int(w))/len(self.shuffled_word)
        screen.fill(self.LIGHT_TEAL)
        self.sidebar.__init__()
        for i in range(0, len(self.word)):
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(start_x + i*90, h/2, 80, 70))
            letter_font = pygame.font.SysFont('Calibri (Body)', 60)
            letter = letter_font.render(str(self.shuffled_word[i]), False, (255, 245, 255))
            screen.blit(letter, (start_x + i*90 + 20, h/2 + 10))

