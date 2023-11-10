# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, low, high):
    pivot = arr[low]
    i = low
    j = high
    while i <= j:
        #moving one pointer to right
        while arr[i] <= pivot:
            i += 1
        #moving other pointer to left
        while arr[j] >= pivot:
            j -= 1

        if i <= j:
            print("SWITCHING",arr,arr[i],arr[j])
            arr[i],arr[j] = arr[j],arr[i]
            i += 1
            j -= 1
    if arr[j] < pivot:
        arr[j], arr[low] = arr[low], arr[j]
    return j


def quickSort(arr, low, high):
    temp = []
    temp.append(low)
    temp.append(high)
    print("Before",temp)
    while len(temp) is not 0:
        high=temp.pop()
        low= temp.pop()
        print("In loop",temp, low,high)
        pi = partition(arr,low,high)
        print('Partition',pi,arr)
        if low < pi -1:
            temp.append(low)
            temp.append(pi -1)

        if pi +1 < high:
            temp.append(pi+1)
            temp.append(high)


arr = [2, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print ("Sorted array is:")
for i in range(n):
    print ("%d" % arr[i]),
