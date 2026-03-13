# # Stock Buy And Sell
# # Problem Statement: You are given an array of prices where prices[i] is the price of a given stock on an ith day.

# Approach:

# Create a variable maxPro and store 0 initially.
# Create a variable minPrice and store some larger value(ex: MAX_VALUE) value initially.
# Run a for loop from 0 to n.
# Update the minPrice if it is greater than the current element of the array
# Take the difference of the minPrice with the current element of the array and compare and maintain it in maxPro.
# Return the maxPro.

def profit(arr):
    maxi=0
    maini=float('inf')
    for i in range(len(arr)):
        maini=min(maini,arr[i])
        maxi=max(maxi,arr[i]-maini)
    return maxi