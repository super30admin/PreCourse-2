# Python program for implementation of MergeSort 
# time complexity of O(n log n) in all cases
# Space complexity is O(n)

def mergeSort(arr):
      if len(arr) > 1:
        mid = len(arr) // 2   # Finding the mid of the array
        left_half = arr[:mid]  # Divide the array into two halves
        right_half = arr[mid:]

        mergeSort(left_half)  # Recursively sort the first half
        mergeSort(right_half)  # Recursively sort the second half

        i = j = k = 0

        # Copy data to temporary lists left_half[] and right_half[]
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Check if any element was left
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
# Code to print the list 
def printList(arr): 
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
