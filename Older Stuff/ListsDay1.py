lang = ["C", "C++", "Python", "Java"]

nums = [3,4,5,6,7,8]
lst = ["Some string", 4, 5, True]

lang[1]

lang[-1] #the length of the list is assumed when using negative numbers

lang[1:3]

lang[0:4:2] # Goes from 0 to 4 jumping by 2

lang[::-1] # Reverses a list

for i in range(len(lang)):
    print(i)

for i, c in enumerate(lang): # Enumerate produces a set of two values, an index and a value (in that order)
    print(i,c)


