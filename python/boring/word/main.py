# coding:utf-8
import os
import time
import pygame
from pygame.locals import *
import random
from PIL import Image, ImageDraw, ImageFont


class Block(object):
    def __init__(self, screen, name):

        # 设置字母图片默认的位置
        self.x = random.randint(1, 390)
        self.y = 0
        self.name = name
        # 设置要显示内容的窗口
        self.screen = screen
        # 用来保存图片名字
        self.image_path= self.get_path(name)
        self.image = pygame.image.load(self.image_path).convert()

    def out_of_screen(self):
        if self.y > 540:
            return True
        else:
            return False

    def move(self):
        self.y += 3

    def display(self):
        self.screen.blit(self.image,(self.x,self.y))

    @staticmethod
    def get_path(name):
        path = "./resource1/"
        if 'A' <= name <= 'Z':
            name += name
        return path + name + ".gif"

    def the_letter_is_me(self, letter):
        return letter == self.name


class FinalInfo(object):
    def __init__(self, screen, success=True):
        self.screen = screen
        if success:
            self.image_path = './resource1/success.png'
        else:
            self.image_path = './resource1/failure.png'
        self.image = pygame.image.load(self.image_path).convert()

    def display(self):
        self.screen.blit(self.image, (0, 0))


class DataControlCenter(object):
    # 初始化
    def __init__(self, screen):
        self.failure_times = 0
        self.start_time = time.time()
        self.end_time = self.start_time
        self.game_time = 60
        # 记录游戏状态 0表示failure 1 表示正在进行游戏 2 表示成功
        self.status = 1
        self.success_or_failure = False
        self.screen = screen
        self.block_list = []
        self.pop_list= []
        # 生成block的时间间隔(单位: 帧数)
        self.num_flag = 20
        # 现在的帧数
        self.num_now = 0
        self.final_info = None

    def win_or_fail(self):
        """
        检测游戏状态
        :return:
        """
        if self.status == 1:
            self.end_time = time.time()
            if self.end_time - self.start_time > self.game_time and self.failure_times <= 5:
                self.final_info = FinalInfo(self.screen)
                self.status = 2
            elif self.failure_times >= 5:
                self.final_info = FinalInfo(self.screen, success=False)
                self.status = 0

    @staticmethod
    def get_rand_name_of_block():
        return chr(random.choice([random.randint(65, 90), random.randint(97, 122)]))

    # 添加block
    def add_block(self):
        if self.status == 1:
            if self.num_now == self.num_flag:
                self.num_now = 0
                block_to_add = Block(self.screen, self.get_rand_name_of_block())
                self.block_list.append((block_to_add.name, block_to_add))
            else:
                self.num_now += 1

    # 显示图像
    def display(self):
        # 显示block
        if self.status == 1:
            for name, block_buffer in self.block_list:
                block_buffer.display()
        else:
            self.final_info.display()

    # 移动blocks
    def move_blocks(self):
        for name, block in self.block_list:
            block.move()

    def get_blocks_to_delete(self, letter):
        """
        检测符合键盘击中的字母
        :param letter: 键盘输入的字母
        :return:
        """
        if self.status == 1:
            for item in self.block_list:
                if item[0] == letter:
                    self.pop_list.append(item)
                    break

    def get_blocks_out_of_edge(self):
        # 检查越界block
        for item in self.block_list:
            if item[1].out_of_screen():
                self.pop_list.append(item)
                self.failure_times += 1

    def delete_blocks_out_of_edge(self):
        if self.status == 1:
            for item in self.pop_list:
                self.block_list.remove(item)
            self.pop_list = []

    def manage_data(self):
        if self.status == 1:
            # 检查越界block
            self.get_blocks_out_of_edge()
            # 删除越界block和被击中的block
            self.delete_blocks_out_of_edge()

    def destroy_data(self):
        if self.block_list:
            self.block_list = None


def main():
    # 1. 创建一个窗口，用来显示内容
    screen = pygame.display.set_mode((460, 540), 0, 32)
    # 2. 创建一个和窗口大小的图片，用来充当背景
    background = pygame.image.load("./resource1/background.png").convert()
    # 退出标识
    exit_flag = False
    data_control_center = DataControlCenter(screen)
    pygame.display.set_caption("Typing Game")

    while not exit_flag:

        data_control_center.add_block()
        # 设定需要显示的背景图
        screen.blit(background, (0, 0))
        # screen.blit(test_block, (0, 0))
        # 对鼠标，键盘事件进行监听判断
        data_control_center.move_blocks()
        events = pygame.event.get()

        for event in events:
            if event.type == QUIT:
                    # 退出
                    exit_flag = True
                    break
            elif event.type == KEYDOWN :
                try:
                    if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                        letter_received = chr(event.key).upper()
                    else:
                        letter_received = chr(event.key)
                    # 将被击中的block记录在要删除的pop_list中
                    data_control_center.get_blocks_to_delete(letter_received)
                except:
                    pass

        data_control_center.win_or_fail()
        data_control_center.manage_data()
        # 显示block
        data_control_center.display()
        # print data_control_center.status, data_control_center.failure_times

        pygame.display.update()
        time.sleep(0.03)  # 用于控制帧数


def get_images(text, big_or_small, size):
    image = Image.new(mode='RGBA', size=size, color="#ffffff")
    draw_table = ImageDraw.Draw(im=image)
    draw_table.text(xy=(0, 0), text=text.decode("utf-8"), fill='#008B8B', font=ImageFont.truetype('./write3.ttf', 50))
    image.save("./resource1/" + big_or_small + text + '.png', 'PNG')  # 保存在当前路径下，格式为PNG
    image.close()


def get_images_transparent(text, is_big, size):
    image = Image.new(mode='RGBA', size=size, color="#ffffff")
    draw_table = ImageDraw.Draw(im=image)
    draw_table.text(xy=(0, 0), text=text.decode("utf-8"), fill='#008B8B', font=ImageFont.truetype('./write3.ttf', 50))

    content = text*2 if is_big else text
    filename = './resource1/{0}.gif'.format(content)

    # Get the alpha band
    alpha = image.split()[3]

    # Convert the image into P mode but only use 255 colors in the palette out of 256
    im = image.convert('RGB').convert('P', palette=Image.ADAPTIVE, colors=255)

    # Set all pixel values below 128 to 255,
    # and the rest to 0
    mask = Image.eval(alpha, lambda a: 255 if a <= 128 else 0)

    # Paste the color of index 255 and use alpha as a mask
    im.paste(255, mask)
    # The transparency index is 255
    image = image.convert('RGB').convert('P', palette=Image.ADAPTIVE)
    image.save(filename, transparency=255)  # 保存在当前路径下，格式为PNG
    image.close()



if __name__ == "__main__":
    main()

    # get_images_transparent("a", False, (40, 40))
    #`
    # if not os.path.exists("resource1"):
    #     os.mkdir("resource1")
    # for i in range(65, 91):
    #     get_images_transparent(str(chr(i)), True, (40, 40))
    #
    # for i in range(97, 123):
    #     get_images_transparent(str(chr(i)), False, (40, 40))
    # get_images("", "background", (460, 540))
    # get_images("闯关失败", "failure", (460, 540))
    # get_images("闯关成功", "success", (460, 540))
