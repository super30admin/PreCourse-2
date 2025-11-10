# Python program for implementation of MergeSort 

#TC for mergesort in any condition is O(nlogn)
#SC is o(n)
def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = (len(arr)) //2
    left = arr[:mid]
    right = arr[mid:]
    lhalf = mergeSort(left)
    rhalf = mergeSort(right)
    return merge(lhalf, rhalf)
    
def merge(left, right):
    res =[]
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:

          res.append(left[i])
          i += 1
        else:  
          res.append(right[j])
          j += 1
    res.extend(left[i:])
    res.extend(right[j:])
    return res


    
  
  #write your code here
  
# Code to print the list 
def printList(arr): 
   for i in arr:
      print(i, end =" ")
   print()
   
    
      
    
    #write your code here
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    arr = mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
