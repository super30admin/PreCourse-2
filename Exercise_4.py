# Python program for implementation of MergeSort 
def mergeSort(arr):
  
  #write your code here
  if len(arr)>1:
    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]
    #keep dividing into two parts
    mergeSort(left)
    mergeSort(right)

    #compare and rearrange
    i,j,k=0,0,0
    while i<len(left) and j<len(right):
      if left[i]<right[j]:
        arr[k]=left[i]
        i+=1
      else:
        arr[k]=right[j]
        j+=1
      k+=1

    if i<len(left):
      while i<len(left):
        arr[k]=left[i]
        i+=1
        k+=1
    if j<len(right):
      while j<len(right):
        arr[k]=right[j]
        j+=1
        k+=1

# Code to print the list 
def printList(arr): 
    
    #write your code here
    for i in arr:
      print(i,end=" ")
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    print()
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 


#Time Complexity: for sorting, O(n log n) where n is number of elements in the list.
#Space complexity: avg case O(log n)