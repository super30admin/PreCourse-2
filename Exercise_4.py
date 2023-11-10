# Python program for implementation of MergeSort 
# // Time Complexity : O(nlogn)
# // Space Complexity : O(N)
# // Did this code successfully run on Leetcode : Not Found
# // Any problem you faced while coding this : 
# Needed to look how subarrays can be formed and the indexes that needs to be traversed.


# // Your code here along with comments explaining your approach

# Array is divided into subarrays to a point it cannot be further divided with recursion.
# Then while merging each two blocks are compared, arranged and then merged.
def mergeSort(arr):
        if len(arr) > 1:
            mid = len(arr)//2
            leftArr = arr[0:mid]
            rightArr = arr[mid:len(arr)]
            mergeSort(leftArr)
            mergeSort(rightArr)
            i = j = k = 0
            while i < len(leftArr) and j < len(rightArr):
                if leftArr[i] <= rightArr[j]:
                    arr[k] = leftArr[i]
                    i += 1
                else:
                    arr[k] = rightArr[j]
                    j += 1
                k += 1
# Checking if any element was left
            while i < len(leftArr):
                arr[k] = leftArr[i]
                i += 1
                k += 1
            while j < len(rightArr):
                arr[k] = rightArr[j]
                j += 1
                k += 1
  

  
# Code to print the list 
def printList(arr): 
	for i in range(len(arr)):
		print(arr[i], end=" ")
	print()

    
    #write your code here
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
