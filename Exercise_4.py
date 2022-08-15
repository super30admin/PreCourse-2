# Python program for implementation of MergeSort
def merge(left, right):
  if not len(left) or not len(right):
    return left or right
  
  result = []
  i, j = 0, 0
  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      result.append(left[i])
      i += 1
      
    else:
      result.append(right[j])
      j += 1
      
    while i < len(left):
      result.append(left[i])
      i += 1
      
    while j < len(right):
      result.append(right[j])
      j += 1

def mergeSort(arr):
  if len(arr) < 2:
    return arr
  
  mid = len(arr)//2
  left = mergeSort(arr[:mid])
  right = mergeSort(arr[mid:])
  merge(left, right)
  
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


# driver code to test the above code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)
