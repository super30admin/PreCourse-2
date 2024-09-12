# Python program for implementation of MergeSort 
# Time Complexity : O(nlog(n))
# Any problem you faced while coding this : No
#Basic logic is recursion with 3 pointers. I divided the list in such a way that only one element remains in each list  anf then compared element in each array and put them in their list.
def mergeSort(arr):
  #write your code here
  if (len(arr)>1):
    mid = int(len(arr)/2)
    a1 = arr[:mid]
    a2 = arr[mid:]
    mergeSort(a1)
    mergeSort(a2)

    ptr1 = ptr2 = ptr3 = 0

    while ptr1<len(a1) and ptr2<len(a2):
      if a1[ptr1] < a2[ptr2]:
        arr[ptr3] = a1[ptr1]
        ptr1 = ptr1 + 1
      else:
        arr[ptr3] = a2[ptr2]
        ptr2 = ptr2 + 1
      ptr3 = ptr3 + 1

    while ptr1 < len(a1):
      arr[ptr3] = a1[ptr1]
      ptr1 = ptr1 + 1
      ptr3 = ptr3 + 1

    while ptr2 < len(a2):
      arr[ptr3] = a2[ptr2]
      ptr2 = ptr2 + 1
      ptr3 = ptr3 + 1


# Code to print the list 
def printList(arr): 
    
    #write your code here
    for i in range(len(arr)):
      print(arr[i])

# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
