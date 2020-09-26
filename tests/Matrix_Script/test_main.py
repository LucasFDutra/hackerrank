from hackerrank.Matrix_Script import main

def test_mount_the_word():
    n = 7
    m = 3
    matrix = [
        'Tsi',
        'h%x',
        'i #',
        'sM ',
        '$a ',
        '#t%',
        'ir!'
    ]

    assert main.mount_the_word(matrix, n, m) == 'This$#is% Matrix#  %!'


def test_matrix_decode():
    strings_matrix = ['This$#is% Matrix#  %!', 'Matrix ** is a % good movie!!']
    correct_res = ['This is Matrix#  %!', 'Matrix is a good movie!!']
    for i in range(len(strings_matrix)):
        assert main.matrix_decode(strings_matrix[i]) == correct_res[i]