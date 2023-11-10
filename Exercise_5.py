# Python program for implementation of Quicksort
# Time complexity O(n^2)
# Space complexity O(n)
# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
    lo=l
    hi=h - 1
    pivot=arr[h]

    while lo < hi:
     # All the elements less than to the
    # pivot go before or at l
        while lo< hi and arr[lo]< pivot:
            #l moves to the right
            lo += 1
        while hi > lo and arr[hi]>= pivot:
            #r moves to the left 
            hi -= 1
        
        if lo < hi:
            #swap the positions
            arr[lo],arr[hi]=arr[hi],arr[lo]

    #if l and r crossed each other
    if arr[lo]> pivot:
        #swap
        arr[lo],arr[h] = arr[h],arr[lo]

    return lo

def quickSortIterative(arr, l, h):
  size=h-l+1
  st=[0]*(size)
#declare top element
  top_of_the_st= -1

#addign values of l and h to the st
  top_of_the_st += 1
  st[top_of_the_st] += l
  top_of_the_st += 1
  st[top_of_the_st] += h

  while top_of_the_st >=0:
    #pop the values from stack
    h = st[top_of_the_st]
    top_of_the_st -= 1 

    l= st[top_of_the_st]
    top_of_the_st -= 1
#set the pivot to the index returned from partition function
    partion_position=partition(arr,l,h)

#if elemets are at left side of pivot, i.e smaller than pivot
    if partion_position -1 > l:
      #add them to stack
      top_of_the_st += 1
      st[top_of_the_st]=l
      top_of_the_st += 1
      st[top_of_the_st]= partion_position-1
    
    #if elements are greater than pivot
    if partion_position+1<h:
      top_of_the_st += 1
      st[top_of_the_st] = partion_position+1
      top_of_the_st +=1
      st[top_of_the_st]= h

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 6, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 