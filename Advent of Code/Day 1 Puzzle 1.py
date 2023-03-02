'''
Day 1 Puzzle 1 and 2 of Advent of Code;

Puzzle 1: sort through a text file of split collections 
of numbers and return the largest sum.

'''


with open('input.txt', 'r') as input:
    data = []
    val = 0
    lst1 = []
    for x in input:
        data.append(x)
    for x in data:
        if len(x) > 3:
            val += int(x)
        else:
            lst1.append(val)
            val = 0
print(sorted(lst1))
print(sorted(lst1)[-1:-4:-1])
print("sum: ",sum(sorted(lst1)[-1:-4:-1]))
input.close()
