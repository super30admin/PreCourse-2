# Python program for implementation of MergeSort 
def mergeSort(arr):
  
      # write your code here
      # tc O(n log n), sc O(n + log n = n).
      def divide_and_conquer(array, start, end):
          if start >= end:
              return

          mid = start + ((end - start) // 2)
          divide_and_conquer(start, mid)
          divide_and_conquer(mid+1, end)

          # merge two sorted arrays
          sorted_arrays = []
          i, j = start, mid+1

          while i <= mid and j <= end:
              if array[i] <= array[j]:
                  sorted_arrays.append(array[i])
                  i += 1
              else:
                  sorted_arrays.append(array[j])
                  j += 1

          while i <= mid:
              sorted_arrays.append(array[i])
              i += 1

          while j <= end:
              sorted_arrays.append(array[j])
              j += 1

          array[start:end+1] = sorted_arrays

      divide_and_conquer(arr, 0, len(arr)-1)
  
# Code to print the list 
def printList(arr): 
    
    # write your code here
    sortedlist = []
    for num in arr:
        sortedlist.append(num)
      
    print(sortedlist)
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
