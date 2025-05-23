# Time Complexity - O(n log n)
# Space Complexity - O(n)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this - multiple problems

# Python program for implementation of MergeSort 
def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    arrLeft =  mergeSort(arr[:mid])
    arrRight = mergeSort(arr[mid:])
    return merge(arrLeft, arrRight)
    
def merge(arrLeft, arrRight):
    result = []
    i = 0
    j = 0    
    while i < len(arrLeft) and j < len(arrRight):
        if arrLeft[i] <= arrRight[j]:
            result.append(arrLeft[i])
            i += 1
        else:
            result.append(arrRight[j])
            j += 1
            
    for k in range(i, len(arrLeft)):
        result.append(arrLeft[k])
    for g in range(j, len(arrRight)):
        result.append(arrRight[g])
        
    return result
  
# Code to print the list 
def printList(arr): 
    #write your code here
    print(arr)
 
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    sorted_arr = mergeSort(arr)
    print("Sorted array is: ", end="\n") 
    printList(sorted_arr) 
