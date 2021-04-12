# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, low, high):
    #write your code here
	flag = 0
	pivot = low

	while flag != 1:

		while arr[pivot] <= arr[high] and (pivot != high):
			high -= 1

		if pivot == high:
			flag = 1
		elif arr[pivot] > arr[high]:
			arr[pivot], arr[high] = arr[high], arr[pivot]
			pivot = high

		if flag != 0:

			while arr[low] <= arr[pivot] and (pivot != low):
				low += 1

			if pivot == low:
				flag = 1
			elif arr[pivot] < arr[low]:
				arr[pivot], arr[low] = arr[low], arr[pivot]
				pivot = low
	return pivot



def quickSortIterative(arr, low, high):
	#write your code here

	while low < high:

		pivot = partition(arr, low, high)
		high = pivot + 1
		

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
