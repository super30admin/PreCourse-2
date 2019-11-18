

class Iterative_quick_sort 
{ 
    /* This function takes last element as pivot, 
       places the pivot element at its correct 
       position in sorted array, and places all 
       smaller (smaller than pivot) to left of 
       pivot and all greater elements to right 
       of pivot */
    void swap(int arr[],int i,int j){
       int temp = arr[i]; 
        arr[i] = arr[j]; 
        arr[j] = temp; 
    }
    
    int partition(int arr[], int low, int high) 
    { 
   
        int pivot = arr[high];  
        int i = low; // index of smaller element 
        for (int j=low; j<high; j++) 
        { 
            // If current element is smaller than the pivot 
            if (arr[j] < pivot) 
            { 
               swap(arr, i,j);
                i++; 
            } 
        }
        swap(arr,i,high);
        return i;
        //Write code here for Partition and Swap 
    } 
    /* The main func
     * tion that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    void sort(int arr[], int l, int h) 
    {  
    	int[] stack = new int[h - l + 1]; 
    	  
        // initialize top of stack 
        int top = -1; 
  
        stack[++top] = l; 
        stack[++top] = h; 
  
        while (top >= 0) { 
            // Pop h and l 
            h = stack[top--]; 
            l = stack[top--]; 
  
            int p = partition(arr, l, h); 
  
            if (p - 1 > l) { 
                stack[++top] = l; 
                stack[++top] = p - 1; 
            } 
  
            if (p + 1 < h) { 
                stack[++top] = p + 1; 
                stack[++top] = h; 
            } 
        } 
    	
    } 
  
    /* A utility function to print array of size n */
    static void printArray(int arr[]) 
    { 
        int n = arr.length; 
        for (int i=0; i<n; ++i) 
            System.out.print(arr[i]+" "); 
        System.out.println(); 
    } 
  
    // Driver program 
    public static void main(String args[]) 
    { 
        int arr[] = {10, 7, 8, 9, 1, 1453,1,6427,461,100, 9,7832}; 
        int n = arr.length; 
  
        Iterative_quick_sort ob = new Iterative_quick_sort(); 
        ob.sort(arr, 0, n-1); 
  
        System.out.println("sorted array"); 
        printArray(arr); 
    } 
} 
