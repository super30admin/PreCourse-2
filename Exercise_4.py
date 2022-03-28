# // Time Complexity : O(N)
# // Space Complexity : O(N)
# // Did this code successfully run on Leetcode :yes
# // Any problem you faced while coding this : had to research mergesort before starting, as a review


# Python program for implementation of MergeSort 
def mergeSort(arr):
  if(len(arr)>1):
    middle = len(arr)//2
    left = arr[:middle]         #getting the left side of the array
    right= arr[middle:]         #getting the right side of the array

    mergeSort(left)             #recursively merge the left side
    mergeSort(right)            #recursively merge the right side

    index1 = index2 = arrayindex = 0

    while(index1 < len(left) and index2 <len(right)):       #  compare the left to the right number and put them in the correct order to the main array starting with two elements
      if(left[index1] <right[index2]):
        arr[arrayindex] = left[index1]
        index1+=1
      else:
        arr[arrayindex] = right[index2]
        index2+=1
      arrayindex+=1

    if (index1<len(left)):        #if there are still elements remaining in the left array, add them to the main array
      while(index1 < len(left)):
        arr[arrayindex] = left[index1]
        index1+=1
        arrayindex+=1
    elif(index2<len(right)):      #if there are still elements remaining in the right array, add them to the main array
      while(index2 <len(right)):
        arr[arrayindex] = right[index2]
        index2+=1
        arrayindex+=1
    

# Code to print the list 
def printList(arr): 
    for i in arr:
      print(i)
   
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7,]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
