# Python program for implementation of MergeSort 

# Time Complexity: O(nlog n)
# Space Complexity: O(n)

def mergeSort(arr):
  #write your code here
  if len(arr) > 1:
    mid = len(arr)//2
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    mergeSort(left_arr)
    mergeSort(right_arr)

    i = j = k = 0
    while i < len(left_arr) and j < len(right_arr):
      if left_arr[i] <= right_arr[j]:
        arr[k] = left_arr[i]
        i += 1
      else:
        arr[k] = right_arr[j]
        j += 1
      k += 1

    while i < len(left_arr):
      arr[k] = left_arr[i]
      i += 1
      k += 1

    while j < len(right_arr):
      arr[k] = right_arr[j]
      j += 1
      k += 1
  
# Code to print the list 
def printList(arr): 
    #write your code here
    for i in range(0, len(arr)):
       print("Element-",i," : ", arr[i])
    print("\n")
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
