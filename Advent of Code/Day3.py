'''
Day 3 of Advent of code
Rupsack
'''
values = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
values_list = list(values)

def find_value(char):
    for x, i in enumerate(values_list):
        if char == i:
            return x+1
full_letter = []
total_value = 0
with open('input_3.txt') as f:
    data = f.read()
    i = 0
    three_str_lst = [] 
    for char in range(0, len(data)):
        if i == 3:
            i == 0
            full_letter.append(three_str_lst)
            three_str_lst = [] 
        if data[char] == "\n":
            i += 1
            continue
        three_str_lst.append(data[char])
    base_set = set()
        

#         # length = len(line)
#         # first_half = line[0:int((len(line))/2)]
#         # second_half = line[int((len(line))/2):len(line)-1]
#         # for char in first_half:
#         #     if char in second_half:
#         #         dupe_letter.append(char)
#         #         break
#         # print(length, first_half, ' ',second_half)
            
print(dupe_letter)
# print(data)
# for x in dupe_letter:
#     total_value += find_value(x)
# print(total_value)
'''
cDtZFjDjcMCDDtZFSMCvv DpmsmSRRpmmbSpdPRdTmTsp
mmPpsbZZbbzvzgbrZRPgP MWqtHtqDnGCnMWCDwGHwtwW
cBFBNNccsTLjJjfcjfGDGQtWwFCnCGtqCCQH
TNsTLJlffd ldzvrmbmrPzp

'''