# Python program for implementation of MergeSort 

#-----------------------------------------------------
# Time Complexity : O(nLog n)  ---> n is the number of elements in the array
# Space Complexity : O (n) ---> n is the number of elements in the array
#---------------------------------------------------
def mergeSort(arr):
  
  if len(arr)>1:
    # find mid index
    mid= len(arr)//2
    # left subarray
    L=arr[:mid]
    # right subarray
    R=arr[mid:]
  
    # Sorting the left subarray.
    mergeSort(L)
    # Sorting the right subarray.
    mergeSort(R)

    # initalize left ,right and final answer pointer 
    right=left=ans=0
    

    while left < len(L) and right < len(R):
      if L[left] < R[right]:
        arr[ans]=L[left]
        left+=1
      else:
        arr[ans]=R[right]
        right+=1
      ans+=1

# traversing the remaining left array to add
    while left < len(L):
      arr[ans]=L[left]
      left+=1
      ans+=1

# traversing the remaining right array to add
    while right < len(R):
      arr[ans]=R[right]
      right+=1
      ans+=1
        
         
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
