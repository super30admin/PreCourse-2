# Python program for implementation of MergeSort 
# Time Complexity - O(nlogn)
# Space Complexity - O(n) 
# Did this code successfully run on Leetcode :Yes
# Any problem you faced while coding this : No

def mergeSort(arr):
  if len(arr) > 1:
      #if we have array finding mid 
      m = len(arr) //2
      l = arr[:m]
      r = arr[m:]

      mergeSort(l)
      mergeSort(r)
      i = j = k = 0
      # Copy data to the temporary arrays l[] and r[]
      while i < len(l) and j < len(r):
          if l[i] < r[j]:
            arr[k] = l[i]
            i += 1
          else:
            arr[k] = r[j]
            j += 1
          k += 1
        # Checking if any element was left in l[]
      while i < len(l):
          arr[k] = l[i]
          i += 1
          k += 1
  
        # Checking if any element was left in r[]
      while j < len(r):
          arr[k] = r[j]
          j += 1
          k += 1

# Code to print the list 
def printList(arr): 
    for i in arr:
        print(i, end=" ")
    print()

# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
