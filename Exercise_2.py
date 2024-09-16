def partition(arr,low,high):
    print("partion",arr)
    pivot=arr[high]
    index=low
    current=low
    while(current<high):
        if(arr[current]<=pivot):
            arr[index],arr[current]=arr[current],arr[index]
            index=index+1
        current=current+1
    arr[high],arr[index]=arr[index],arr[high]
    print("partition",arr)
    return index


def quicksort(arr,low,high):
    if(low<high):
        index=partition(arr,low,high)
        quicksort(arr,low,index-1)
        quicksort(arr,index+1,high)
if __name__=="__main__":
    arr=[10,7,8,9,1,5]
    n=len(arr)
    print("he")
    quicksort(arr,0,n-1)
    print("sorted array is :")
    for i in range(n):
        print("%d" %arr[i])
  
 
