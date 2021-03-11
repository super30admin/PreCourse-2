# Python program for implementation of Quicksort Sort

# give you explanation for the approach
def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] < pivot:
            i = i + 1

            # SWAP i, j
            arr[i], arr[j] = arr[j], arr[i]

    # SWAP i +1 and Pivot
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    print (arr)
    return (i + 1)

    # write your code here


# Function to do Quick sort
def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    top = 0
    stack = []
    stack.append(low); top +=1
    stack.append(high); top +=1
    print(stack)


    while top > 0:
        h = stack.pop(); top -=1
        l = stack.pop(); top -=1

        pivot = partition(arr, l, h)
        print (f"pivot index is {pivot}")

        if l < pivot-1:
            stack.append(l); top += 1
            stack.append(pivot-1);top +=1
            print("left index range" + str(stack))
        if pivot+1 < h:
            stack.append(pivot+1);top += 1
            stack.append(h);top += 1
            print("right index range" + str(stack))


# write your code here

# Driver code to test above
arr = [10, 7, 8, 9, 1, 5,2,3,5,213,2,32,3,23,7,56,7,3,31,34,3]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i])