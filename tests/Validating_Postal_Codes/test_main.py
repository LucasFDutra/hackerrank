from hackerrank.Validating_Postal_Codes import main

def test_main():
    postal_codes = ['121426', '110000', '523563', '552523', '54', '100000', '999999', '152313', '152314']
    correct_res = [True, False, True, False, False, False, False, True, True]
    for i in range(len(postal_codes)):
        assert main.main(postal_codes[i]) == correct_res[i]
