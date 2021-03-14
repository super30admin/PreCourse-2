# Python program for implementation of MergeSort 
def merge(left,right):
    l = 0
    r = 0
    newLi = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            newLi.append(left[l])
            l += 1
        else:
            newLi.append(right[r])
            r += 1
    if l < len(left):
        newLi.extend(left[l:])
    if r < len(right):
        newLi.extend(right[r:])

    return newLi   
def mergeSort(arr):
  #write your code here
  if len(arr) <= 1:
      return arr
  p = len(arr)//2
  l = mergeSort(arr[:p])
  r = mergeSort(arr[p:])
  return merge(l,r)
# Code to print the list 



def printList(arr): 
    #write your code here
    print(arr) 
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    arr = mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
