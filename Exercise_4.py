# Python program for implementation of MergeSort 
def merge(l, r):
    solution = []

    l_ptr = 0
    r_ptr = 0

    while l_ptr < len(l) and r_ptr < len(r):

        if(l[l_ptr] < r[r_ptr]):
            solution.append(l[l_ptr])
            l_ptr += 1
        else:
            solution.append(r[r_ptr])
            r_ptr += 1

    solution.extend(l[l_ptr:])
    solution.extend(r[r_ptr:])


    return solution


def mergeSort(arr):

    if len(arr) > 1:

        mdpt = len(arr) // 2

        l = arr[:mdpt]
        r = arr[mdpt:]

        mergeSort(l)
        mergeSort(r)

        l_ptr = 0
        r_ptr = 0
        idx = 0
        while l_ptr < len(l) and r_ptr < len(r):

            if(l[l_ptr] < r[r_ptr]):
                arr[idx] = l[l_ptr]
                l_ptr += 1
            else:
                arr[idx] = r[r_ptr]
                r_ptr += 1
            idx += 1


        while l_ptr < len(l):         #emptying left array
            arr[idx] = l[l_ptr]
            l_ptr += 1
            idx += 1

        while r_ptr < len(r):         #emptying right array
            arr[idx] = r[r_ptr]
            r_ptr += 1
            idx += 1









  #write your code here


#edited


# Code to print the list 
def printList(arr): 
    for i in arr:
        print(i)

    #write your code here
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr)
    print("Sorted array is: ", end="\n") 
    printList(arr)
