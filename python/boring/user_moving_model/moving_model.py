# coding=utf-8
import time
import pygame
from pygame.locals import *
import random
import math


class Base(object):
    def __init__(self, screen, x, y, width, height):
        # 坐标
        self.x = x
        self.y = y
        # 块本身的高和宽
        self.width = width
        self.height = height
        # 设置要显示内容的窗口
        self.screen = screen


class User(Base):
    def __init__(self, screen, x, y, width, height, image_path, width_of_bg, height_of_bg):
        super(User, self).__init__(screen, x, y, width, height)
        self.image = pygame.image.load(image_path).convert()
        self.width_of_bg = width_of_bg
        self.height_of_bg = height_of_bg
        self.angel = random.randint(0, 360)
        self.flag = random.randint(0,1)

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):

        cur_x = self.x
        cur_y = self.y
        if self.flag == 0:
            cur_x += 1
        else:
            cur_x -= 1
        y_plus = int(math.cos(self.angel)*4)
        y_plus = y_plus if y_plus > 0 else 1
        cur_y += -y_plus if self.angel < 180 else y_plus
        self.x = cur_x
        self.y = cur_y
        flag = False
        if self.y < 0:
            self.y = 0
            flag = True
            self.angel = random.randint(180, 360)
        if self.y > self.height_of_bg:
            self.y = self.height_of_bg-self.height
            flag = True
            self.angel = random.randint(0,180)
        if self.x < 0:
            self.x = 0
            flag = True
            self.flag = 1- self.flag
            self.angel = 360 - random.randint(90, 270)
        if self.x > self.width_of_bg:
            self.x = self.width_of_bg-self.width
            self.flag = 1-self.flag
            flag = True
            self.angel = random.randint(90, 270)


class DataCenter(object):
    def __init__(self, screen, width_of_bg, height_of_bg):
        self.users = []
        # for _ in range(random.randint(10, 20)):
        for _ in range(random.randint(20,40)):
            self.users.append(User(screen,random.randint(0, width_of_bg),random.randint(0, height_of_bg),
                                   10,10, "./resource/dot.png",width_of_bg, height_of_bg))

    def display(self):
        for user in self.users:
            user.display()

    def move(self):
        for user in self.users:
            # print(user.x, user.y, user.angel)
            user.move()


def main():
    # 1. 创建一个窗口，用来显示内容
    screen = pygame.display.set_mode((460, 440), 0, 32)

    # 2. 创建一个和窗口大小的图片，用来充当背景
    background = pygame.image.load("./resource/background.png").convert()
    exit_flag = False
    data_center = DataCenter(screen, 460, 440)
    while not exit_flag:
        # 设定需要显示的背景图
        screen.blit(background, (0, 0))
        # 对鼠标，键盘事件进行监听判断
        for event in pygame.event.get():
            if event.type == QUIT:
                    # 退出
                    exit_flag = True
                    break

        data_center.move()
        data_center.display()
        pygame.display.update()
        time.sleep(0.03)  # 用于控制帧数


if __name__ == "__main__":
    main()
