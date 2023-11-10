# Python program for implementation of MergeSort 
# Time Complexity : O(nlog n)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# We divide the array into half around the middle element. We keep dividing till the arrays are of length 1(i.e already sorted)
# We recursively call mergesort on both these arrays
# While merging two arrays, we start checking from the leftmost element of both the arrays and compare them
# The smaller element gets added to the merged array and so on.
def mergeSort(arr):
    if len(arr)>1:
      left_arr=arr[:len(arr)//2]
      right_arr=arr[len(arr)//2:]

      mergeSort(left_arr)
      mergeSort(right_arr)

      #Merging step
      i=0 # left_arr index
      j=0 # right_arr index
      k=0 # merged array index

      while i<len(left_arr) and j<len(right_arr):
        if left_arr[i]<right_arr[j]:
          arr[k]=left_arr[i]
          i+=1
        else:
          arr[k]=right_arr[j]
          j+=1
        k+=1
      
      while i<len(left_arr):
        arr[k]=left_arr[i]
        i+=1
        k+=1

      while j<len(right_arr):
        arr[k]=right_arr[j]
        j+=1
        k+=1

  
# Code to print the list 
def printList(arr): 
    for i in arr:
      print(i)
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
