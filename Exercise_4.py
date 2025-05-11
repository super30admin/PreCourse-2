# Python program for implementation of MergeSort 
def merge(arr, start, mid, end):
    buf = [0]*(end-start+1)
    bufi = 0 # buffer to merge
    i = 0 # first half
    j = mid+1 # second half
    for _ in range(start, end+1):
        if i > mid:
            buf[bufi] = arr[j]
            j += 1
        elif j > end:
            buf[bufi] = arr[i]
            i += 1
        elif arr[i] > arr[j]:
            buf[bufi] = arr[j]
            j += 1
        else:
            buf[bufi] = arr[i]
            i += 1
        bufi += 1
    # write the sorted buffer back to arr
    for n in buf:
        arr[start] = n
        start += 1

def mergeSort(arr, start, end):
    if start >= end:
        return
    mid = (start + end)//2
    mergeSort(arr, start, mid) # run mergeSort on each half
    mergeSort(arr, mid+1, end)
    merge(arr, start, mid, end) # merge the sorted halves

# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is:", arr)  
    mergeSort(arr, 0 , len(arr)-1) 
    print("Sorted array is:", arr) 
