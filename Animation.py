import time
import copy
import os


def pretty_print(ugly_list):
    for row in ugly_list:
        string = ""
        for col in row:
            string += col + " "
        print(string)
        print("    ")
        
        
def next_step(l1):
    new_screen = copy.deepcopy(l1)
    i = 0
    next_val = 0
    for y, row in enumerate(l1):
        string = ""
        for x, col in enumerate(row):
            string += str(i)
            if x == len(row) - 1 and y == len(row) - 1:
                continue
            elif x == len(row) - 1 and y < len(row) - 1:
                new_screen[y + 1][0] = l1[y][x]
            elif x < len(row) - 1 and y <= len(row) - 1:
                new_screen[y][x + 1] = l1[y][x] 
            if x == 0 and y == 0 and col != ">":
                new_screen[y][x] = ">"
    return new_screen
                
        
def animate_string():
    a_string = input("String to animate: ")
    length = len(a_string)
    screen = [[">" for i in range(length)] for j in range(length)]
    square = len(a_string) * len(a_string)
    for frame in range(square - length):
        # os.system("cls")
        for i, char in enumerate(a_string):
            screen[0][i] = char 
        pretty_print(screen)
        screen = next_step(screen)
        time.sleep(0.35)
    # os.system("cls")
    pretty_print(screen)
        
animate_string()