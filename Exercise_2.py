# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
	i=low-1 #smaller index taken as -1 
	pivot=arr[high] #Pivot as last element
	for j in range(low, high):
		if arr[j] <= pivot: #if cur element is less or eq to Pivot
			i=i+1 #increase smaller element
			arr[i], arr[j] = arr[j], arr[i] #swap smaller and higher element

	arr[i+1], arr[high] = arr[high], arr[i+1]
	return i+1
  
  
    #write your code here
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
	if len(arr) == 1:
		return arr
	if low<high:
		part=partition(arr,low,high)
		quickSort(arr, low, part-1) #sort element before part
		quickSort(arr, part+1,high)#sort element after part
    
    #write your code here
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
