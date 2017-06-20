import os
from copy import deepcopy,copy

def wait():
    input()

def title():
    os.system('clear')
    print("   _____           _       _          \n" +
          "  / ____|         | |     | |         \n" +
          " | (___  _   _  __| | ___ | | ___   _ \n"+
          "  \___ \| | | |/ _` |/ _ \| |/ / | | |\n"+
          "  ____) | |_| | (_| | (_) |   <| |_| |\n"+
          " |_____/ \__,_|\__,_|\___/|_|\_\\\\__,_|\n"+
          "                                      \n")

def check_sudoku(sudoku_board):
    for row in sudoku_board:
        for number in row:
                if row.count(number) > 1:
                    return False;
    value = len(sudoku_board)
    each_row = []
    while value > 0:
        for row in x:
            each_row.append(row[value-1])
        for number in each_row:
            if each_row.count(number) > 1:
                return False
            else:
                each_row = []
                value-=1
        return True
    shift_column = 0
    while shift_column <= 6:
        shift_row = 0
        while shift_row <= 6:
            box = []
            for row in range(3):
                    for column in range(3):
                        box.append(sudoku_board[shift_row+row][shift_column+column])
                        for number in box:
                            if each_row.count(number) > 1:
                                return False
                            else:
                                box = []
            shift_row+=3
        shift_column+=3
    return True


def check_space_in_board():
    filled_board = True
    for row in range(9):
        for column in range(9):
            if block[row][column] == " ":
                return False
    return True

def draw_board():
    title()
    shift_column = 0
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
            for column in range(3):
                print(block[row+shift_column][column], end=" ")
            print("|", end=" ")
            for column in range(3):
                print(block[row+shift_column][column+3], end=" ")
            print("|", end=" ")
            for column in range(3):
                print(block[row+shift_column][column+6], end=" ")
            print("|")
        shift_column += 3
    print("    + - - - + - - - + - - - +",end="\n")
    print()

sud_easy = [[6,7,4,5," "," "," "," ",3],[2,1,5," "," "," "," "," ",7],
       [9," "," ",7," ",1,2," "," "],[" "," ",7," ",5," "," ",3," "],
       [" "," "," ",2," ",4," "," "," "],[" ",2," "," ",9," ",5," "," "],
       [" "," ",9,8," ",5," "," ",1],[1," "," "," "," "," ",3,9,8],
       [3," "," "," "," ",9,7,5,6]]

sud_medium =[[" "," "," "," "," "," ",6,8," "],
      [" "," "," "," ",7,3," "," ",9],
      [3," ",9," "," "," "," ",4,5],
      [4,9," "," "," "," "," "," "," "],
      [8," ",3," ",5," ",9," ",2],
      [" "," "," "," "," "," "," ",3,6],
      [9,6," "," "," "," ",3," ",8],
      [7," "," ",6,8," "," "," "," "],
      [" ",2,8," "," "," "," "," "," "]]

sud_hard =[[4," "," ",1,3," "," ",7," "],
      [" "," "," "," "," "," "," "," "," "],
      [1,8," "," ",6,7," "," "," "],
      [5," "," "," ",4," "," "," "," "],
      [" ",6," "," "," "," ",4," ",7],
      [" "," ",7," "," "," ",6,2," "],
      [" "," ",3,9," "," "," "," ",8],
      [" "," "," "," ",1," ",3," "," "],
      [" "," "," "," "," ",4," ",5," "]]

block = []

#main
quit=False
while not quit:
    while True:
        os.system('clear')
        title()
        print("For row, column and number you can type in numbers from 1 to 9.\nIf you want to delete a number, press enter or type \"0\".\nIf you want to quit the game or the chosen level, type \"exit\".\n")
        print("For easy level, press \"1\"\nFor medium level, press \"2\"\nFor hard level, press \"3\"")
        print()
        x=input("Please choose level: ")
        if x=="1":
            block=deepcopy(sud1)
            break
        elif x=="2":
            block=deepcopy(sud2)
            break
        elif x=="3":
            block=deepcopy(sud3)
            break
        elif str.upper(x)=="EXIT":
            quit=True
            break
        else:
            print("Invalid input,press enter to continue!")
            wait()
    if quit:
        break
    original=deepcopy(block)
    filled_board = check_space_in_board()
    exit=False
    if filled_board:
            if check_sudoku(block)==True:
                draw_board()
                print("\nCORRECT answer, congratulations!!!\n")
            else:
                draw_board()
                print("\nWRONG answer, press enter to continue!\n")
                filled_board=False
                wait()
                os.system('clear')
    while not filled_board and not exit:
        draw_board()
        exit=False

        r=input("Enter the row: ")
        if str.upper(r)=="EXIT":
            filled_board=True
            exit=True
            break
        while not (str.isdigit(r)) or (int(r)>9 or int(r)<1):
            if str.upper(r)=="EXIT":
                filled_board=True
                exit=True
                break
            r=input("Enter the row: ")
        if exit:
            break

        c=input("Enter the column: ")
        if str.upper(c)=="EXIT":
            filled_board=True
            exit=True
            break
        while not (str.isdigit(c)) or (int(c)>9 or int(c)<1):
            if str.upper(c)=="EXIT":
                filled_board=True
                exit=True
                break
            c=input("Enter the column: ")
        if exit:
            break

        number=input("Enter the number: ")
        if str.upper(number)=="EXIT":
            filled_board=True
            break
        if (number == "" or number == "0"):
            number=" "
        else:
            while not str.isdigit(number) or (int(number) > 9 or int(number) < 1):
                if (number == "" or number == "0") and original[int(r)-1][int(c)-1] == " ":
                    number=" "
                    break
                number=input("Enter the number: ")

        if original[int(r)-1][int(c)-1]==" ":
            if number != " ":
                block[int(r)-1][int(c)-1]=int(number)
            else:
                block[int(r)-1][int(c)-1]=number
        else:
            if number!=" ":
                print("You cannot change the given numbers, press enter to continue!")
                wait()
            else:
                print("You cannot delete the given numbers, press enter to continue!")
                wait()

        os.system('clear')
        filled_board=check_space_in_board()
        if filled_board:
            if check_sudoku(block):
                draw_board()
                print("\nCORRECT answer, congratulations!!!\n")
                quit=True
            else:
                draw_board()
                print("\nWRONG answer, press enter to continue!\n")
                filled_board=False
                wait()
                os.system('clear')
