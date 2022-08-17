# Python program for implementation of MergeSort
# Time Complexity: O(nlogn) 
def mergeSort(arr):
  if len(arr) > 1:
    m = len(arr) // 2
    left_prt = arr[:m]
    right_prt = arr[m:]
    mergeSort(left_prt)
    mergeSort(right_prt)
    temp_1 = temp_2 = temp_3 = 0
    while temp_1 < len(left_prt) and temp_2 < len(right_prt):
      if left_prt[temp_1] < right_prt[temp_2]:
        arr[temp_3] = left_prt[temp_1]
        temp_1 += 1
      else:
        arr[temp_3] = right_prt[temp_2]
        temp_2 += 1
      temp_3 += 1
    
    while temp_1 < len(left_prt):
      arr[temp_3] = left_prt[temp_1]
      temp_1 += 1
      temp_3 += 1
    
    while temp_2 < len(right_prt):
      arr[temp_3] = right_prt[temp_2]
      temp_2 += 1
      temp_3 += 1
  
# Code to print the list 
def printList(arr):
    print(*arr)

# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
