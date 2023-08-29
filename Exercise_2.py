#Python program for implementation of Quicksort Sort 
#Time Complexity: O(n log n)
# Space Complexity: O(log n)
# Give you explanation for the approach
def partition(arr,low,high):
  i=low #Assign i to low
  j=high-1 #Assign j to high-1
  pivot=arr[high] #Assign pivot with the value of arr[high]

  while i<=j: #Continue looping until i is less than equal to j
    while i<=j and arr[i]<pivot: #Check if i<=j and arr[i]<pivot
      i+=1           #If that's the case increment i by 1
    while j>=low and arr[j]>=pivot:  #Check if j>=low and arr[j]>=pivot
      j-=1                          #If that's the case increment j by 1

    if i<j:                         #If i<j
      arr[i], arr[j]=arr[j], arr[i] #Swap the elements of arr[j] and arr[i]

   
  arr[i], arr[high]=arr[high], arr[i] #At the end of Loop, swap values of arr[high] with arr[i]
  return i 

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low<high:
      #Partition the array into two parts and get the pivot index
      pivot_index=partition(arr,low, high)

      #Recursively sort the two subarrays
      quickSort(arr, low, pivot_index-1) #Sort elements before pivot
      quickSort(arr, pivot_index+1, high) #Sort elements after pivot
      
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
