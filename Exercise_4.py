#Time Complexity : O(nlogn)
#Space Complexity : O(n)
#Did this code successfully run on Leetcode : No, I did not run it on leetcode
#Any problem you faced while coding this : I am not perfectly clear on merging


#Your code here along with comments explaining your approach

# Python program for implementation of MergeSort 
def merge(arr,l,m,r):
	#we get the length of left and right sub array and the create two sub arrays of same size
    n1 = m - l + 1
    n2 = r- m 
  	L = [0] * (n1) 
    R = [0] * (n2) 
  
    # Copy data to temp arrays L[] and R[] from original array
    for i in range(0 , n1): 
        L[i] = arr[l + i] 
  
    for j in range(0 , n2): 
        R[j] = arr[m + 1 + j] 
  
    # Merge the temp arrays back into arr[l..r] 
    i, j, k = 0, 0 ,1

    while i < n1 and j < n2 : 
        if L[i] <= R[j]: 
            arr[k] = L[i] 
            i += 1
        else: 
            arr[k] = R[j] 
            j += 1
        k += 1
  
    # Copy any remaining elements of L[]
    while i < n1: 
        arr[k] = L[i] 
        i += 1
        k += 1
  
    # Copy any remaining elements of R[]
    while j < n2: 
        arr[k] = R[j] 
        j += 1
        k += 1

def sort_arr(arr,l,r):
    if l < r: 
    	#getting midpoint
        m = (l+(r-1))//2
        
        sort_arr(arr, l, m) 
        sort_arr(arr, m+1, r)     
        merge(arr, l, m, r) 

    

def mergeSort(arr):
    # find mid point and recurrsively apply merge sort on them
    left = 0
    right = len(arr)-1
    
    sort_arr(arr,left,right)
    
    
def printList(arr):
    for x in arr:
        print(x, end= " ")
    
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is:", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("\n\nSorted array is: ", end="\n") 
    printList(arr) 
