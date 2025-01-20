import pygame
from pygame import Surface
import sys
import numpy as np
import time
pygame.init()

leg = 40
wid = 40
sep_time = 0.1
blocks_sys = np.zeros([leg+2, wid+2])


def load(net):
    net_temp = net.copy()
    for i in range(leg+2):
        for j in range(wid+2):
            if (i == 0 or i == leg+1) or (j == 0 or j == wid+1):
                pass
            else:
                temp_sum = 0
                choices = [0, 1, -1]
                for a in choices:
                    for b in choices:
                        temp_sum += net[i+a][j+b]
                temp_sum -= net[i][j]
                # 获取sum

                if temp_sum == 2:
                    pass
                elif temp_sum == 3:
                    net_temp[i][j] = 1
                else:
                    net_temp[i][j] = 0
    net[:] = net_temp


def main():
    pygame.display.set_caption("生命游戏")
    screen = pygame.display.set_mode([20*leg, 20*wid])
    screen.fill(color='grey')
    # 设置幕布

    blocks = []
    for i in range(leg):
        blocks.append([])
        for j in range(wid):
            blocks[i].append(Surface([16, 16]))

    for i in range(leg):
        for j in range(wid):
            if blocks_sys[i+1][j+1] == 0:
                blocks[i][j].fill(color='white')
            else:
                blocks[i][j].fill(color='black')

    for i in range(leg):
        for j in range(wid):
            screen.blit(blocks[i][j], (20 * i + 2, 20 * j + 2))

    flag = 0
    current_time = time.time()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                x = int(x)//20+1
                y = int(y)//20+1
                blocks_sys[x][y] = not blocks_sys[x][y]
            if event.type == pygame.KEYDOWN:
                flag = not flag
        # 侦测循环

        if time.time()-current_time > sep_time and flag == 1:
            load(blocks_sys)
            current_time = time.time()
        # 演化循环（内容发生改变）

        for i in range(leg):
            for j in range(wid):
                if blocks_sys[i + 1][j + 1] == 0:
                    blocks[i][j].fill(color='white')
                else:
                    blocks[i][j].fill(color='black')
        # 更新颜色
        for i in range(leg):
            for j in range(wid):
                screen.blit(blocks[i][j], (20 * i + 2, 20 * j + 2))
        pygame.display.flip()
        # 贴图刷新 + 帧刷新


if __name__ == '__main__':
    main()
