#Time complexity is O(nlogn) in the average case and O(n^2) in the worst case
#Space complexity is O(logn)
#Code ran successfully in leetcode terminal
#No problem faced when executing the code

# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr,low,high):
    #write your code here
    #here I am considering pivot as the left most value
    pivot=arr[low]
    #I am taking low into i
    i=low
    #I am taking high into j
    j=high
    #Here I am keeping a condition such that while loop should run only if i is less than j
    while(i<j):
        #here I am implementing 'do while' 
        #i will be incremented until value of arr[i] is greater than pivot
        while True:
            i+=1
            #here I included another condition because if there is no value greater than pivot, it should break at the end
            if(i==high or arr[i]>pivot):
                break
        #here I am implementing 'do while' 
        #j will be decremented until value of arr[j] is less than or equal to pivot
        while True:
            j-=1
            #here I inlcuded another condition because if there is no value <= pivot, it should stop before pivot
            if(j<low+1 or arr[j]<=pivot):
                break
        #only if i is less than j, swapping of values needs to be done
        if(i<j):
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
    #after the while loop, finally we need to swap pivot with arr[j] value and return the value of j        
    temp=arr[j]
    arr[j]=arr[low]
    arr[low]=temp
    return j


def quickSortIterative(arr, low, high):
    #write your code here
    #I am going to create a stack where the indexes of the partitons will be stored
    stack=[]
    #I am appending low and high values into the stack
    stack.append(low)
    stack.append(high)
    #while loop iterates until the stack gets empty
    while len(stack):
        end=stack.pop()
        start=stack.pop()
        #partition function will be called to get the pivot position
        pivot=partition(arr,start,end)
        #checking the position of pivot with respect to start
        if(pivot-1>start):
            stack.append(start)
            stack.append(pivot)
        #checking the position of pivot with respect to end
        if(pivot+1<end):
            stack.append(pivot+1)
            stack.append(end)

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr)
#here I am sending n directly as we will be doing decrement for j using do while in partitioning
quickSortIterative(arr,0,n) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i])

