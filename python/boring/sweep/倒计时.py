# coding=utf-8
import time
import pygame
from pygame.locals import *
import random
from PIL import Image, ImageDraw, ImageFont


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


class Buttom(Base):
    def __init__(self, screen, x, y, width, height, image_path):
        super(Buttom, self).__init__(screen, x, y, width, height)
        self.image = pygame.image.load(image_path).convert()

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))


class CalcOfTime(object):
    def __init__(self, screen):
        self.screen = screen
        self.grade = None

    def display(self):
        self.grade.display()

    def generate_photo_of_grade(self, grade):
        image = Image.new(mode='RGBA', size=(281, 60), color="#ffffff")
        draw_table = ImageDraw.Draw(im=image)
        draw_table.text(xy=(0, 0), text=grade, fill='#000000', font=ImageFont.truetype('./resource/fang_song.ttf', 20))
        image.save('./resource/grade.png', 'PNG')
        image.close()
        self.grade = Buttom(self.screen, 162, 206, 0, 0, "./resource/grade.png")


def main():
    # 1. 创建一个窗口，用来显示内容
    screen = pygame.display.set_mode((460, 440), 0, 32)

    # 2. 创建一个和窗口大小的图片，用来充当背景
    background = pygame.image.load("./resource/background.png").convert()
    cot = CalcOfTime(screen)
    exit_flag = False

    while not exit_flag:

        # 设定需要显示的背景图
        screen.blit(background, (0, 0))
        # 对鼠标，键盘事件进行监听判断
        for event in pygame.event.get():

            if event.type == QUIT:
                    # 退出
                    exit_flag = True
                    break
        cot.generate_photo_of_grade(u"离2020年1月1日：\n还有222天2小时32分29秒！")
        cot.display()
        pygame.display.update()
        time.sleep(0.03)  # 用于控制帧数


if __name__ == "__main__":
    main()
