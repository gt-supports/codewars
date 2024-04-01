# https://www.codewars.com/kata/53f0f358b9cb376eca001079/solutions/python
class Ball(object):
    def __init__(self, type="regular"):
        self.ball_type = type


def middle_me(N, X, Y):
    # your code here
    if N % 2 != 0:
        return X
    return f'{Y * (N / 2)}{X}{Y * (N / 2)}'


middle_me(18, 'z', '#')

