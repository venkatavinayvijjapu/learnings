# Merge Overlapping Sub-intervals
# Problem Statement: Given an array of intervals, merge all the overlapping intervals and return an array of non-overlapping intervals.

from typing  import List
def merge(arr:List[List[int]]):
    n=len(arr)
    arr.sort()
    ans=[]
    for i in range(n):
        if not ans or arr[i][0]>ans[-1][1]:
            ans.append(arr[i])
        else:
            arr[-1][1]=max(ans[-1][1],arr[i][1])
    return ans