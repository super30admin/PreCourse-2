# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
  
  
    #write your code here   
     pivot = arr[high]
     lpos=low-1
     for j in range(low,high):
          if(arr[j]<= pivot):
               lpos=lpos+1
               temp=arr[j]
               arr[j]=arr[lpos]
               arr[lpos]=temp
               
     arr[high]=arr[lpos+1]
     arr[lpos+1]=pivot
     return lpos+1       
               
     
  

# Function to do Quick sort 
# time Complexity: O(n*2) 
def quickSort(arr,low,high): 
    
    #write your code here
    if(high>low):
         div=partition(arr,low,high)
         quickSort(arr,low,div-1)
         quickSort(arr,div+1,high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
