# Program name - Script to implement mergesort
# Author - Prajakta Pardeshi

# Time complexity - O(n)
# Space complexity  O(1) 


def mergeSort(arr):
    if len(arr) > 1:
        a = len(arr)//2
        l = arr[:a]
        r = arr[a:]

        mergeSort(l)
        mergeSort(r) 

        b = 0
        c = 0
        d = 0
        while b < len(l) and c < len(r):
            if l[b] < r[c]:
                arr[d] = l[b]
                b += 1
            else:
                arr[d] = r[c]
                c += 1
            d += 1

        while b < len(l):
            arr[d] = l[b]
            b += 1
            d += 1

        while c < len(r):
            arr[d] = r[c]
            c += 1
            d += 1


def printList(arr):

    for i in range(len(arr)):
        print(arr[i], end=" ")
 
    return

# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("\nSorted array is: ", end="\n") 
    printList(arr)