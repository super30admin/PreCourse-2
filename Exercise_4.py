# Python program for implementation of MergeSort 
def mergeSort(arr):

  def merge(left_arr, right_arr ):
    print(left_arr, right_arr)
    i = 0 
    j = 0 
    result = []

    if right_arr==None:
      right_arr = []

    if left_arr==None:
      left_arr = []

    while i < len(left_arr) and j < len(right_arr):
      if left_arr[i] < right_arr[j]:
        result.append(left_arr[i]) ; i+=1
      else:
        result.append(right_arr[j]) ; j+=1

    while i < len(left_arr):
      result.append(left_arr[i]) ; i+=1

    while j < len(right_arr):
      result.append(right_arr[j]) ; j+=1

    print("result = ", result, "i=", i, " j =", j)
    return result 

  def sort(arr):
    if len(arr)<2:
      print("sort returned :", arr)
      return arr
    mid = len(arr)//2 ; print(arr, mid, len(arr), arr[:mid], arr[mid:])
    left = mergeSort(arr[:mid]) ; #print("left =", arr[:mid])
    right= mergeSort(arr[mid:]);  #print("right =", arr[mid:])
    print("Left right received:", left , right)
    result =  merge(left, right)    
    return result 

  result = sort(arr)
  for i in range(len(arr)):
    arr[i] = result[i]
  return result 
  
# Code to print the list 
def printList(arr): 
    print(arr)
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
