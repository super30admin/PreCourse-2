# Python program for implementation of MergeSort 
def mergeSort(arr):

  #write your code here
  def merge(arr, left, right):
    m = left + (right-left) // 2
    i,j = left, m+1

    while (i <= m and j <= right):
      if (arr[i] < arr[j]):
        i += 1
      else:
        arr[i], arr[j] = arr[j], arr[i]
        j += 1

    while i < right:
      if arr[i] > arr[i+1]:
        arr[i], arr[i+1] = arr[i+1], arr[i]
      i += 1

        
  def  sort(arr, left, right):
    if left == right:
      return
    
    m = left + (right-left)//2
    sort(arr, left, m)
    sort(arr, m+1, right)
    merge(arr, left, right)

  low, high = 0, len(arr)-1

  if not high > low:
    return arr

  sort(arr, low, high)

# Code to print the list 
def printList(arr): 
    
    #write your code here
    print(" ".join([str(e) for e in arr]))
  
# driver code to test the above code 
if __name__ == '__main__':   
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
