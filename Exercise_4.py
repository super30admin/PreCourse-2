# Python program for implementation of MergeSort 
#Time Complexity : O(n log n)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode : yes
# Any problem you faced while coding this :
def mergeSort(arr):
  
	  #write your code here
	  if len(arr) <= 1:
	  	 return arr

	  # Divide list into 2 lists
	  left = arr[:int(len(arr)/2)]
	  right = arr[int(len(arr)/2):]

	  #call merge sort recursively until it divided into single element
	  left = mergeSort	 (left)
	  right = mergeSort  (right)

	  #merge two sorted lists
	  return merge_sorted_arrays(left,right)

def merge_sorted_arrays(a,b):
    
	i = j = 0
	sorted_list = []

	while i < len(a) and j < len(b):
		if a[i] <= b[j]:
			sorted_list.append(a[i])
			i += 1
		else:
			sorted_list.append(b[j])
			j += 1

	# to add elements remaining in either side when it is divided into uneuqal size of elements
	while i < len(a):
		sorted_list.append(a[i])
		i += 1

	while j < len(b):
		sorted_list.append(b[j])
		j += 1

	return sorted_list	  
      
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    print(arr) 
    sorted_arr = mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    print(sorted_arr) 

