
# Tic Tac Toe
# It is a Console Game

# import modules
import os
from sys import platform


def clear_console():

    # programin calistirildigi platforma gore,
    # console comutu ekrani temizliyor.

    if platform == "linux" or platform == "linux2":
        os.system('clear')
        print("\n")

    elif platform == "darwin":
        os.system('clear')
        print("\n")

    elif platform == "win32":
        os.system('cls')
        print("\n")

clear_console()


def draw_board():

    board_list = [["-", "-", "-"],
                  ["-", "-", "-"],
                  ["-", "-", "-"]]

    board_theme = "|{}||{}||{}|\n|{}||{}||{}|\n|{}||{}||{}|".format(
        # Board bilgileri veriliyor.
        board_list[0][0], board_list[0][1], board_list[0][2],
        board_list[1][0], board_list[1][1], board_list[1][2],
        board_list[2][0], board_list[2][1], board_list[2][2])

    print(board_theme)

draw_board()


def player_input():
    pass