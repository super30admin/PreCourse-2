# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    piv=low
    i,j=low,high
    while i<j:

        while arr[i]<arr[piv]:
            i+=1
        while arr[j]>arr[piv]:
            j-=1
        arr[i],arr[j]=arr[j],arr[i]
    arr[piv],arr[j]=arr[j],arr[piv]
    return j



    #write your code here
  

# Function to do Quick sort 
def quickSort(arr,low,high):
    if low<high:


        piv= partition(arr,low,high)
        quickSort(arr,low,piv-1)
        quickSort(arr,piv+1,high)
    
    #write your code here
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
