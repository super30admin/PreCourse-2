# Python program for implementation of MergeSort 
def mergeSort(arr):
  
  #write your code here
  #Merge sort works on divide and conquer approach
  #Time complexity for merge sort in all cases comes to be O(nlogn)

  if len(arr) >1:
  # Finding the mid point of the array
      mid = len(arr)//2

      #Left items of the array
      left_items = arr[:mid]

      #Right items of the array
      right_items = arr[mid:]

      #Sorting the left items
      mergeSort(left_items)

      #Sorting the right items
      mergeSort(right_items)

      i=j=k=0
      #Using left and right arrays
      while i < len(left_items) and j < len(right_items):
        if left_items[i] < right_items[j]:
          arr[k] = left_items[i]
          i+=1
        else:
          arr[k] = right_items[j]
          j = j+1
        k = k + 1

      #If left items or right array items left
      while i < len(left_items):
        arr[k] = left_items[i]
        i = i+1
        k = k+1

      while j < len(right_items):
        arr[k] = right_items[j]
        j= j+1
        k= k+1

# Code to print the list 
def printList(arr): 
    
    #write your code here
    for i in range(len(arr)):
      print(arr[i])
    
    print()
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
