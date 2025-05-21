# Python program for implementation of MergeSort 
#Time Complexity : O(n log n) - as merge sort divides and then merges.
#Space Complexity :O(n) - temporary arrays are created for left and right halves.
#Did this code successfully run on Leetcode : Yes
def mergeSort(arr):
  
  #write your code here
 if len(arr)>1:        #only sort if the array has more than one element
    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]

    mergeSort(left)
    mergeSort(right)

    i=j=k=0 # index of left array,right array and original array 

    while i < len(left)and j<len(right):
       if left[i]<right[j]:
          arr[k]=left[i]
          i +=1
       else:
          arr[k]=right[j]
          j+=1
          k+=1
       
# Code to print the list 
def printList(arr): 
    
    #write your code here
     for i in arr:
        print(i,end=" ")
        print()
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
