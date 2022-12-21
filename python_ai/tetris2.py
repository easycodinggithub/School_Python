import msvcrt
import time
import os
import ctypes
import numpy as np

x = 3
y = 3


def cls():
    os.system('cls')


def gotoxy(x, y):
    ctypes.windll.kernel32.SetConsoleCursorPosition(ctypes.windll.kernel32.GetStdHandle(-11),
                                                    (((y & 0xFFFF) << 0x10) | (x & 0xFFFF)))


def draw_background():
    for j in range(0, 23):
        for i in range(0, 12):
            if background[j, i] == 1:
                print("*", end="")
            else:
                print("-", end="")
        print("")


def make_block():
    for j in range(0, 4):
        for i in range(0, 4):
            if (block_L[j, i] == 1):
                gotoxy(i + x, j + y)
                print("*")


def delete_block():
    for j in range(0, 4):
        for i in range(0, 4):
            if (block_L[j, i] == 1):
                gotoxy(i + x, j + y)
                print("-")


def overlap_check(tx, ty):
    # print(block_L)
    # print(background[ty+y:ty+y+4, tx+x:tx+x+4])

    # overlap_count = np.sum(np.bitwise_and( block_L, background[ty+y:ty+y+4, tx+x:tx+x+4] ))

    # print(block_L)

    # print(background[0 : ty + y, 0 : tx + x])

    # overlap_count = 0

    # for j in range(0, 4):
    #     for i in range(0, 4):
    #         if(block_L[j, i] == 1 and background[j + ty + y, i + tx + x] == 1):
    #             overlap_count += 1
    # return overlap_count
    # print(block_L & background[y + ty : y + ty + 4, x + tx : x + tx + 4])

    # print(np.shape(background[y + ty : y + ty + 4, x + tx : x + tx + 4]))
    tempBackground = np.array(background[y + ty: y + ty + 4, x + tx: x + tx + 4])

    return (np.shape(tempBackground) == np.shape(block_L)) and (np.sum(block_L & tempBackground) <= 0)


background = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
                       ])

block_L = np.array([[0, 0, 0, 0],
                    [0, 1, 0, 0],
                    [0, 1, 1, 1],
                    [0, 0, 0, 0]])
count = 0

draw_background()
make_block()

while True:
    if msvcrt.kbhit():
        key = msvcrt.getch()

        if key == b'a':
            if overlap_check(-1, 0):
                delete_block()
                x -= 1
                make_block()

        elif key == b'd':
            if overlap_check(1, 0):
                delete_block()
                x += 1
                make_block()

        elif key == b's':
            if overlap_check(0, 1):
                delete_block()
                y += 1
                make_block()

    if count == 100:
        if overlap_check(0, 1):
            count = 0
            delete_block()
            y += 1
            make_block()

    count += 1
    time.sleep(0.01)