# Python program for implementation of Quicksort
""" The quickSort function uses a stack to store the limitsof the array that needs to go through sorting. 
The indexes are then popped out of the stack and the partition function that places the pivot in the right position is called.
This function remains the same for both iterative and recursive implementations. In my implementation I pick a random pivot.
The time complexity for this is O(nlogn) and space complexity is O(n) for the stack"""
# This function is same in both iterative and recursive
import random
def partition(arr,low,high):
	pivot = random.randint(low,high)
	arr[pivot], arr[low] = arr[low], arr[pivot]
	less = low
	for i in range(low+1, high+1):
		if(arr[low]>=arr[i]):
			less += 1
			arr[less],arr[i] = arr[i],arr[less]
	arr[low], arr[less] = arr[less],arr[low]
	return less

def quickSortIterative(arr, l, h):
  #write your code here
  stack = []
  stack.append(h)
  stack.append(l)
  while(stack!=[]):
  	l = stack.pop()
  	h = stack.pop()
  	pivot = partition(arr,l,h)

  	if(pivot-1>l):
  		stack.append(pivot-1)
  		stack.append(l)
  	if(pivot+1<h):
  		stack.append(h)
  		stack.append(l)


arr = [10, 7, 8, 9, 1, 5, 4, 20, 8] 
quickSortIterative(arr, 0, len(arr)-1)
print(arr)