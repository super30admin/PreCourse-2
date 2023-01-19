# Time Complexity : O(NlogN), N being the length of the array
# Space Complexity : O(N), N being the length of the array. 
# Did this code successfully run on Leetcode : Did not find a 
# corresponding problem in leetcode. 
# Any problem you faced while coding this : Had to refer to the 
# recursive quicksort problem to debug why the iterative one 
# won't run properly. 


# Your code here along with comments explaining your approach

# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
    #write your code here
    mid = int((l+h)/2)
    pivot=arr[mid]

    while(l<h):
        #while left side is less than pivot
        while(arr[l]<pivot):
            l = l+1
        #while right side is greater than pivot
        while(arr[h]>pivot):
            h = h-1
        #swap
        temp = arr[l]
        arr[l]=arr[h]
        arr[h] = temp
    #return the point where left side meets right side. 
    return int((l+h)/2)

def quickSortIterative(arr, l, h):
    #write your code here
    stack = []
    #place left and right index into an stack-like array.
    stack.append(l)
    stack.append(h)
    
    while(len(stack)>0):
        #pop the last two left and right index from the stack. 
        s2 = stack.pop(len(stack)-1)
        s1 = stack.pop(len(stack)-1)

        if s1<s2:
            #run partition function with popped left and right index. 
            p_mid = partition(arr, s1, s2)
            #place new left and right into stack to be popped again. 
            if l<p_mid:
                stack.append(s1)
                stack.append(p_mid)
            if p_mid+1<s2:
                stack.append(p_mid+1)
                stack.append(s2)

arr = [6,3,9,1,0,4]
quickSortIterative(arr, 0, len(arr)-1)
print(arr)
    
