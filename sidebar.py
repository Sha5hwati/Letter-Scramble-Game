import pygame
from main import W, H, SCREEN, FONT


class SideBar:
    __x = 2
    __y = 2
    __width = int(W / 7) - 4
    __height = int(H / 6) - 4
    __score = 0

    def __init__(self):
        pygame.draw.rect(SCREEN, (0, 0, 0), pygame.Rect(0, 0, W / 7, H))
        pygame.draw.rect(SCREEN, (255, 255, 255), pygame.Rect(self.__x, self.__y, self.__width, H - 2))
        self.__help_image = pygame.image.load('images/help.PNG')
        self.__shuffle_image = pygame.image.load('images/shuffle.PNG')
        self.help_rect = self.__help_image.get_rect()
        self.shuffle_rect = self.__shuffle_image.get_rect()
        self.__owl()
        self.__scoreboard()
        self.__show_score()
        self.__shuffle()
        self.__help()

    def __owl(self):
        owl_image = pygame.image.load('images/owl.PNG')
        owl_image = pygame.transform.scale(owl_image, (self.__width, self.__height))
        SCREEN.blit(owl_image, (self.__x, self.__y + 25))

    def __scoreboard(self):
        text = FONT.render("Score", False, (0, 0, 0))
        SCREEN.blit(text, (self.__width/4 + 10, self.__y + self.__height + 50))
        outer_rect = pygame.Rect(self.__x, self.__y + 1.3 * self.__height + 50, self.__width, self.__height - 10)
        pygame.draw.rect(SCREEN, (0, 0, 0), outer_rect)
        inner_rect = pygame.Rect(self.__x + 2, self.__y + 1.3 * self.__height + 52, self.__width - 4, self.__height-14)
        pygame.draw.rect(SCREEN, (255, 255, 255), inner_rect)

    def __show_score(self):
        box = pygame.Rect(self.__x + 2, self.__y + 1.3 * self.__height + 52, self.__width - 4, self.__height - 14)
        pygame.draw.rect(SCREEN, (255, 255, 255), box)
        score_font = pygame.font.SysFont('Calibri (Body)', 50)
        score = score_font.render(str(self.__score), False, (0, 0, 0))
        SCREEN.blit(score, (self.__width / 2 - 10, self.__y + 1.5*self.__height + 50))

    def __shuffle(self):
        self.__shuffle_image = pygame.transform.scale(self.__shuffle_image, (self.__width, self.__height))
        SCREEN.blit(self.__shuffle_image, (self.__x, self.__y + 3*self.__height + 25))
        self.shuffle_rect = self.__shuffle_image.get_rect(x=self.__x, y=self.__y + 3*self.__height + 25)

    def __help(self):
        self.__help_image = pygame.transform.scale(self.__help_image, (self.__width, self.__height))
        SCREEN.blit(self.__help_image, (self.__x, self.__y + 4*self.__height + 50))
        self.help_rect = self.__help_image.get_rect(x=self.__x, y=self.__y + 4*self.__height + 50)

    def add_score(self):
        self.__score = self.__score + 1
        self.__show_score()

    def get_score(self):
        return self.__score
