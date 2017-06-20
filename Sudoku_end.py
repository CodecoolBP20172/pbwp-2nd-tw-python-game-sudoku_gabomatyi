import os
from copy import deepcopy, copy

def wait():
    input()

def title():
    print("   _____           _       _          \n"+
          "  / ____|         | |     | |         \n"+
          " | (___  _   _  __| | ___ | | ___   _ \n"+
          "  \___ \| | | |/ _` |/ _ \| |/ / | | |\n"+
          "  ____) | |_| | (_| | (_) |   <| |_| |\n"+
          " |_____/ \__,_|\__,_|\___/|_|\_\\\\__,_|\n"+
          "                                      \n")

def check_sudoku(x):
    for row in x:
        for thing in row:
            if row.count(thing) > 1:
                return False;
    value = len(x)
    eachRow = []
    while value>0:
        for row in x:
            eachRow.append(row[value-1])
        for thing in eachRow:
            if eachRow.count(thing) > 1:
                return False
            else:
                eachRow = []
                value-=1
    q=0
    while q <= 6:
        p=0
        while p <= 6:
            box=[]
            for i in range(3):
                for j in range(3):
                    box.append(x[i+p][j+q])
                    for thing in box:
                        if eachRow.count(thing) > 1:
                            return False
                        else:
                            box=[]
            p+=3
        q+=3
    return True

def check_space():
    null = True
    for i in range(9):
        for j in range(9):
            if block[i][j] == " ":
                return False
    return True


def draw():
    os.system('clear')
    title()
    p = 0
    x = 1
    start = "\033[1m"
    end = "\033[0m"
    print()
    print(start,"         1 2 3   4 5 6   7 8 9", end)
    print()
    while p <= 6:
        print("        + - - - + - - - + - - - +",end="\n")
        for i in range(3):
            print(start,"   ",x,end,"|", end=" ")
            x += 1
            for j in range(3):
                print(block[i+p][j], end=" ")
            print("|", end=" ")
            for j in range(3):
                print(block[i+p][j+3], end=" ")
            print("|", end=" ")
            for j in range(3):
                print(block[i+p][j+6], end=" ")
            print("|")
        p += 3
    print("        + - - - + - - - + - - - +",end="\n")
    print()


sud1 = [[6,7,4,5,8,2,9,1,3],
        [2,1,5,9,4,3,6,8,7],
        [9,8,3," ",6,1,2,4,5],
        [4,9,7,6,5,8,1,3,2],
        [5,3,6,2,1,4,8,7,9],
        [8,2,1,3,9,7," ",6,4],
        [7,6,9,8,3,5,4,2,1],
        [1,5,2,4,7,6,3,9,8],
        [3,4,8,1,2,9,7,5,6]]

sud2 = [[1,7,2,5,4,9,6,8,3],
        [6,4,5,8,7,3,2,1,9],
        [3," ",9,2,6,1,7,4,5],
        [4,9,6,3,2,7,8,5,1],
        [8,1,3,4,5,6,9,7,2],
        [2,5,7,1,9,8,4,3,6],
        [9,6,4,7,1,5,3," ",8],
        [7,3,1,6,8,2,5,9,4],
        [5,2,8,9,3,4,1,6,7]]

sud3 = [[4,2,6,1,3,8,5,7,9],
        [7,3,5,4,2,9,8,6,1],
        [1,8,9,5,6,7,2,3,4],
        [5,1,2,7,4,6," ",8,3],
        [9,6,8,2,5,3,4,1,7],
        [3," ",7,8,9,1,6,2,5],
        [6,5,3,9,7,2,1,4,8],
        [8,7,4,6,1,5,3,9,2],
        [2,9,1,3,8,4,7,5,6]]

block = []

quit = False
while not quit:
    while True:
        os.system('clear')
        title()
        print(" For row, column and number you can type in numbers from 1 to 9.\n If you want to delete a number, press enter or type \"0\".\n If you want to quit the game or the chosen level, type \"exit\".\n")
        print(" For easy level, press \"1\"!\n For medium level, press \"2\"!\n For hard level, press \"3\"!")
        print()
        x = input(" Please choose level: ")
        if x == "1":
            block = deepcopy(sud1)
            break
        elif x == "2":
            block = deepcopy(sud2)
            break
        elif x == "3":
            block = deepcopy(sud3)
            break
        elif str.upper(x) == "EXIT":
            quit=True
            break
        else:
            print(" Invalid input, press enter to continue!")
            wait()

    if quit:
        break
    null = check_space()
    original = deepcopy(block)

    while not null:
        draw()

        r=input(" Enter the row: ")
        if str.upper(r) == "EXIT":
            null=True
            break
        while not str.isdigit(r) or (int(r) > 9 or int(r) < 1):
            r=input(" Enter the row: ")

        c=input(" Enter the column: ")
        if str.upper(c) == "EXIT":
            null=True
            break
        while not str.isdigit(c) or (int(c) > 9 or int(c) < 1):
            c=input(" Enter the column: ")

        number=input(" Enter the number: ")
        if str.upper(number) == "EXIT":
            null=True
            break
        if (number == "" or number == "0"):
            number = " "
        else:
            while not str.isdigit(number) or (int(number) > 9 or int(number) < 1):
                if (number == "" or number == "0") and original[int(r)-1][int(c)-1] == " ":
                    number = " "
                    break
                number=input(" Enter the number: ")


        if original[int(r)-1][int(c)-1] == " ":
            if number != " ":
                block[int(r)-1][int(c)-1] = int(number)
            else:
                block[int(r)-1][int(c)-1] = number
        else:
            if number != " ":
                print(" You cannot change the given numbers, press enter to continue!")
                wait()
            else:
                print(" You cannot delete the given numbers, press enter to continue!")
                wait()
        os.system('clear')
        null=check_space()

        if null:
            if check_sudoku(block)==True:
                draw()
                print("\n CORRECT answer, congratulations!!!\n")
                quit = True
            else:
                draw()
                print("\n WRONG answer, press enter to continue!\n")
                null=False
                wait()
                os.system('clear')
