# Python program for implementation of Quicksort Sort 
  


# Function to do Quick sort 
     def quickSort(arr,low,high): 
        if len(arr)<=1:
            return arr
        else:
            pivot = arr[-1]
        items_greater =[]
        items_lower =[]
        for item in arr:
            if item>pivot:
               items_greater.append(item)  
            else: 
                items_lower.append(item) 
        return quickSort(items_lower) + [pivot] + [items_greater]
        
    
  
        # Driver code to test above 
        arr = [10, 7, 8, 9, 1, 5] 
        n = len(arr) 
        q=quickSort(arr,0,n-1) 
        print ("Sorted array is:") 
        print(q) 
        
  
 
