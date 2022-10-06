# Python program for implementation of MergeSort 
def mergeSort(arr):
  
  #write your code here

  #Checking if the size of the arr is not 1 or less than 1. Helps out avoid the situation when there is only 1 
  # independant element and we don't need to divide it anymore
  if len(arr)>1:

    #Calculating mid in order to divide the array into parts
    mid=len(arr)//2

    left_side=arr[:mid]  #First part
    right_side=arr[mid:] #Second Part

    mergeSort(left_side)   # Sending the left_part to further divide
    mergeSort(right_side)  # Sending the right_part to further divide

    a,b,c=0,0,0

    while a<len(left_side) and b<len(right_side):
        if left_side[a]<=right_side[b]:
            arr[c]=left_side[a]
            a+=1
        else:
            arr[c]=right_side[b]
            b+=1
        c+=1

    while a<len(left_side):
        arr[c]=left_side[a]
        a+=1
        b+=1
    
    while b<len(right_side):
        arr[c]=right_side[b]
        b+=1
        c+=1

  
# Code to print the list 
def printList(arr): 
    print(arr)
    #write your code here
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 