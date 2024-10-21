# // Time Complexity : O(nlog(n)) mergeSort uses recursion but merge only takes O(n)
# // Space Complexity : O(n) since every sub array takes up additional space
# // Did this code successfully run on Leetcode :NA
# // Any problem you faced while coding this : No
# Python program for implementation of MergeSort 
def mergeSort(arr):
  
  #write your code here
  if len(arr) > 1:              #check if more than 1 element, no? sorted
    l_arr = arr[:len(arr)//2]   #start to mid
    r_arr = arr[len(arr)//2:]   #mid to end

  #recursion
    mergeSort(l_arr)
    mergeSort(r_arr)
   
  #  merge
    i = j = k = 0                             #l-arrindex, r-arrindex, merge-arrindex
    # while loop to compare and 2 to fill subarrays
    while i < len(l_arr) and j < len(r_arr):  # comparison and swap
        if l_arr[i] < r_arr[j]:
          arr[k] = l_arr[i]
          i += 1
        else:
          arr[k] = r_arr[j]
          j+=1
        k+=1

    while i < len(l_arr):                     #copy remaining elements
       arr[k] = l_arr[i]
       i+=1
       k+=1

    while j < len(r_arr):                     #copy remaining elements    
       arr[k] = r_arr[j]
       j+=1
       k+=1

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
