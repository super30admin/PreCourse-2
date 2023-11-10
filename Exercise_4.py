#Time complexity is O(n*logn)
#space complexity is O(n)

# Python program for implementation of MergeSort 
def mergeSort(arr):
  
  #write your code here
  if len(arr)>1:
    middle=len(arr)//2
    left=arr[:middle]
    right=arr[middle:]
    mergeSort(left)
    mergeSort(right)
    a=0
    b=0
    c=0
    while a<len(left) and b<len(right):
      if left[a]<left[b]:
        arr[c]=left[a]
        a+=1
      else:
        arr[c]=right[b]
        b+=1
      c+=1

    while a<len(left):
      arr[c]=left[a]
      a+=1
      c+=1
    while b<len(right):
      arr[c]=right[b]
      b+=1
      c+=1
# Code to print the list 
def printList(arr): 
    
    #write your code here
    for i in range(len(arr)):
      print(arr[i],end=" ")
    print()
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
