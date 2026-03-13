# Find the duplicate in an array of N+1 integers
# Problem Statement: Given an array of N + 1 size, where each element is between 1 and N. Assuming there is only one duplicate number, your task is to find the duplicate number.

from typing import List
def findDuplicate(arr: List[int]) -> int:
    n = len(arr)
    freq = [0] * (n + 1)
    for i in range(n):
        if freq[arr[i]] == 0:
            freq[arr[i]] += 1
        else:
            return arr[i]
    return 0