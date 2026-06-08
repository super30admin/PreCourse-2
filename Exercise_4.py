#Kindly include Time and Space complexity at top of each file

#Time and Space Complexity
# Space Complexity : O(N)
# Time Complexity : O(N log N) where N is the number of elements in the array

 
def mergeSort(arr):
  if len(arr)>1:
     mid=len(arr)//2
     left=arr[:mid]
     right=arr[mid:]

     mergeSort(left)
     mergeSort(right)

     i=j=k=0
     while i<len(left) and j<len(right):
        if left[i]<right[j]:
           arr[k]=left[i]
           i=i+1
        else:
           arr[k]=right[j]
           j=j+1
        k=k+1
    
     while i<len(left):
        arr[k]=left[i]
        i=i+1
        k=k+1
     
     while j<len(right):
        arr[k]=right[j]
        j=j+1
        k=k+1
