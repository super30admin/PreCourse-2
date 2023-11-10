# Python program for implementation of Quicksort
#Time Complexity O(n*log n)
#Space Complexity O(n)
# This function is same in both iterative and recursive
def partition(arr,l,h):
    pivote=arr[h]
    i=l-1
    for j in range(l,h):
      if arr[j]<pivote:
          i+=1
          arr[i],arr[j]=arr[j],arr[i]
    i+=1
    arr[i], arr[h] = arr[h], arr[i]
    return i


def quickSortIterative(arr):
    # mimicing the recursion using while loop to sort
    st=[0,len(arr)-1]
    while(st):
        h=st.pop()
        l=st.pop()
        pivote=partition(arr,l,h)
        if pivote-1>l:
            st.append(l)
            st.append(pivote-1)
        if pivote+1<h:
            st.append(pivote+1)
            st.append(h)
    print(arr)

arr = [12, 11, 13, 5, 6, 7]
quickSortIterative(arr)


