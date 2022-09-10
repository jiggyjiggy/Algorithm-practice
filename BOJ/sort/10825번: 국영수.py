import sys


class Elem:
    def __init__(self, name, korean, english, math):
        self.name = name
        self.korean = korean
        self.english = english
        self.math = math


n = int(sys.stdin.readline())
a = []

for i in range(n):
    inp = sys.stdin.readline().split()
    inp[1:] = map(int, inp[1:])
    a.append(Elem(*inp))

a.sort(key=lambda x: (-x.korean, x.english, -x.math, x.name))

[print(elem.name) for elem in a]
