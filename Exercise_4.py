# Python program for implementation of MergeSort 

# Time Complexity : O(log n)
# Space Complexity : O(log n)
# Did this code successfully run on Leetcode : N/A, no Leetcode link
# Any problem you faced while coding this : No

# Code identifies middle of sorted array and recursively searches subarrays for the value
# At the end it merges the sorted subarrays 
# During the merge process, index i represents the number of elements of subarray1 that have been copied to fullArray,
# while index j represents the number of elements of subarray2 that have been copied to fullArray. 
# Assuming subarray1 and subarray2 both have at least one uncopied element, copy the smaller of the two elements being considered. 
# Since i + j objects have been previously copied, the next element is placed in fullArray[i + j]. 
# (For example, when i + j is 0, the next element is copied to S[0]). If we reach the end of one of the sequences, we must copy the next element from the other.

def mergeSort(arr):
  
  #write your code here
  n = len(arr)
  mid = n//2
  subArray1 = arr[0:mid]
  subArray2 = arr[mid:n]

  mergeSort(subArray1)
  mergeSort(subArray2)

  merge(subArray1, subArray2, arr)

def merge(subArray1, subarray2, fullArray):
   i = j = 0
   while i+j < len(fullArray):
      if j == len(subarray2) or (i < len(subArray1) and subArray1[i]<subarray2[j]):
         fullArray[i+j] = subArray1[i]
         i+=1
      else:
         fullArray[i+j] = subarray2[j]
         j+=1
  
# Code to print the list 
def printList(arr): 
    print(arr)
    #write your code here
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
