# Python program for implementation of MergeSort

# Time Complexity : O(nlog n)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode : yes
# Any problem you faced while coding this : no

def mergeSort(arr):
	if len(arr) > 1:
		mid = len(arr) // 2
		leftsubarr = arr[:mid]
		rightsubarr = arr[mid:]
		mergeSort(leftsubarr)
		mergeSort(rightsubarr)
		
		i = j = k = 0
		while i < len(leftsubarr) and j < len(rightsubarr):
			if leftsubarr[i] < rightsubarr[j]:
				arr[k] = leftsubarr[i]
				i+=1
			else:
				arr[k] = rightsubarr[j]
				j+=1
			k+=1
		
		while i < len(leftsubarr):
			arr[k] = leftsubarr[i]
			i+=1
			k+=1
			
		while j < len(rightsubarr):
			arr[k] = rightsubarr[j]
			j+=1
			k+=1
  
# Code to print the list 
def printList(arr):
	for i in range(len(arr)):
		print(arr[i]," ")
    
    #write your code here
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
