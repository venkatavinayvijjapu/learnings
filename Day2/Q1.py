# Rotate Image by 90 degree
# Problem Statement: Given a matrix, your task is to rotate the matrix 90 degrees clockwise.

from typing import List
def rotate(List[List[int]]):
    n=len(matrix)
    for i in range(n):
        for j in range(i):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    for i in range(n):
        matrix[i].reverse()