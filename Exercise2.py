def quicksort(arr):
    #when left part of right part is left with one number or no number; stop the recursion
    if (len(arr) ==0) or (len(arr)==1):
        return arr
    #considering first element as pivot
    pivot = arr[0]
    i = 0
    for j in range(len(arr)):
        if arr[j] < pivot:
            # swap values of arr[i] and arr[j] after increamenting i value
            i += 1
            arr[j],arr[i] = arr[i], arr[j]
    # swap pivot and arr[i] values
    arr[0],arr[i] = arr[i],arr[0]
    #call quickSort function for left part of list till pivot index
    left = quicksort(arr[:i])
    # add pivot to the list
    left.append(arr[i])
    return left+ quicksort(arr[i+1:])  # calling quick sort for right part of the list

alist = [54,26,93,17,77,31,0,9,2,4,6,90]
print("original array is ",alist)
print("sorted array: ",quicksort(alist))


'''
#output
original array is  [54, 26, 93, 17, 77, 31, 0, 9, 2, 4, 6, 90]
sorted array:  [0, 2, 4, 6, 9, 17, 26, 31, 54, 77, 90, 93]

'''
