"""
// Time Complexity :  O(nlogn), where n is the number of elements in the array
// Space Complexity : O(n)
// Did this code successfully run on Leetcode : not on leetcode
// Any problem you faced while coding this : No
"""


# Python program for implementation of MergeSort 
def merge(arr,a,b): # function to merge 2 sorted lists a and b
  i=0
  j=0
  k=0
  
  while i<len(a) and j<len(b): #loop runs until one of the lists exhausts 
    if a[i] < b[j]: #checks if ith element in 'a' is smaller than jth element in 'b' and adds it to the merged list if true
      arr[k] = a[i] 
      i+=1
    else:
      arr[k] = b[j] #else add b[j] to the merged list
      j+=1
    k+=1

  while i < len(a): #loop for when there are elements remaining in the 'a' list, adds remaining values to the merged list
    arr[k] = a[i] 
    i+=1
    k+=1
          
  while j < len(b): #loop for when there are elements remaining in the 'b' list, adds remaining values to the merged list
    arr[k] = b[j] 
    j+=1
    k+=1
  
def mergeSort(arr):
  
  #write your code here
    l=0
    h=len(arr)-1

    if l<h:
      #print("here")
      mid = len(arr)//2 #find mid
      a=arr[:mid] #create 2 lists, from low to mid-1 and mid to high
      b=arr[mid:]
      mergeSort(a)
      mergeSort(b)
      merge(arr,a,b) #call merge() to merge the 2 lists

# Code to print the list 
def printList(arr): 
    
    #write your code here
    print(arr)
    
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
