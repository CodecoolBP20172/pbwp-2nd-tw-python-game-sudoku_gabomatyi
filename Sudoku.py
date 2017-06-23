import os
import random
import datetime
from copy import deepcopy, copy


# waits for an input before continue
def wait():
    input()


# imports sudoku board from files on a choosen level - randomly from three different games on each level
def import_sudoku(sudoku, filename="easy_sudoku.csv", skip=0):
    line_read = 0
    with open(filename, "r") as input_stream:
        for i in range((skip*8)+skip):
            next(input_stream)
        for line in input_stream:
            if line_read == 9:
                break
            line = line.strip("\n")
            current_line = line.split(",")
            sudoku.append(current_line)
            line_read += 1
    return sudoku


# draws the Sudoku title
def title():
    os.system('clear')
    print("   _____           _       _          \n" +
          "  / ____|         | |     | |         \n" +
          " | (___  _   _  __| | ___ | | ___   _ \n" +
          "  \___ \| | | |/ _` |/ _ \| |/ / | | |\n" +
          "  ____) | |_| | (_| | (_) |   <| |_| |\n" +
          " |_____/ \__,_|\__,_|\___/|_|\_\\\\__,_|\n" +
          "                                      \n")


# checks if the fully filled board is correct (1-9 in each row, column and block)
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


# continually checking if the board is full
def check_space_in_board():
    filled_board = True
    for row in range(9):
        for column in range(9):
            if choosen_sudoku[row][column] == " ":
                return False
    return True


# draws the sudoku board
def draw_board():
    title()
    shift_column = 0
    shift_row = 0
    row_number = 1
    print(START_BOLD+START_RED+"      1 2 3   4 5 6   7 8 9"+END_BOLD+END_RED)
    print()
    while shift_column <= 6:
        print("    + - - - + - - - + - - - +", end="\n")
        for row in range(3):
            print(START_BOLD+START_RED, row_number, END_BOLD+END_RED, "|", end=" ")
            row_number += 1
            shift_row = 0
            while shift_row <= 6:
                for column in range(3):
                    if original[row + shift_column][column + shift_row] == " ":
                        print(choosen_sudoku[row + shift_column][column + shift_row], end=" ")
                    else:
                        print(START_GREEN+str(choosen_sudoku[row + shift_column][column + shift_row]) +
                              END_GREEN, end=" ")
                print("|", end=" ")
                shift_row += 3
            print()
        shift_column += 3
    print("    + - - - + - - - + - - - +", end="\n")
    print()


# restart the choosen board if called by the user
def restart_func(choosen_sudoku):
    global restart
    restart = True
    choosen_sudoku = deepcopy(original)
    return choosen_sudoku


# exports the time of the game to an external file with the player's name
def time_export(best_times_dict, filename="times.csv"):
    try:
        with open(filename, "a") as output_stream:
            for name, time in best_times_dict.items():
                output_stream.write("%s- %s" % (name, time))
            output_stream.write("%s- %s\n" % (user_name, user_time))
    except FileNotFoundError:
        with open(filename, "w") as output_stream:
            output_stream.write("%s- %s" % (user_name, user_time))


choosen_sudoku = []
level_dict = {"1": "easy_sudoku.csv", "2": "medium_sudoku.csv", "3": "hard_sudoku.csv"}
choosen_row = ""
choosen_column = ""
user_name = ""
original = []
input_matrix = [["row", "column"], [choosen_row, choosen_column]]
best_times_dict = dict()
START_BLUE = "\u001b[34m"
END_BLUE = "\u001b[0m"
START_PINK = "\u001b[35m"
END_PINK = "\u001b[0m"
START_RED = "\u001b[31m"
END_RED = "\u001b[0m"
START_GREEN = "\u001b[32m"
END_GREEN = "\u001b[0m"
START_BOLD = "\033[1m"
END_BOLD = "\033[0m"


# main
quit = False
restart = False
while not quit:
    while True:
        if exit:
            choosen_sudoku = deepcopy(original)
        os.system('clear')
        title()
        if not user_name:
            user_name = input("Please enter your name: \n")
        print("\nFor row, column and number you can type in numbers from", START_BLUE+"1 to 9"+END_BLUE+".")
        print("If you want to delete a number, press", START_BLUE+"enter"+END_BLUE+" or type", START_BLUE+"\"0\""+END_BLUE+".")
        print("If you want to quit the game or the chosen level, type", START_BLUE, "\"exit\""+END_BLUE+".")
        print("If you want to restart the game, type", START_BLUE+"\"restart\""+END_BLUE+"!\n")
        print("For easy level, press", START_BLUE, "\"1\""+END_BLUE+"!\nFor medium level, press",
              START_BLUE+"\"2\""+END_BLUE+"!\nFor hard level, press", START_BLUE+"\"3\""+END_BLUE+"!")
        print()
        level = input("Please choose level: ")
        start_time = datetime.datetime.now()
        if level in level_dict.keys():
            num = random.randint(0, 2)
            choosen_sudoku = import_sudoku(choosen_sudoku, level_dict[level], num)
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
            print(START_PINK+"\nCORRECT answer, congratulations!!!\n"+END_PINK)
        else:
            draw_board()
            print(START_PINK+"\nWRONG answer, press enter to continue!\n"+END_PINK)
            filled_board = False
            wait()
            os.system('clear')

    while not filled_board and not exit:
        draw_board()
        exit = False

        input_matrix = ["row", "column"]
        restart = False
        for i in range(2):
            value = input("Enter the %s: " % input_matrix[i])
            if str.upper(value) == "EXIT":
                exit = True
                break
            if str.upper(value) == "RESTART":
                choosen_sudoku = restart_func(choosen_sudoku)
                restart = True
                break
            while not (str.isdigit(value)) or (int(value) > 9 or int(value) < 1):
                if str.upper(value) == "EXIT":
                    exit = True
                    break
                value = input("Enter the %s: " % input_matrix[i])
                if str.upper(value) == "RESTART":
                    choosen_sudoku = restart_func(choosen_sudoku)
                    break
            if exit or restart:
                break
            if input_matrix[i] == "row":
                choosen_row = value
            else:
                choosen_column = value
        if exit:
            break
        if not restart:
            choosen_number = input("Enter the number: ")
            if str.upper(choosen_number) == "EXIT":
                exit = True
                break
            if str.upper(choosen_number) == "RESTART":
                choosen_sudoku = restart_func(choosen_sudoku)
                continue
            if (choosen_number == "" or choosen_number == "0"):
                choosen_number = " "
            else:
                while not str.isdigit(choosen_number) or (int(choosen_number) > 9 or int(choosen_number) < 1):
                    if (choosen_number == "" or choosen_number == "0") and original[int(choosen_row) - 1][int(choosen_column) - 1] == " ":
                        choosen_number = " "
                        break
                    if str.upper(choosen_number) == "EXIT":
                        exit = True
                        break
                    if str.upper(choosen_number) == "RESTART":
                        choosen_sudoku = restart_func(choosen_sudoku)
                        restart = True
                        break
                    choosen_number = input("Enter the number: ")
            if exit:
                break
            if restart:
                continue
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
                for row in range(len(choosen_sudoku)):
                    for item in range(len(choosen_sudoku)):
                        choosen_sudoku[row][item] = int(choosen_sudoku[row][item])
                if check_sudoku(choosen_sudoku):
                    draw_board()
                    print(START_PINK+"\nCORRECT answer, congratulations!!!\n"+END_PINK)
                    user_time = datetime.datetime.now() - start_time
                    print("Dear %s, your time is: %s." % (user_name, user_time))
                    time_export(best_times_dict, "results.csv")
                    quit = True
                else:
                    draw_board()
                    print(START_PINK+"\nWRONG answer, press enter to continue!\n"+END_PINK)
                    filled_board = False
                    wait()
                    os.system('clear')
