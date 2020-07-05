# Python program for implementation of MergeSort 
sorted_arr = []

def mergeSort(arr):
	global sorted_arr
	if len(arr) > 1:
		sorted_arr = helper(arr, 0, len(arr)-1)
  #write your code here

def helper(helper_arr, l, h):
	if l == h:
		return [helper_arr[l]]
	if h == l+1:
		return [helper_arr[l], helper_arr[h]] if helper_arr[l] < helper_arr[h] else [helper_arr[h], helper_arr[l]]

	mid = (l + h) // 2

	arr1 = []
	arr2 = []
	if l <= mid:
		arr1 = helper(helper_arr, l, mid)
	if mid+1 <= h:
		arr2 = helper(helper_arr, mid+1, h)

	if not arr1:
		return arr2
	if not arr2:
		return arr1
	if arr1[-1] <= arr2[0]:
		return arr1 + arr2
	else:
		return arr2 + arr1
  
# Code to print the list 
def printList(arr): 
	if sorted_arr:
		arr = sorted_arr
	print(arr)
	#write your code here
  
# driver code to test the above code 
if __name__ == '__main__': 
	arr = [12, 11, 13, 5, 6, 7]  

	print ("Given array is", end="\n")  
	printList(arr) 
	mergeSort(arr) 
	print("Sorted array is: ", end="\n") 
	printList(arr) 
