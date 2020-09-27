from hackerrank.Is_Fibo import main


def test_solve_is_fibo_small_number():
    assert main.solve(1) == 'IsFibo'

def test_solve_is_not_fibo_small_number():
    assert main.solve(4) == 'IsNotFibo'

def test_solve_is_not_fibo_larger_number():
    assert main.solve(223317) == 'IsNotFibo'

def test_solve_is_not_fibo_larger_number():
    assert main.solve(4223318) == 'IsNotFibo'

