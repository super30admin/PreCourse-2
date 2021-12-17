# Time Complexity : 
# Best Case: O(N(log(N))) 
# Worst Case: O(N(log(N)))  

# Space Complexity : (Recursion Stack = log(N) + Auxiliarry Array = 1)
# Best, Worst, Average Case = O(log(N))

# Did this code successfully run on Leetcode : N/A
# Any problem you faced while coding this : No
def mergeSort(arr):

  def recur(left, right):
    if left == right:
      return (left, right)

    mid = left + (right - left) // 2

    pBounds = recur(left, mid)    
    qBounds = recur(mid + 1, right)
    
    p = pBounds[0]
    q = qBounds[0]
    qEnd = qBounds[1]

    while p < q and q <= qEnd:
      if arr[p] <= arr[q]: #if ele in left subarray less than ele in right subarray move left pointer up
        p += 1
      else: # rotate the subarray from index [p + 1] to q in the right direction. 
            # Put element that was at q in index location p.
        temp = arr[q] 
        for i in range(q, p, -1):
          arr[i] = arr[i - 1]
        arr[p] = temp
        p += 1
        q += 1
    
    return (left, right) 
    # Always return the left and right because in the call above we want to use these bounds to move elements in place.
  
  recur(0, len(arr) - 1)

  #write your code here
  
# Code to print the list 
def printList(arr): 
  print(arr)
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [4, 2, 1, 4, 3,12, 11, 13, 6, 5, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
