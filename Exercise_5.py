# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
	#write your code here
  	pivot=arr[h]
  	i=l
  	for j in range(l,h):
  		if arr[j]<=pivot:
  			arr[i],arr[j]=arr[j],arr[i]
  			i+=1
  	arr[i],arr[h]=arr[h],arr[i]
  	return i

def quickSortIterative(arr, l, h):
	#write your code here
	n=h-l+1
	stack=[0]*n

	top=-1
	top+=1
	stack[top]=l
	top+=1
	stack[top]=h

	while top>=0:
		h=stack[top]
		top-=1
		l=stack[top]
		top-=1

		part=partition(arr,l,h)
		
		if part-1>l:
			top+=1
			stack[top]=l
			top+=1
			stack[top]=part-1

		if part+1<h:
			top+=1
			stack[top]=part+1
			top+=1
			stack[top]=h

			
 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
