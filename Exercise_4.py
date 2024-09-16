# Also a divide and conquer strategy. We divide the array in to halfs at each level. There will logn levels. We keep dividing until we land at individual elements. While merging two subarrays we merge in such a way that resulting subarray is sorted. 
# T.C = O(nlogn) We divide array in to halfs until we reach single values - there will be logn levels/times halfing the array. Merge operation traverses across all elements once.
# S.C = O(n) at any given point of time. At each divide operation- there will be up to auxilory n extra space being used to store left and right arrays before merging.
def mergeSort(arr):
    if len(arr) < 2:
        return
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    mergeSort(left)
    mergeSort(right)
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            # We make changes to the original array
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    # Checking if any element was left after one of the pointers moved to the end of the array
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

# Code to print the list 
def printList(arr): 
  print(arr)
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
