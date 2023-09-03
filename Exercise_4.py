# Python program for implementation of MergeSort 
def mergeSort(arr):
  #write your code here
  if len(arr)<=1:
    return arr
  mid =len(arr)//2  
  left_arr=arr[:mid] 
  right_arr=arr[mid:]
  
  left_arr=mergeSort(left_arr) 
  right_arr=mergeSort(right_arr)
  
  result=[]
  i=j=0
  
  while i<len(left_arr) and j<len(right_arr):
    if left_arr[i]<right_arr[j]:
        result.append(left_arr[i])
        i+=1
    else:
        result.append(right_arr[j])
        j+=1
  result.extend(left_arr[i:])
  result.extend(right_arr[j:])
  
  return result
# Code to print the list 
def printList(arr): 
    #write your code here
  for i in range(len(arr)):
    print(arr[i], end=" ")
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
