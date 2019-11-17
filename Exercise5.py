def partition(arr, low, high):
    i = (low - 1)         # index of smaller element
    pivot = arr[high]     # pivot
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    print("returning p as ",i+1)
    return (i+1)

#iterative quicksort using stack

# adding the next low and high values for each partition into stack
# stack is passed with initial low and high values
def quickSort(arr, low, high, stack):
    # Enter the loop if stack is not None
    while(stack):
        #
        low = stack.pop(0)
        high = stack.pop(0)
        # call partition function for low and high values
        p = partition(arr,low,high)
        # if partition index is greater than previous low index-----We should pass arr[low:p-1] to partition function
        if(p-1>low):
            # Adding new low and high values to stack
            stack.append(low)
            stack.append(p-1)
            print("appending values to stack: ",low, p-1)
        # if partition index is less than previous high index-----We should pass arr[p+1:] to partition function
        if(p+1<high):
            # Adding new low and high values to stack
            stack.append(p+1)
            stack.append(high)
            print("appending values to stack: ",p+1,high)


alist = [54,26,100,987,93,17,77,31,-1,-345,0,253678]
low = 0
high = len(alist)-1
stack = []
stack.append(low)
stack.append(high)
quickSort(alist,low,high,stack)
print("final array")
print(alist)


'''
#output


returning p as  11
appending values to stack:  0 10
returning p as  2
appending values to stack:  0 1
appending values to stack:  3 10
returning p as  0
returning p as  9
appending values to stack:  3 8
returning p as  4
appending values to stack:  5 8
returning p as  8
appending values to stack:  5 7
returning p as  6
final array
[-345, -1, 0, 17, 26, 31, 54, 77, 93, 100, 987, 253678]
'''
