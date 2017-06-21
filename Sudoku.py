import os
from copy import deepcopy, copy


def wait():
    input()


def title():
    os.system('clear')
    print("   _____           _       _          \n" +
          "  / ____|         | |     | |         \n" +
          " | (___  _   _  __| | ___ | | ___   _ \n" +
          "  \___ \| | | |/ _` |/ _ \| |/ / | | |\n" +
          "  ____) | |_| | (_| | (_) |   <| |_| |\n" +
          " |_____/ \__,_|\__,_|\___/|_|\_\\\\__,_|\n" +
          "                                      \n")


def check_sudoku(sudoku_board):
    for row in sudoku_board:
        for number in row:
            if row.count(number) > 1:
                return False
    value = len(sudoku_board)
    each_row = []
    while value > 0:
        for row in sudoku_board:
            each_row.append(row[value - 1])
        for number in each_row:
            if each_row.count(number) > 1:
                return False
            each_row = []
            value -= 1
        return True
    shift_column = 0
    while shift_column <= 6:
        shift_row = 0
        while shift_row <= 6:
            box = []
            for row in range(3):
                for column in range(3):
                    box.append(sudoku_board[shift_row + row][shift_column + column])
                    for number in box:
                        if each_row.count(number) > 1:
                            return False
                        box = []
            shift_row += 3
        shift_column += 3
    return True


def check_space_in_board():
    filled_board = True
    for row in range(9):
        for column in range(9):
            if choosen_sudoku[row][column] == " ":
                return False
    return True


def draw_board():
    title()
    shift_column = 0
    shift_row = 0
    row_number = 1
    start_bold = "\033[1m"
    end_bold = "\033[0m"
    print(start_bold, "     1 2 3   4 5 6   7 8 9", end_bold)
    print()
    while shift_column <= 6:
        print("    + - - - + - - - + - - - +", end="\n")
        for row in range(3):
            print(start_bold, row_number, end_bold, "|", end=" ")
            row_number += 1
            shift_row = 0
            while shift_row <= 6:
                for column in range(3):
                    print(choosen_sudoku[row + shift_column][column + shift_row], end=" ")
                print("|", end=" ")
                shift_row += 3
            print()
        shift_column += 3
    print("    + - - - + - - - + - - - +", end="\n")
    print()


sud_easy = [[6, 7, 4, 5, " ", " ", " ", " ", 3],
            [2, 1, 5, " ", " ", " ", " ", " ", 7],
            [9, " ", " ", 7, " ", 1, 2, " ", " "],
            [" ", " ", 7, " ", 5, " ", " ", 3, " "],
            [" ", " ", " ", 2, " ", 4, " ", " ", " "],
            [" ", 2, " ", " ", 9, " ", 5, " ", " "],
            [" ", " ", 9, 8, " ", 5, " ", " ", 1],
            [1, " ", " ", " ", " ", " ", 3, 9, 8],
            [3, " ", " ", " ", " ", 9, 7, 5, 6]]

sud_medium = [[" ", " ", " ", " ", " ", " ", 6, 8, " "],
              [" ", " ", " ", " ", 7, 3, " ", " ", 9],
              [3, " ", 9, " ", " ", " ", " ", 4, 5],
              [4, 9, " ", " ", " ", " ", " ", " ", " "],
              [8, " ", 3, " ", 5, " ", 9, " ", 2],
              [" ", " ", " ", " ", " ", " ", " ", 3, 6],
              [9, 6, " ", " ", " ", " ", 3, " ", 8],
              [7, " ", " ", 6, 8, " ", " ", " ", " "],
              [" ", 2, 8, " ", " ", " ", " ", " ", " "]]

sud_hard = [[4, " ", " ", 1, 3, " ", " ", 7, " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            [1, 8, " ", " ", 6, 7, " ", " ", " "],
            [5, " ", " ", " ", 4, " ", " ", " ", " "],
            [" ", 6, " ", " ", " ", " ", 4, " ", 7],
            [" ", " ", 7, " ", " ", " ", 6, 2, " "],
            [" ", " ", 3, 9, " ", " ", " ", " ", 8],
            [" ", " ", " ", " ", 1, " ", 3, " ", " "],
            [" ", " ", " ", " ", " ", 4, " ", 5, " "]]

choosen_sudoku = []

level_dict = {"1": sud_easy, "2": sud_medium, "3": sud_hard}
choosen_row = ""
choosen_column = ""
input_matrix = [["row", "column"], [choosen_row, choosen_column]]

# main
quit = False
while not quit:
    while True:
        os.system('clear')
        title()
        print("For row, column and number you can type in numbers from 1 to 9.")
        print("If you want to delete a number, press enter or type \"0\".")
        print("If you want to quit the game or the chosen level, type \"exit\".\n")
        print("For easy level, press \"1\"\nFor medium level, press \"2\"\nFor hard level, press \"3\"")
        print()
        level = input("Please choose level: ")
        if level in level_dict.keys():
            choosen_sudoku = deepcopy(level_dict[level])
            break
        elif str.upper(level) == "EXIT":
            quit = True
            break
        else:
            print("Invalid input,press enter to continue!")
            wait()
    if quit:
        break
    original = deepcopy(choosen_sudoku)
    filled_board = check_space_in_board()
    exit = False
    if filled_board:
        if check_sudoku(choosen_sudoku):
            draw_board()
            print("\nCORRECT answer, congratulations!!!\n")
        else:
            draw_board()
            print("\nWRONG answer, press enter to continue!\n")
            filled_board = False
            wait()
            os.system('clear')
    while not filled_board and not exit:
        draw_board()
        exit = False

        input_matrix = ["row", "column"]
        for i in range(2):
            value = input("Enter the %s: " % input_matrix[i])
            if str.upper(value) == "EXIT":
                filled_board = True
                exit = True
                break
            while not (str.isdigit(value)) or (int(value) > 9 or int(value) < 1):
                if str.upper(value) == "EXIT":
                    filled_board = True
                    exit = True
                    break
                value = input("Enter the %s: " % input_matrix[i])
            if exit:
                break
            if input_matrix[i] == "row":
                choosen_row = value
            else:
                choosen_column = value

        choosen_number = input("Enter the number: ")
        if str.upper(choosen_number) == "EXIT":
            filled_board = True
            break
        if (choosen_number == "" or choosen_number == "0"):
            choosen_number = " "
        else:
            while not str.isdigit(choosen_number) or (
                    int(choosen_number) > 9 or int(choosen_number) < 1):
                if (choosen_number == "" or choosen_number == "0") and original[int(choosen_row) - 1][int(choosen_column) - 1] == " ":
                    choosen_number = " "
                    break
                choosen_number = input("Enter the number: ")

        if original[int(choosen_row) - 1][int(choosen_column) - 1] == " ":
            if choosen_number != " ":
                choosen_sudoku[int(choosen_row) -
                               1][int(choosen_column) -
                                  1] = int(choosen_number)
            else:
                choosen_sudoku[int(choosen_row) -
                               1][int(choosen_column) -
                                  1] = choosen_number
        else:
            if choosen_number != " ":
                print("You cannot change the given numbers, press enter to continue!")
                wait()
            else:
                print("You cannot delete the given numbers, press enter to continue!")
                wait()

        os.system('clear')
        filled_board = check_space_in_board()
        if filled_board:
            if check_sudoku(choosen_sudoku):
                draw_board()
                print("\nCORRECT answer, congratulations!!!\n")
                quit = True
            else:
                draw_board()
                print("\nWRONG answer, press enter to continue!\n")
                filled_board = False
                wait()
                os.system('clear')
