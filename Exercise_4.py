# Python program for implementation of MergeSort 





def merge(arr, left, mid, right):
	n1=mid-left+1
	n2=right-mid

	tempL=[0]*n1#create temp array 
	tempR=[0]*n2

	for i in range(0 , n1):
		tempL = arr[left + i]

	for j in range(0 , n2):
		tempR[j] = arr[mid + 1 + j]
    #merge temp array 
	i=0
	j=0
	k=left
	while i < n1 and j < n2 : 
		if tempL[i] <= tempR[j]: 
			arr[k] = tempL[i] 
			i += 1
		else: 
			arr[k] = tempR[j] 
			j += 1
		k += 1
    #copy remaning element 
	while i < n1: 
		arr[k] = tempL[i] 
		i += 1
		k += 1

	while j < n2: 
		arr[k] = tempR[j] 
		j += 1
		k += 1

def mergeSort(arr,left,right):
	
	if left<right:
		mid=(left+(right-left)//2)
		mergeSort(arr, left, mid)#sort first half
		mergeSort(arr, mid+1, right)#sort second half 
		merge(arr,left,mid,right)#merge 
  
  #write your code here
  
# Code to print the list 
def printList(arr):
	for i in range(len(arr)): 
		print ("%d" %arr[i]) 
    
    #write your code here
  
# driver code to test the above code 
if __name__ == '__main__': 
	arr = [12, 11, 13, 5, 6, 7]  
	print ("Given array is", end="\n")  
	printList(arr)
	left=0
	right=len(arr)-1 
	mergeSort(arr,left,right) 
	print("Sorted array is: ", end="\n") 
	printList(arr) 
