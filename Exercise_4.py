# Python program for implementation of MergeSort
def mergeSort(arr):
	#write your code here
	if len(arr)>1:
		mid=len(arr)//2
		
		l1=arr[:mid]
		l2=arr[mid:]

		mergeSort(l1)
		mergeSort(l2)
		
		i=j=k=0
		n1=len(l1)
		n2=len(l2)
		while i<n1 and j<n2:
			if l1[i]<l2[j]:
				arr[k]=l1[i]
				i+=1
			else:
				arr[k]=l2[j]
				j+=1
			k+=1

		while i<n1:
			arr[k]=l1[i]
			i+=1
			k+=1
		while j<n2:
			arr[k]=l2[j]
			j+=1
			k+=1

			
# Code to print the list 
def printList(arr):
	#write your code here
    print(arr)
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
