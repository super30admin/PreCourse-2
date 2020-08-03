# Python program for implementation of MergeSort 
def mergeSort(arr):
  #write your code here
  if len(arr) <= 1 :
    return arr

  if arr:
    left = 0
    right = len(arr)
    mid = (left+right)//2
    first = mergeSort(arr[left:mid])
    second = mergeSort(arr[mid:right])

    new_arr = [0]*len(arr)
    one = two = ptr = 0

    # print(first, second)
    while one < len(first) and two < len(second):
      if first[one] <= second[two]:
        new_arr[ptr] = first[one]
        one += 1
        ptr += 1
      elif second[two] < first[one]:
        new_arr[ptr] = second[two]
        two += 1
        ptr += 1

    if one < len(first):
      new_arr[ptr:] = first[one:].copy()
    
    elif two < len(second):
      new_arr[ptr:] = second[two:].copy()
    # print(new_arr)
    # print('---')
    return new_arr
  
# Code to print the list 
def printList(arr): 
    print(arr)
    #write your code here
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]
    arr = [9,8,7,6,5,4,3,2,1]  
    print ("Given array is", end="\n")  
    printList(arr) 
    sorted_array = mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(sorted_array) 
