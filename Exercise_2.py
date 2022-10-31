#Time complexity:O(nlog(n))
#space complexity: O(1)
#Ran in leetcode: yes
#problems/issues: None
#The "low" is set as pivot. All elemnts less than pivot and greater than pivot are segragated in the array. Then the solution 
# recurses to the left and right half after placing the pivot at the right position.
# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
#from pandas import pivot


def partition(arr,low,high):
  
  
    #write your code here
    pivot=arr[low]
    i=low
    for j in range(low+1,high+1):
        if(arr[j]<pivot):
            temp=arr[i+1]
            arr[i+1]=arr[j]
            arr[j]=temp
            i+=1
    temp=arr[i]
    arr[i]=pivot
    arr[low]=temp
    return i
    
    
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here
    if(low>=high):
        return
    k=partition(arr,low,high)
    quickSort(arr,low,k-1)
    quickSort(arr,k+1,high)

  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
