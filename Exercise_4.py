# Time Complexity : 0(n*log(n))
# Space Complexity :O(n)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this :No

# Python program for implementation of MergeSort 
def merge(A,B): # Merge two sorted list A and B
    (m,n) = (len(A),len(B))
    (C,i,j) = ([],0,0)
    
    #Case 1 :- When both lists A and B have elements for comparing
    while i < m and j < n:
        if A[i] <= B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
    
    #Case 2 :- If list B is over, shift all elements of A to C 
    while i < m:
        C.append(A[i])
        i += 1
    
    #Case 3 :- If list A is over, shift all elements of B to C 
    while j < n:
        C.append(B[j])
        j += 1
    
    # Return sorted merged list   
    return C




def mergeSort(arr):  #Recursive MergeSort
  n=len(arr)  
  if n<=1:
      return(arr)
  left=mergeSort(arr[0:n//2])
  right=mergeSort(arr[n//2:])
  
  return(merge(left,right)) # Return Merge of two sorted list l and r
  
  
  
# Code to print the list 
def printList(arr): 
    
    for i in arr:
      print(i)
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    arr=mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
