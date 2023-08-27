# Python program for implementation of MergeSort 
def mergeSort(arr):
  if len(arr)>1:
    mid=len(arr)//2 #Middle of the array
    left_part=arr[:mid] #Split the array into two halves
    right_part=arr[mid:]

    mergeSort(left_part) #Recursively sort the left Part
    mergeSort(right_part) #Recursively sort the right Part

    i=j=k=0

    #Merge the sorted parts back into the original array
    while i<len(left_part) and j<len(right_part):
      if left_part[i]< right_part[j]:
        arr[k]=left_part[i]
        i+=1

      else:
        arr[k]=right_part[j]
        j+=1
      k+=1

     #Check for any remaining elements in left_part and right_part
     while i<len(left_part):
       arr[k]=left_part[i]
       i+=1
       k+=1

     while j<len(right_part):
        arr[k]=right_part[j]
        j+=1
        k+=1

#Code to print the list
def printList(arr): 
    for element in arr:
      print(element, end=" ")
    print()

  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
