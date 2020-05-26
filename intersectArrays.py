## Question from leetcode: 
## https://leetcode.com/problems/intersection-of-two-arrays-ii
# Given two arrays, write a function to compute their intersection.

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
########################################

## Test lists of numbers. 
arr1 = [1, 3, 54, 2, 5, 5, 5]
arr2 = [2, 7, 4, 4, 2, 3, 5, 32, 22, 1, 5]

from itertools import repeat
# Check to see if a key (value) is in the dictionary already. 
#  If it isn't, add the key and the value of 1. 
#  If it is, add the value to the current count. 
def checkDict(arr1):
    dict1 = {}
    for elem in arr1: 
        if elem in dict1: 
            dict1[elem] = (dict1[elem]+1)
        else: 
            dict1[elem] = 1 
    return(dict1)

# Create the dictionary with the intersection. Use checkDict()
def detIntersect(arr1, arr2):
    dict1 = checkDict(arr1)
    dict2 = checkDict(arr2)
    dictFin = {}
    if (len(dict1) <= len(dict2)):  # loop through the smaller dict.
        for key in dict1: 
            if key in dict2: 
                tmp1 = min(dict2[key], dict1[key])
                dictFin[key] = tmp1
    else: 
        for key in dict2: 
            if key in dict1: 
                tmp1 = min(dict2[key], dict1[key])
                dictFin[key] = tmp1

    return(dictFin)

# Assemble once the pieces are done to create the list. 
dictFin = detIntersect(arr1, arr2)
listy = []
for key in dictFin:
    listy.extend(repeat(key,dictFin[key]))
print(listy)