with open('input_day2.txt') as p:
    data = p
    game_list = []
    for x in data:
        string = x.split()
        game_list.append(string)

score_dict = {
    'X': 0,
    'Y': 3,
    'Z': 6
}

def get_score(gamelist):
    score = 0
    for x in gamelist:
        if (x[0] == 'B' and x[1] == 'X') or (x[0] == 'A' and x[1] == 'Y') or (x[0] == 'C' and x[1] == 'Z'): # play rock
            score += 1 + score_dict[x[1]]
        if (x[0] == 'C' and x[1] == 'X') or (x[0] == 'B' and x[1] == 'Y') or (x[0] == 'A' and x[1] == 'Z'): # play paper
            score += 2 + score_dict[x[1]]
        if (x[0] == 'A' and x[1] == 'X') or (x[0] == 'C' and x[1] == 'Y') or (x[0] == 'B' and x[1] == 'Z'): # play scissors
            score += 3 + score_dict[x[1]]

    return str(score)      

print(get_score(game_list))
