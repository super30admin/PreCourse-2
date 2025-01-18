#Time complexity is O(nlogn) and space complexity is O(n).

# Python program for implementation of MergeSort 
def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    leftArr = arr[left:mid + 1]
    rightArr = arr[mid + 1:right + 1]

    i = j = 0
    k = left

    while i < n1 and j < n2:
        if leftArr[i] < rightArr[j]:
            arr[k]=leftArr[i]
            i+=1
        else:
            arr[k] = rightArr[j]
            j+=1
        k += 1
    while i < n1:
        arr[k] = leftArr[i]
        i+=1
        k+=1
    while j < n2:
        arr[k] = rightArr[j]
        j+=1
        k+=1



def mergeSort(arr):
  
  #write your code here

  if len(arr) > 1:
      mid = len(arr) // 2

      left = arr[:mid]
      right = arr[mid:]


      mergeSort(left)
      mergeSort(right)

      merge(arr, 0, mid - 1, len(arr) - 1)
  
# Code to print the list 
def printList(arr): 
    
    #write your code here

    for i in arr:
        print(i, end=" ")
    print()
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
