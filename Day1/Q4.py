# # Kadane’s Algorithm : Maximum Subarray Sum in an Array

# We will run a loop(say i) to iterate the given array.
# Now, while iterating we will add the elements to the sum variable and consider the maximum one.
# If at any point the sum becomes negative we will set the sum to 0 as we are not going to consider it as a part of our answer.

import sys

def max(arr,n):
    maxi=-sys.maxsize-1
    sum=0
    for i in range(n):
        sum+=arr[i]
        if sum>maxi:
            maxi=sum
        if sum<0:
            sum=0
    return maxi