# Python program for implementation of MergeSort 
def mergeSort(values):
    if len(values)>1:
        mid = len(values)//2
        left = mergeSort(values[:mid])
        right = mergeSort(values[mid:])

        i,j=0,0
        values =[]
        while i<len(left) and j<len(right):
          if left[i] < right[j]:
            values.append(left[i])
            i+=1
          else:
            values.append(right[j])
            j+=1

        while i<len(left):
          values.append(left[i])
          i+=1

        while j<len(right):
          values.append(right[j])
          j+=1
    return values
      

# Code to print the list 
def printList(arr): 
    
    for i in range(len(arr)):
      print(arr[i])
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7, 1, -1, 2] 
    print ("Given array is", end="\n")  
    printList(arr) 
    arr = mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 

#TC: O(nlong)
#SC: O(n)