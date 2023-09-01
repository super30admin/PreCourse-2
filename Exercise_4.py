# Python program for implementation of MergeSort 
# Time Complexity: O(n * log n)
# Space Complexity: O(n)
def mergeSort(arr):
    #write your code here
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    left = mergeSort(arr[:middle])
    right = mergeSort(arr[middle:])

    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result
  
# Code to print the list 
def printList(arr): 
    #write your code here
    for i in arr:
        print(i, end=" ")

  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    arr = mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
