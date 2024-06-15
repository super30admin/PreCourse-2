# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
  #write your code here
    pivot = arr[low] #Assign the first element as pivot element
    i = low # i will search for elements greater than pivot element
    j = high # j will search for elements smaller than pivot element
    while(i<=j):
        print(arr)
        while True:
            i+=1 #increment i till ith element is greater than pivot or until i reached the high pointer
            if i>=high or arr[i]>=pivot:
                break
        while True:
            j-=1 #decrement j until jth element is less than pivot or until j reached the low pointer
            if j<=low or arr[j]<pivot:
                break
        if (i<=j):
            (arr[i],arr[j])=(arr[j],arr[i]) #swap the ith and jth element, so that all the smaller elements are to the left of pivot and bigger element are to right of pivot
    (arr[low],arr[j])=(arr[j],arr[low]) # to place the pivot in right positionin array
    return j


# Function to do Quick sort 
def quickSort(arr,low,high): 
    #write your code here
    if (low<high):
        j = partition(arr,low,high)
        quickSort(arr,low,j) #here the element at the jth position will act as infinity
        quickSort(arr,j+1,high)
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
arr.append(9999) #add large element to the end of array depicting infinity
n = len(arr) 
quickSort(arr,0,n-1)
arr.pop() #pop the infinity element
print ("Sorted array is:") 
for i in range(len(arr)): 
    print ("%d" %arr[i]), 
  
 
