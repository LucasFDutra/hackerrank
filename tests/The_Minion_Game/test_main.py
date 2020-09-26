from hackerrank.The_Minion_Game import main


def test_main():
    string = 'BANANA'
    res = main.main(string)
    assert (res == 'Stuart 12')

def test_players_points():
    string = 'BANANA'
    stuart, kevin = main.players_points(string)
    assert (stuart == 12 and kevin == 9)

def test_is_vowels():
    all_letters = 'AEIOUBCDFGHJKLMNPQRSTVWXYZ'
    for i, letter in enumerate(all_letters):
        if (i < 5):
            assert (main.is_vowels(letter) == True)
        else:
            assert (main.is_vowels(letter) == False)
