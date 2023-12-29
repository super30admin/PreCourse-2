
# Time Complexity: O(nlogn)
# Space Complexity: O(n) //  logN due to recursion call stack  and O(N) to merge the final result into a new array => O(n)

# Python program for implementation of MergeSort

def merge(arr1, arr2):
    i = 0
    j = 0
    res = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1
    while i < len(arr1):
        res.append(arr1[i])
        i += 1
    while j < len(arr2):
        res.append(arr2[j])
        j += 1

    return res


def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])

    return merge(left, right)

  
  #write your code here
  
# Code to print the list 
def printList(arr): 
    #write your code here
    print(arr)

# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    arr = mergeSort(arr)
    print("Sorted array is: ", end="\n") 
    printList(arr) 
