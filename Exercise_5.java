//Time complexity: O(n logn)
//Space complexity: O(1)
//Successfully executed on leetcode



class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
        int temp;
        temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
        int i = l-1;
        int p = arr[h];
        int j;
        int temp;
        for(j=l;j<=h-1;j++)
        {
            if(arr[j]<=p)
            {
                i++;
                swap(arr,i,j);
            }
        }
        swap(arr,i+1,h);

        return i+1;
        
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        if(l<h)
        {   
            int index = partition(arr,l,h);
            QuickSort(arr,l,index-1);
            QuickSort(arr, index+1, h);
            
        }        
    } 
  
    // A utility function to print contents of arr 
    void printArr(int arr[], int n) 
    { 
        int i; 
        for (i = 0; i < n; ++i) 
            System.out.print(arr[i] + " "); 
    } 
  
    // Driver code to test above 
    public static void main(String args[]) 
    { 
        IterativeQuickSort ob = new IterativeQuickSort(); 
        int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 }; 
        ob.QuickSort(arr, 0, arr.length - 1); 
        ob.printArr(arr, arr.length); 
    } 
} 