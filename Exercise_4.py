# Time Complexity : O(nlogn)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode : 
# Any problem you faced while coding this : No
# Python program for implementation of MergeSort 
def mergeSort(arr):
  
  #write your code here
    if len(arr) > 1:
        #mid point
        mid = len(arr)//2

        #divide the left array elements
        l = arr[:mid]

        #divide the right array elements
        r= arr[mid:]

        #sort first and second half
        mergeSort(l)
        mergeSort(r)

        i=j=k=0
        #merge two halves back together
        while i < len(l) and j < len(r):
            if l[i] <= r[j]:
                arr[k] = l[i]
                i+=1
            else:
                arr[k] = r[j]
                j+=1
            k+=1

        #copying the remaining elements from the left half
        while i < len(l):
            arr[k] = l[i]
            i+=1
            k+=1
        
        #copying remaining elements from right half
        while j < len(r):
            arr[k] = r[j]
            j+=1
            k+=1
            
  
# Code to print the list 
def printList(arr): 
     
    #write your code here
    for i in range(len(arr)):
        print(arr[i], end=" ")
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("\n")
    print("Sorted array is: ", end="\n") 
    printList(arr) 
