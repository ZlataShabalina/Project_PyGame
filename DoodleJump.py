import pygame
from pygame.locals import *
import sys
import random
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap


class Hello(QWidget):
    def __init__(self):
        super(Hello, self).__init__()

        self.gamer = 'Jump1.png'
        self.setWindowTitle('Приветствие')
        self.setMinimumWidth(400)
        self.setMinimumHeight(500)

        self.button = QPushButton('Играть', self)
        self.button.resize(80, 25)
        self.button.move(155, 450)

        self.label_1 = QLabel(self)
        self.label_1.setText('Введите свой никнейм')
        self.label_1.move(120, 50)

        self.box1 = QLineEdit(self)
        self.box1.resize(150, 20)
        self.box1.move(125, 80)

        self.label_3 = QLabel(self)
        self.label_3.setText('')
        self.label_3.move(120, 130)

        self.label_2 = QLabel(self)
        self.label_2.setText('Выберете стиль одежды дудла')
        self.label_2.move(100, 200)

        pixmap = QPixmap('Jump1.png')
        self.label_4 = QLabel(self)
        self.label_4.setPixmap(pixmap)
        self.label_4.resize(pixmap.width(), pixmap.height())
        self.label_4.move(25, 250)

        pixmap = QPixmap('Jump2.png')
        self.label_5 = QLabel(self)
        self.label_5.setPixmap(pixmap)
        self.label_5.resize(pixmap.width(), pixmap.height())
        self.label_5.move(150, 250)

        pixmap = QPixmap('Jump3.png')
        self.label_6 = QLabel(self)
        self.label_6.setPixmap(pixmap)
        self.label_6.resize(pixmap.width(), pixmap.height())
        self.label_6.move(275, 250)

        self.check_1 = QRadioButton(self)
        self.check_1.move(80, 350)
        self.check_1.setChecked(True)
        self.check_1.name = 'Jump1.png'

        self.check_2 = QRadioButton(self)
        self.check_2.move(205, 350)
        self.check_2.name = 'Jump2.png'

        self.check_3 = QRadioButton(self)
        self.check_3.move(330, 350)
        self.check_3.name = 'Jump3.png'

    def center(self):  # окно появится в центре экрана
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


class Fin(QWidget):
    def __init__(self):
        super(Fin, self).__init__()

        self.score = 0
        self.name = 'NoName'
        self.setWindowTitle('Информация')
        self.setMinimumWidth(400)
        self.setMinimumHeight(230)

        self.label_4 = QLabel(self)
        self.label_4.setText('Попробуем еще раз?')
        self.label_4.move(80, 180)

        self.button_1 = QPushButton('Да', self)
        self.button_1.resize(80, 25)
        self.button_1.move(100, 220)

        self.button_2 = QPushButton('Нет', self)
        self.button_2.resize(80, 25)
        self.button_2.move(200, 220)

        self.label_1 = QLabel(self)
        self.label_1.setText('')
        self.label_1.move(100, 50)

        self.label_2 = QLabel(self)
        self.label_2.setText('')
        self.label_2.move(170, 100)

        self.label_3 = QLabel(self)
        self.label_3.setText('')
        self.label_3.move(170, 60)

    def center(self):  # окно появится в центре экрана
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


class DoodleJump(QWidget):
    def __init__(self):
        super(DoodleJump, self).__init__()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Doodle Jump')
        self.state = 0
        self.score = 0
        self.gamer = 'Jump1.png'
        self.green = pygame.image.load('greens1.png').convert_alpha()
        self.blue = pygame.image.load('blue1.png').convert_alpha()
        self.PlayerRight = pygame.image.load(self.gamer).convert_alpha()
        self.PlayerLeft = pygame.transform.flip(self.PlayerRight, True, False)
        self.Player = self.PlayerRight
        self.red = pygame.image.load('red.png').convert_alpha()
        self.red1 = pygame.image.load('red1.png').convert_alpha()
        self.platforms = []
        self.playerx = 400
        self.playery = 400
        self.xmovement = 0
        self.jump = 25
        self.gravity = 0
        self.cameray = 0
        self.user = 'NoName'

    def setup(self, user='NoName', gamer='Jump1.png'):
        self.user = user
        self.gamer = gamer
        self.PlayerRight = pygame.image.load(self.gamer).convert_alpha()
        self.PlayerLeft = pygame.transform.flip(self.PlayerRight, True, False)
        self.Player = self.PlayerRight

    def UpdatePlayer(self):
        if not self.jump:
            self.playery += self.gravity
            self.gravity += 1
        elif self.jump:
            self.playery -= self.jump
            self.jump -= 1
        key = pygame.key.get_pressed()
        if key[K_RIGHT]:
            if self.xmovement < 10:
                self.xmovement += 1
                self.Player = self.PlayerLeft
        elif key[K_LEFT]:
            if self.xmovement > -10:
                self.xmovement -= 1
                self.Player = self.PlayerRight
        else:
            if self.xmovement > 0:
                self.xmovement -= 1
            elif self.xmovement < 0:
                self.xmovement += 1
        if self.playerx > 850:
            self.playerx = -50
        if self.playerx < -50:
            self.playerx = 850
        self.playerx += self.xmovement
        if self.playery - self.cameray <= 200:
            self.cameray -= 2

        if self.playery - self.cameray > 550:
            self.state = 1
            w.show_window_2(self.user, self.score)

        self.screen.blit(self.Player, (self.playerx, self.playery - self.cameray))

    def UpdatePlatforms(self):
        for i in self.platforms:
            rect = pygame.Rect(i[0], i[1], self.green.get_width() - 10, self.green.get_height())
            player = pygame.Rect(self.playerx, self.playery, self.Player.get_width() - 10,
                                 self.Player.get_height())
            if rect.colliderect(player) and self.gravity and self.playery < (i[1] - self.cameray):
                if i[2] != 2:
                    self.jump = 15
                    self.gravity = 0
                else:
                    i[-1] = 1
            if i[2] == 1:
                if i[-1] == 1:
                    i[0] += 2
                    if i[0] > 550:
                        i[-1] = 0
                else:
                    i[0] -= 2
                    if i[0] <= 0:
                        i[-1] = 1

    def DrawPlatforms(self):
        for i in self.platforms:
            check = self.platforms[1][1] - self.cameray
            if check > 600:
                self.platforms.append([random.randint(0, 700), self.platforms[-1][1] - 50, random.randint(0, 1), 0])
                self.platforms.pop(0)
            if i[2] == 0:
                self.screen.blit(self.green, (i[0], i[1] - self.cameray))
            elif i[2] == 1:
                self.screen.blit(self.blue, (i[0], i[1] - self.cameray))
            elif i[2] == 2:
                if not i[3]:
                    self.screen.blit(self.red, (i[0], i[1] - self.cameray))
                else:
                    self.screen.blit(self.red1, (i[0], i[1] - self.cameray))

    def GeneratePlatforms(self):
        on = 600
        while on > -100:
            x = random.randint(0, 700)
            platform = random.randint(0, 1000)
            if platform < 600:
                platform = 0
            elif platform < 900:
                platform = 1
            else:
                platform = 2
            self.platforms.append([x, on, platform, 0])
            on -= 50

    def DrawGrid(self):
        for x in range(80):
            pygame.draw.line(self.screen, (222, 222, 222), (x * 12, 0), (x * 12, 600))
            pygame.draw.line(self.screen, (222, 222, 222), (0, x * 12), (800, x * 12))

    def run(self):
        clock = pygame.time.Clock()
        self.GeneratePlatforms()
        while True:
            self.screen.fill((255, 255, 255))
            clock.tick(60)
            self.score += 0.02
            for event in pygame.event.get():
                if event.type == QUIT:
                    w.show_window_3(self.user)
                    self.state = 1
            if self.state == 0:
                self.DrawGrid()
                self.DrawPlatforms()
                self.UpdatePlatforms()
                self.UpdatePlayer()

                pygame.display.flip()


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

    def show_window_1(self):
        self.w1 = Hello()
        self.w1.show()
        self.w1.check_1.toggled.connect(self.onClicked)
        self.w1.check_2.toggled.connect(self.onClicked)
        self.w1.check_3.toggled.connect(self.onClicked)
        self.w1.button.clicked.connect(self.inc_click1)

    def onClicked(self):
        check = self.sender()
        if check.isChecked():
            self.w1.gamer = check.name

    def inc_click1(self):
        user = self.w1.box1.text()
        gamer = self.w1.gamer
        if user == '' or user == ' ':
            self.w1.label_3.setText('Вы не ввели никнейм,\nпопробуйте еще раз.')
            self.w1.label_3.setStyleSheet("font: 87 14pt 'Arial'; color: rgb(255, 0, 0);")
            self.w1.label_3.move(80, 130)
            self.w1.label_3.adjustSize()
        else:
            self.game = DoodleJump()
            self.game.setup(user, gamer)  # передаем имя пользователя и костюм в главное окно
            self.w1.close()
            self.game.run()

    def show_window_2(self, name='Noname', score=0):
        self.w2 = Fin()
        self.w2.name = name
        self.w2.score = str(int(score))
        self.w2.label_1.setText(f'{self.w2.name}, вы набрали')
        self.w2.label_1.adjustSize()
        self.w2.label_1.move(100, 50)

        self.w2.label_2.setText('очков!')
        self.w2.label_2.adjustSize()
        self.w2.label_2.move(170, 100)

        self.w2.label_3.setText(self.w2.score)
        self.w2.label_3.setStyleSheet("font: 87 18pt 'Arial Black'; color: rgb(255, 0, 0);")
        self.w2.label_3.adjustSize()
        self.w2.label_3.move(170, 60)
        self.w2.button_1.clicked.connect(self.click1)
        self.w2.button_2.clicked.connect(self.click2)
        self.w2.show()

    def click1(self):

        self.game.state = 0
        self.game.score = 0
        self.game.GeneratePlatforms()
        self.game.platforms = []
        self.game.playerx = 400
        self.game.playery = 400
        self.game.xmovement = 0
        self.game.jump = 25
        self.game.gravity = 0
        self.game.cameray = 0
        self.w2.close()
        self.game.run()

    def click2(self):
        sys.exit()

    def click3(self):
        self.game.state = 0
        self.w3.close()

    def show_window_3(self, name='NoName'):
        self.w3 = Fin()
        self.w3.button_1.move(100, 120)
        self.w3.button_2.move(200, 120)
        self.w3.label_4.setText(f'{name}, уже уходите?')
        self.w3.label_4.move(100, 60)
        self.w3.button_1.clicked.connect(self.click2)
        self.w3.button_2.clicked.connect(self.click3)
        self.w3.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show_window_1()
    sys.exit(app.exec_())
