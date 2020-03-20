# coding=utf-8
import time
import pygame
from pygame.locals import *

class Block(object):
    def __init__(self, screen, x, y, width, height, path):
        self.name = path.split("/")[-1]
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.image.load(path).convert()

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

class Chess(object):

    def __init__(self, screen):
        self.width_of_chessboard = 698
        self.height_of_chessboard = 758
        self.width_of_chess = 50
        self.height_of_chess = 50
        self.width_of_square = 70
        self.height_of_square = 70
        self.x = 71-25
        self.y = 69-25
        self.red_chess_info = {(0, 0):(1, (1,2,3,4,5,4,3,2,1)),
                       (1,2): (6, (6,6)),
                       (0, 3): (2, (7,7,7,7,7)),
                       }
        self.black_chess_info = {(0, 9):(1, (1,2,3,4,5,4,3,2,1)),
                               (1,7): (6, (6,6)),
                               (0,6): (2, (7,7,7,7,7)),
                               }
        self.red_chess = []
        self.black_chess = []
        for (dx, dy), (width, names) in self.red_chess_info.items():
            x = self.x + dx*self.width_of_square
            y = self.y + dy*self.height_of_square
            for i, name in enumerate(names):
                name = name*10 + name
                self.red_chess.append(Block(screen, x+width*i*self.width_of_square, y, self.width_of_chess, self.height_of_chess, "./resource/{0}.gif".format(name)))
        for (dx, dy), (width, names) in self.black_chess_info.items():
            x = self.x+dx*self.width_of_square
            y = self.y + dy*self.height_of_square
            for i, name in enumerate(names):
                self.black_chess.append(Block(screen, x+width*i*self.width_of_square, y, self.width_of_chess, self.height_of_chess, "./resource/{0}.png".format(name)))


    def display(self):
        for chess in self.red_chess:
            chess.display()
        for chess in self.black_chess:
            chess.display()

    def get_pos(self, x, y):
        for i in range(9):
            for j in range(10):
                if self.x+ i*self.width_of_square<= x < self.x+(i+1)*self.width_of_square and  \
                    self.y+ j*self.width_of_square<= y < self.y+(j+1)*self.width_of_square:
                    return self.x+ i*self.width_of_square, self.y+ j*self.width_of_square
        return -1, -1
    def get_clicked_block(self, x, y):
        for block in self.red_chess+self.black_chess:
            if block.x <= x < block.x + block.width and block.y <= y < block.y + block.height:
                return block
        return None
    def remove_block(self, x, y):
        block = self.get_clicked_block(x, y)
        if block in self.red_chess:
            self.red_chess.remove(block)
        if block in self.black_chess:
            self.black_chess.remove(block)


def main():
    # 1. 创建一个窗口，用来显示内容
    screen = pygame.display.set_mode((698, 758), 0, 32)

    # 2. 创建一个和窗口大小的图片，用来充当背景
    background = pygame.image.load("./resource/background1.png").convert()

    exit_flag = False
    old_left = False
    old_right = False
    left_clicked = False
    block = None
    chess_board = Chess(screen)
    while not exit_flag:

        # 设定需要显示的背景图
        screen.blit(background, (0, 0))
        # 对鼠标，键盘事件进行监听判断
        for event in pygame.event.get():

            if event.type == QUIT:
                    # 退出
                    exit_flag = True
                    break
            left, center, right = pygame.mouse.get_pressed()
            # print left, center, right
            x, y = pygame.mouse.get_pos()
            if old_right and (not right):
                chess_board.remove_block(x, y)
            elif old_left and (not left):  # 左键点击
                print("left  clicked")
                if left_clicked:
                    x, y = chess_board.get_pos(x, y)
                    if (x , y) != (-1, -1):
                        print(x, y, block.name)
                        block.x = x
                        block.y = y
                        left_clicked = False
                        block = None
                else:
                    block = chess_board.get_clicked_block(x, y)
                    if block:
                        print(block.name)
                        left_clicked = True
            old_left = left
            old_right = right
        chess_board.display()
        pygame.display.update()
        time.sleep(0.03)  # 用于控制帧数


if __name__ == "__main__":
    main()

