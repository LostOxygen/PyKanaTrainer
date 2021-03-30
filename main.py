# -*- coding: utf-8 -*-
from PyKanaTrainer.trainer import KanaTrainer
import unicodedata
from curses import wrapper
import curses
import random
import time
import os
import sys


def start(stdscr) -> None:
    #initialize the program and draw the standard screen
    win, rows, cols = initialize_screen()
    rows, cols = rows, cols
    draw_standard_screen(win, rows, cols)
    trainer = KanaTrainer()
    train_method = 0

    win.refresh()

    #display the training methods and their highlighting
    win.addstr(3, int(cols/2)-12, "Choose Training Method:", curses.A_UNDERLINE)
    win.addstr(3, int(cols/2)-12, "[ 1 ] Hiragana "+u"\u2192"+" Romaji", curses.A_NORMAL)
    win.addstr(4, int(cols/2)-12, "[ 2 ] Katakana "+u"\u2192"+" Romaji", curses.A_NORMAL)
    win.addstr(5, int(cols/2)-12, "[ 3 ] Romaji "+u"\u2192"+" Hiragana", curses.A_NORMAL)
    win.addstr(6, int(cols/2)-12, "[ 4 ] Romaji "+u"\u2192"+" Katakana", curses.A_NORMAL)
    win.addstr(7, int(cols/2)-12, "[ 0 ] Exit Trainer", curses.A_NORMAL)

    #catch the keycode to navigate through the menu
    while True:
        key = win.getkey()
        if key == "0":
            try:
                quit_trainer()
            except Exception as e:
                return 1
        elif key == "1":
            train_method = 1
            break
        elif key == "2":
            train_method = 2
            break
        elif key == "3":
            train_method = 3
            break
        elif key == "4":
            train_method = 4
            break

    draw_standard_screen(win, rows, cols)

    #main loop for the trainer
    training_list = list()
    if train_method == 1:
        training_list = trainer.get_random_hiragana_list()
    elif train_method == 2:
        training_list = trainer.get_random_hiragana_list()
    elif train_method == 3:
        training_list = trainer.get_random_romaji_for_hiragana_list()
    elif train_method == 4:
        training_list = trainer.get_random_hiragana_list()
    training_length = len(training_list)

    #iterate over the kana training list
    for iterations in range(training_length):
        win.nodelay(True) #set nodelay=true to type free
        draw_standard_screen(win, rows, cols)
        training_tuple = training_list.pop() #get the char from the list
        character, correct_trans = training_tuple[1], training_tuple[0]
        win.addstr(int(rows/2), int(cols/2), character, curses.A_BOLD) #print the kana and refresh the window
        #win.refresh()

        input_exit = False
        input_str = ""
        while not input_exit:
            win.nodelay(False)
            key = win.getkey()
            if key == "0":
                quit_trainer()
            elif key == ' ':
                input_exit = True
            elif key == '\x08' and len(input_str) > 0:
                input_str = input_str[:-1]
                draw_standard_screen(win, rows, cols)
                win.addstr(int(rows/2), int(cols/2), character, curses.A_BOLD)
                win.addstr(int(rows/2)+1, int(cols/2), input_str, curses.color_pair(3))
                win.refresh()
            else:
                input_str = input_str + str(key)
                input_str = input_str.rstrip()
                win.addstr(int(rows/2)+1, int(cols/2), input_str, curses.color_pair(3))
                win.refresh()

        #display input string and compare to the correct character
        if input_str == correct_trans:
            win.addstr(int(rows/2)+1, int(cols/2), input_str, curses.color_pair(2)) #highlight the input in green if correct
        else:
            win.addstr(int(rows/2)+1, int(cols/2), input_str, curses.color_pair(1)) #else highlight it in red and display the correct answer
            win.addstr(int(rows/2)+3, int(cols/2)-16, "Correct answer: " + correct_trans, curses.color_pair(3))

        win.refresh()
        time.sleep(1)

    quit_trainer()


def draw_standard_screen(win, rows: int, cols: int) -> None:
    #draws the standard interface -> border, key assignment and title
    # if os.name == "nt":
    #     os.system("cls")
    # else:
    #     os.system("clear")
    win.clear()
    win.refresh()
    win.border()
    win.addstr(1, 2, "SPACE to submit input", curses.A_REVERSE)
    win.addstr(2, 2, "0 to exit", curses.A_REVERSE)
    win.addstr(1, int(cols/2)-6, "PyKanaTrainer", curses.A_REVERSE)
    win.refresh()


def initialize_screen():
    #initializes the screen
    rows, cols = curses.LINES, curses.COLS
    rows = int(rows/2)-5
    win = curses.newwin(rows, cols, 0, 0)
    curses.curs_set(0)
    curses.noecho()
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_RED)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_GREEN)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    return win, rows, cols


def quit_trainer() -> None:
    #clear the terminal and exit the program
    curses.endwin()
    sys.exit(0)


if __name__ == '__main__':
    #call the curses wrapper for the main function
    wrapper(start)
