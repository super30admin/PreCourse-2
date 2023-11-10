# Time Complexity, best case: O(nlog(n)), worst case: O(nlog(n))
# Space complexity, best case: O(n+log(n)), worst case: O(n) #space for the array is log n and extra space for performing merge on n elements is n

# Python program for implementation of MergeSort 
def mergeSort(arr):
  #write your code here
  #we are dividing the array into left and right sub arrays by taking the midpoint
  if len(arr)>1:
      left_arr=arr[:len(arr)//2]
      right_arr=arr[len(arr)//2:]
      #applying mergesort on the left and right sub arrays respectively
      mergeSort(left_arr)
      mergeSort(right_arr)

      #We are initializing the indices
      i=0 #left subarray starting index
      j=0 #right subarray starting index
      k=0 #sorted array starting index

      while i<len(left_arr) and j<len(right_arr):
        #comparing each element of left and right subarray to create a sorted list 
        if left_arr[i]<right_arr[j]:
          arr[k]=left_arr[i]
          i+=1
        else:
          # if element in right subarray is smaller than element in left subarray we add it to the list
          arr[k]=right_arr[j]
          j+=1
        k+=1
      #adding remaining elements in the left subarray to the sorted list
      while i<len(left_arr):
        arr[k]=left_arr[i]
        i+=1
        k+=1
      #adding remaining elements of the right subarray to the sorted list
      while j<len(right_arr):
        arr[k]=right_arr[j]
        j+=1
        k+=1
  return arr
  
# Code to print the list 
def printList(arr): 
    arr_list=[]
    for l in range(len(arr)):
      arr_list.append(arr[l])
    print(arr_list) 
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
