# Python program for implementation of MergeSort
# TIME Complexity: Unfortunately, can't remember
# SPACE Complexity: O(N)
# Did you test in Leetcode: Yes, it passed all test cases
# Any problems faced? Yes, with recursion

def mergeSort(arr):
    low = 0
    high = len(arr)
    if len(arr) > 1:
        mid = (low + high) // 2
        arr[low: mid] = mergeSort(arr[low: mid])
        arr[mid: high] = mergeSort(arr[mid: high])
        arr = merge( arr[low:mid], arr[mid: high] )
        return arr
    return arr

def merge(a, b):
    c = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    if i == len(a):
        c.extend(b[j:len(b)])
    else:
        c.extend(a[i:len(a)])
    return c
  
# Code to print the list 
def printList(arr): 
    print(arr)

  
# driver code to test the above code 
# if __name__ == '__main__':
arr = [12, 11, 13, 5, 6, 7]
print ("Given array is", end="\n")
printList(arr)
arr = mergeSort(arr)
print("Sorted array is: ", end="\n")
printList(arr)
