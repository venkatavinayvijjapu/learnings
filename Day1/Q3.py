# next_permutation : find next lexicographically greater permutation

#  We can use next_permutation

from typing import List

def next(a):
    n=len(a)
    ind=-1
    for i in range(n-2,-1,-1):
        if a[i]<a[i+1]:
            ind=i
            break
    if ind==-1:
        a.reverse()
        return a
    
    for i in range(n-1,ind,-1):
        if a[i]>a[ind]:
            a[i],a[ind]=a[ind],a[i]
            break
    a[ind+1:]=reversed(a[ind+1:])
    return a