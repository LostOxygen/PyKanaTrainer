# -*- coding: utf-8 -*-
from PyKanaTrainer.trainer import KanaTrainer
from curses import wrapper
from typing import Union
import curses
import random
import time
import os
import sys


def start(stdscr) -> None:
    #initialize the program and draw the standard screen
    win, rows, cols = initialize_screen()
    draw_standard_screen(win, rows, cols)
    train_method = 0

    #startscreen menu loop
    while True:
        win.refresh()
        #catch the keycode to navigate through the menu
        key = win.getch()
        if key == ord("q"):
            try:
                quit_trainer()
            except Exception as e:
                return 1
        elif key == curses.KEY_DOWN:
            train_method = (train_method+1) % 4
        elif key == curses.KEY_UP:
            train_method = (train_method-1) % 4
        elif key == ord("e"):
            break
        #display the training methods and their highlighting
        win.addstr(int(rows/2)-10, int(cols/2)-11, "Choose Training Method:", curses.A_UNDERLINE)
        win.addstr(int(rows/2)-8, int(cols/2)-12, "[ 1 ] Hiragana "+u"\u2192"+" Romaji", curses.A_REVERSE if train_method is 0 else curses.A_NORMAL)
        win.addstr(int(rows/2)-6, int(cols/2)-12, "[ 2 ] Katakana "+u"\u2192"+" Romaji", curses.A_REVERSE if train_method is 1 else curses.A_NORMAL)
        win.addstr(int(rows/2)-4, int(cols/2)-12, "[ 3 ] Romaji "+u"\u2192"+" Hiragana", curses.A_REVERSE if train_method is 2 else curses.A_NORMAL)
        win.addstr(int(rows/2)-2, int(cols/2)-12, "[ 4 ] Romaji "+u"\u2192"+" Katakana", curses.A_REVERSE if train_method is 3 else curses.A_NORMAL)

    win.clear()
    draw_standard_screen(win, rows, cols)
    train_loop(train_method)

    quit_trainer()



def train_loop(train_method: int) -> None:
    #main loop for the trainer
    time.sleep(5)


def handle_input() -> None:
    #helper function to handle the input
    pass


def draw_standard_screen(win, rows: int, cols: int) -> None:
    #draws the standard interface -> border, key assignment and title
    win.border()
    win.addstr(1, 2, "Press Q to exit", curses.A_REVERSE)
    win.addstr(2, 2, "Press E to select", curses.A_REVERSE)
    win.addstr(3, 2, "Use ▲ and ▼ to move selection", curses.A_REVERSE)
    win.addstr(2, 2, "Press E to select", curses.A_REVERSE)
    win.addstr(1, int(cols/2)-6, "PyKanaTrainer", curses.A_REVERSE)
    win.refresh()


def initialize_screen():
    #initializes the screen
    rows, cols = curses.LINES, curses.COLS
    win = curses.newwin(rows, cols, 0, 0)
    curses.curs_set(0)
    curses.noecho()
    win.nodelay(1)
    #win.timeout(1000)
    win.keypad(True)
    return win, rows, cols


def quit_trainer() -> None:
    #clear the terminal and exit the program
    curses.endwin()
    sys.exit(0)


if __name__ == '__main__':
    #call the curses wrapper for the main function
    wrapper(start)
