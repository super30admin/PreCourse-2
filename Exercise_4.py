# Python program for implementation of Merge Sort 
# Time Complexity: O(n log n)
# Space Complexity: O(n) ]
# Did this code successfully run on Leetcode: N/A
# Any problem you faced while coding this: None

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        # Sort the first half
        mergeSort(left)

        # Sort the second half
        mergeSort(right)

        # Merge the sorted halves
        i = j = k = 0

        # Merge data by sorting based on left[] and right[]
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Check if any element was left in left[]
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        # Check if any element was left in right[]
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


def printList(arr):
    print(arr)
    
  
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
