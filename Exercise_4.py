#Time Complexity - Best, average and worst - O(n log n)
#Space Complexity- O(n)


# Python program for implementation of MergeSort 
def mergeSort(arr):
  
  #write your code here
  if len(arr) > 1:
    mid = len(arr) // 2   #mid point
    left_arr = arr[:mid]
    right_arr = arr[mid:]  #fetch left and right halves
    mergeSort(left_arr)
    mergeSort(right_arr)

    #Merge step
    merged = []
    i = j = 0
    while i < len(left_arr) and j < len(right_arr):
      if left_arr[i] < right_arr[j]:
        merged.append(left_arr[i])
        i += 1
      else:
        merged.append(right_arr[j])
        j += 1

    #Add remaining elements
    merged.extend(left_arr[i:])
    merged.extend(right_arr[j:])
    arr[:] = merged #copy back to original array
  
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
