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
    for i, row in enumerate(new_screen):
        for j, _ in enumerate(row):
            if j == len(row) - 1 and i == len(new_screen) - 1:
                continue
            elif j == len(row) - 1 and i < len(new_screen) - 1:
                new_screen[i + 1][0] = l1[i][j]
            elif j < len(row) - 1 and i <= len(new_screen) - 1:
                new_screen[i][j + 1] = l1[i][j] 
            if i == 0 and j == 0:
                new_screen[i][j] = ">"

    return new_screen
                
        
def animate_string():
    a_string = input("String to animate: ")
    length = len(a_string) + 5
    screen = [[">" for _ in range(length)] for _ in range(length)]
    square = length ** 2
    for i, char in enumerate(a_string):
        screen[0][i] = char 
    for _ in range(square - len(a_string)):
        os.system("clear")
        pretty_print(screen)
        screen = next_step(screen)
        time.sleep(0.35)
    os.system("clear")
    pretty_print(screen)
        
animate_string()
