# Python program for implementation of MergeSort
#Time Complexity is nlogn as there is use of recursion function
#Space complexity is n because n time subarrays are created

def mergeSort(arr):
  
  #write your code here

  if(len(arr)>1):
    mid = len(arr)//2
    #dividing the array into two parts
    left_sub = arr[:mid]
    right_sub = arr[mid:]
    #There will be recursion call till the array is divide into one element each
    mergeSort(left_sub)
    mergeSort(right_sub)

    #using i for dealing with left subarray, j for dealing the right subarray and k for arranging the value in arr 
    i = j = k = 0
    m = len(left_sub)
    n = len(right_sub)

    #while loop will work till either the left subarray or right is placed fully in the arr 
    while(i<m and j<n):
      #assign the value from the left subarray if the value is smaller than the right subarray 
      if left_sub[i]<right_sub[j]:
        arr[k] = left_sub[i]
        i+=1
      else:
        arr[k] = right_sub[j]
        j+=1
      k+=1
    #assign all the remaining value of left subarray if remaining
    while i<m:
     arr[k] = left_sub[i]
     i+=1
     k+=1
    #assign all the remaining value of rightsub subarray if remaining
    while j<n:
     arr[k] = right_sub[j]
     j+=1
     k+=1

# Code to print the list 
def printList(arr): 
    for i in range(len(arr)):
      print(arr[i], end=" ")

    #write your code here
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
