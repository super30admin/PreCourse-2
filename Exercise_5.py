"""
Time Complexity - O(nlogn)
Space Complexity - O(n)

"""

# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,l,h):
    pivot=arr[l]
    i=l
    j=h
    while i<=j:
        while i<=j and arr[i]<=pivot:
            i+=1
        while i<=j and arr[j]>pivot:
            j-=1
        if i<j:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
    temp=arr[l]
    arr[l]=arr[j]
    arr[j]=temp
    return j
  
  
    #write your code here
  

# Function to do Quick sort 
def quickSortIterative(arr,l,h): 
  s=[]
  s.append((0,len(arr)-1))
  
  while s:
      l,h=s.pop()
      
      if l<h:
          pivot=partition(arr,l,h)
          s.append((l,pivot-1))
          s.append((pivot+1,h))
  
  return arr
  
      
          # partition(arr,j+1,high)
      
  #write your code here
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print (arr[i])
  
