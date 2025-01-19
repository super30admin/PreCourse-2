# Python program for implementation of MergeSort 
def mergeSort(arr):
  if len(arr)<=1:
    return arr
  
  left =0
  right = len(arr)
  mid = (left+right)//2

  left_array=mergeSort(arr[:mid])
  right_array = mergeSort(arr[mid:])

  i,j=0,0
  result =[]
  while i < len(left_array) and j < len(right_array):
    if left_array[i] < right_array[j]:
        result.append(left_array[i])
        i += 1
    else:
        result.append(right_array[j])
        j += 1

  result.extend(left_array[i:])
  result.extend(right_array[j:])
  
  return result

  

  #write your code here
  
# Code to print the list 
def printList(arr): 
    print(arr)
    return
    #write your code here
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    result=mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(result) 
