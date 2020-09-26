def is_vowels(letter):
    vowels = 'AEIOU'
    return letter in vowels

def players_points(string):
    stuart = 0
    kevin = 0
    string_length = len(string)
    for i, s in enumerate(string):
        if is_vowels(s):
            kevin += string_length - i
        else:
            stuart += string_length - i
    return stuart, kevin

def main(string):
    stuart, kevin = players_points(string)

    res = ''
    if (stuart > kevin):
        res = 'Stuart '+str(stuart)
    elif (stuart < kevin):
        res = 'Kevin '+str(kevin)
    else:
        res = 'Draw'

    return res

def minion_game(string):
    print(main(string))
