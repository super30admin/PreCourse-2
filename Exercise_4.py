# Python program for implementation of MergeSort 

"""
Intuition:  The idea here is to divide the array into its smallest parts.
Then using these smallest parts we create a new temporary array and assign each smallest part
in its appropritate location in the temporary array

mergeSort():
Time Complexity : O(log n) #Where n is the number of elements
Space Complexity : O(n) #Uses Recursion

merge():
Time Complexity : O(n) #Where n is the number of elements
Space Complexity : O(n) #Where n is the number of elements

Total Time Complexity:
Time Complexity : O(n Log n) #Where n is the number of elements
Space Complexity : O(n) #Where n is the number of elements
"""
def mergeSort(arr, low, high):
	
	if low < high:
		mid = (low + high)//2
		mergeSort(arr, low, mid)
		mergeSort(arr, mid+1, high)
		merge(arr, low, mid, high)
def merge(array, low, mid, high):

	result = [0] * 20
	resultIndex = low
	currentI = low
	currentJ = mid + 1
	while currentI <= mid and currentJ <= high:
		if array[currentI] < array[currentJ]:
			result[resultIndex] = array[currentI]
			currentI += 1
		else:
			result[resultIndex] = array[currentJ]
			currentJ += 1
		resultIndex += 1
	
	if currentI > mid:

		while currentJ <= high:
			result[resultIndex] = array[currentJ]
			currentJ += 1
			resultIndex += 1
	else:
		while currentI <= mid:
			result[resultIndex] = array[currentI]
			currentI += 1
			resultIndex += 1
	
	for index in range(low, resultIndex):
		array[index] = result[index]

def printList(arr): 
    print(arr)
  
# driver code to test the above code 
if __name__ == '__main__': 
	arr = [12, 11, 13, 5, 6, 7]  
	print ("Given array is", end="\n")  
	printList(arr) 
	mergeSort(arr, 0, len(arr)-1) 
	print("Sorted array is: ", end="\n") 
	printList(arr) 
