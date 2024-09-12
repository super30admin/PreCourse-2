#Time complexity = O(nlogn) expected case
#space complexity= O(logn) as no more than log n memory of stack will be used at a time



# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
    pivot= arr[h]
    i = (l - 1)
  
    for j in range(l,h):
        if (arr[j] <= pivot):
            i=i+1 
            arr[i],arr[j]=arr[j],arr[i]# swaping the values
    

    arr[i + 1],arr[h]=arr[h],arr[i + 1] #putting the pivot in its rightplace in the array
    return (i + 1)




def quickSortIterative(arr, l, h):
  #write your code here 
    stack=[]
    stack.append(l)
    stack.append(h)
    top=len(stack)-1
    while(top>-1):
        r=stack.pop()
        l=stack.pop()
        
        p=partition(arr, l, h)# finding the location of the pivot element
        if(p-1>l):
            stack.append(l)
            stack.append(p-1)
        if(p+1<r):
            stack.append(p+1)
            stack.append(r)
        top=len(stack)-1
    
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 