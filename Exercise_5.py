# Python program for implementation of Quicksort 

# This function is same in both iterative and recursive 
def partition(arr, l, h):
 print("sample=", arr)
 pivot = arr[h]
 index = l
 current = l
 while (current < h):
  if( arr[current] <= pivot):
   arr[index], arr[current] = arr[current], arr[index]
   index += 1
  current += 1
 arr[h], arr[index] = arr[index], arr[h]
 print("partitioned=", arr)
 return index

# Function to do Quick sort 
# arr[] --> Array to be sorted, 
# l --> Starting index, 
# h --> Ending index 
def quickSortIterative(arr, l, h): 

	# Create an auxiliary stack 
	size = h - l + 1
	stack = [0] * (size) 

	# initialize top of stack 
	top = -1

	# push initial values of l and h to stack 
	top = top + 1
	stack[top] = l 
	top = top + 1
	stack[top] = h 

	# Keep popping from stack while is not empty 
	while top >= 0: 

		# Pop h and l 
		h = stack[top] 
		top = top - 1
		l = stack[top] 
		top = top - 1

		# Set pivot element at its correct position in 
		# sorted array 
		p = partition( arr, l, h ) 

		# If there are elements on left side of pivot, 
		# then push left side to stack 
		if p-1 > l: 
			top = top + 1
			stack[top] = l 
			top = top + 1
			stack[top] = p - 1

		# If there are elements on right side of pivot, 
		# then push right side to stack 
		if p + 1 < h: 
			top = top + 1
			stack[top] = p + 1
			top = top + 1
			stack[top] = h 

# Driver code to test above 
arr = [4, 3, 5, 2, 1, 3, 2, 3] 
n = len(arr) 
quickSortIterative(arr, 0, n-1) 
print ("Sorted array is:") 
for i in range(n): 
	print ("% d" % arr[i]), 

# This code is contributed by Mohit Kumra 
