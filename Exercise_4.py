# Python program for implementation of MergeSort
def mergeSort(arr):
  if len(arr) > 1:
      mid = len(arr) // 2  # Find mid Element
      left = arr[:mid]
      right = arr[mid:]

      mergeSort(left)  #Sort the left side
      mergeSort(right) # Sort the right Side

      i = j = k = 0

      while i < len(left) and j < len(right):
          if left[i] < right[j]:
              arr[k] = left[i]
              i += 1
          else:
              arr[k] = right[j]
              j += 1
          k += 1

#Checking if any more Elements are left to be sorted towards left and right
      while i < len(left):
          arr[k] = left[i]
          i += 1
          k += 1

      while j < len(right):
          arr[k] = right[j]
          j += 1
          k += 1

# Code to print the list
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end= " ")
    print()

# driver code
if __name__ == '__main__':
    arr =[5, 4, 6, 3, 2, 5, 4, 2,8]
    print ("Given array is", end=" ")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end=" ")
    printList(arr)

