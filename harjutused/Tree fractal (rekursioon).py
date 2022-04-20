from turtle import *

def tree(length, n):
    if length < (length / n):
        return 0
    forward(length)
    left(45)
    tree(length * 0.5, length / n)
    left(20)
    tree(length * 0.5, length / n)
    right(75)
    tree(length * 0.5, length / n)
    right(20)
    tree(length * 0.5, length / n)
    left(30)
    backward(length)
    return 1


left(90)
backward(30)
tree(200, 4)

