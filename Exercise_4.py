# Python program for implementation of MergeSort 
""" Merge Sort separates the input array by half and recursively does that until the size of each divided array is 1.
Now it begins to merge by sorting the elements separately and continues to do so upwards until the entire result is formed.
The time complexity is O(nlogn) and the space complexity is O(n)."""
def mergeSort(arr,start,end):
	if(start<end-1):
	  mid = start + ((end-start)//2)
	  mergeSort(arr,start, mid)
	  mergeSort(arr,mid,end)
	  merge(arr,start, mid, end)
  #write your code here
def merge(arr, start, mid, end):
  	result = [0 for i in range(end-start)]
  	i = start
  	j = mid
  	curr = 0
  	while(i<mid and j<end):
  		if(arr[i]<=arr[j]):
  			result[curr] = arr[i]
  			i+=1
  		else:
  			result[curr] = arr[j]
  			j+=1
  		curr +=1
  	while(i<mid):
  		result[curr] = arr[i]
  		curr+=1
  		i+=1
  	while(j<end):
  		result[curr] = arr[j]
  		curr+=1
  		j+=1
  	for i in range(len(result)):
  		arr[start+i] = result[i]
# Code to print the list 
def printList(arr): 
    print(arr)
    #write your code here
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr, 0, len(arr)) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
