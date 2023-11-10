def mergeSort(arr):

  #write your code here
  if len(arr) == 1:
    return arr
  mid = len(arr) // 2
  left = (arr[ : mid])
  right = (arr[mid : ])
  mergeSort(left)
  mergeSort(right)
  arr = merge(left, right, arr)



def merge(left, right, arr):
  l = 0
  r = 0
  c = 0
  while l < len(left) and r < len(right) :
    if left[l] < right[r]:
      arr[c] = left[l]
      l += 1
    else:
      arr[c] = right[r]
      r += 1
    c += 1

  while l < len(left):
    arr[c] = left[l]
    l += 1
    c += 1
  while r < len(right):
    arr[c] = right[r]
    r += 1
    c += 1
  return arr


# Code to print the list 
def printList(arr): 

    #write your code here

    print(arr)
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    print ("Given array is")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    print("Sorted array is: ") 
    printList(arr) 