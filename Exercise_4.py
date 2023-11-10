#time complexity is O(nlogn), 
#Space complexity is O(n), where n is the number of elements in the input array
#Code executed successfulltin the leetcode without any errors
#Its been long I worked on mersort, so it took some time but there are no problems faced.
#Python program for implementation of MergeSort 
def mergeSort(arr):
  
  #write your code here
  #array size contains length of the array
  array_size=len(arr)
  #To ensure that there is more than 1 value in the array, I used 'if' condition
  if(array_size>1):
     #mid_value contains the middle position of the array
     mid_value=array_size//2
     #Splitting arr into sub arrays array1 and array2 based on middle value
     array1=arr[0:mid_value]
     array2=arr[mid_value:array_size]
     #Recursively sorting the two arrays
     mergeSort(array1)
     mergeSort(array2)

     #initialising index values of array1, array2 and arr to 0
     a1=a2=a3=0
     #As we have two sub arrays containing sorted values, we are going to compare values
     #in both the arrays and we will updating the original array arr
     while(a1<len(array1) and a2<len(array2)):
        #if the value of array1[a1] is less than array2[a2], we will be updating arr with array1[a1]
        if(array1[a1]<array2[a2]):
           arr[a3]=array1[a1]
           a1+=1
        #if the value of array2[a2] is less than array1[a1], we will be updating arr with array2[a2]
        else:
           arr[a3]=array2[a2]
           a2+=1
        a3+=1
     #After above comparision we can have some values remaining in either of the sorted arrays 
     #as one of the array can be completely traversed
     #Moving all the remaining values in array1 into arr
     while(a1<len(array1)):
        arr[a3]=array1[a1]
        a1+=1
        a3+=1
     #Moving all the remaining values in array2 into arr
     while(a2<len(array2)):
        arr[a3]=array2[a2]
        a2+=1
        a3+=1
  
# Code to print the list 
def printList(arr): 
    
    #write your code here
    for i in arr:
       print(i)
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is:")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is:") 
    printList(arr) 
