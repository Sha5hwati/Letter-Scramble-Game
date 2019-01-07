import pygame
from main import screen, w, h, myfont


class SideBar:
    x = 2
    y = 2
    width = int(w / 7) - 4
    height = int(h / 6) - 4
    score = 0
    help_image = pygame.image.load('images/help.PNG')
    help_rect = help_image.get_rect()
    shuffle_image = pygame.image.load('images/shuffle.PNG')
    shuffle_rect = shuffle_image.get_rect()

    def __init__(self):
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, w / 7, h))
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(self.x, self.y, self.width, h - 2))
        self.owl()
        self.scoreboard()
        self.show_score()
        self.shuffle()
        self.help()

    def owl(self):
        owl_image = pygame.image.load('images/owl.PNG')
        owl_image = pygame.transform.scale(owl_image, (self.width, self.height))
        screen.blit(owl_image, (self.x, self.y + 25))

    def scoreboard(self):
        text = myfont.render("Score", False, (0, 0, 0))
        screen.blit(text, (self.width/4 + 10, self.y + self.height + 50))
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(self.x, self.y + 1.3 * self.height + 50, self.width, self.height - 10))
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(self.x + 2, self.y + 1.3 * self.height + 52, self.width - 4, self.height - 14))

    def show_score(self):
        score_font = pygame.font.SysFont('Calibri (Body)', 50)
        score = score_font.render(str(self.score), False, (0, 0, 0))
        screen.blit(score, (self.width / 2 - 10, self.y + 1.5*self.height + 50))

    def shuffle(self):
        self.shuffle_image = pygame.transform.scale(self.shuffle_image, (self.width, self.height))
        screen.blit(self.shuffle_image, (self.x, self.y + 3*self.height + 25))
        self.shuffle_rect = self.shuffle_image.get_rect(x=self.x, y=self.y + 3*self.height + 25)

    def help(self):
        self.help_image = pygame.transform.scale(self.help_image, (self.width, self.height))
        screen.blit(self.help_image, (self.x, self.y + 4*self.height + 50))
        self.help_rect = self.help_image.get_rect(x=self.x, y=self.y + 4*self.height + 50)

    def add_score(self):
        self.score = self.score + 1
        self.show_score()

