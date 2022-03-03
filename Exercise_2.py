# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
from typing import List


# def partition(arr,low,high):
    
  
    #write your code here
  

# Function to do Quick sort 
def quickSort(arr: List[int]): 
    # if low index is greater or equals to the high index return
    if not arr or arr == None: return arr
    if len(arr) <=1:
        return arr
    else: pivot = arr.pop()
    lowArr = []
    highArr = []
    for i in range(len(arr)):
        if pivot > arr[i]:
            lowArr.append(arr[i])
        else:
            highArr.append(arr[i])

    return quickSort(lowArr) + [pivot] + quickSort(highArr)

    #write your code here
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 

arr = quickSort(arr) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
