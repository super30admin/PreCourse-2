class QuickSort 
{ 
    /* This function takes last element as pivot, 
       places the pivot element at its correct 
       position in sorted array, and places all 
       smaller (smaller than pivot) to left of 
       pivot and all greater elements to right 
       of pivot */
     void swap(int i,int j,int arr[]){
        //Your code here  
        
        int temp = arr[j];
        arr[j] = arr[i];
        arr[i] = temp;
    }
    
    // int partition(int arr[], int low, int high) 

    void sort(int arr[], int low, int high) 
    {  
        if(low >= high)
        {
            return;
        }
        int pivotIdx = low;
        int l = low + 1;
        int r = high;

        while(r >= l)
        {
            if(arr[l] > arr[pivotIdx] && arr[r] < arr[pivotIdx])
            {
                swap(l , r , arr);
            }
            if(arr[l] <= arr[pivotIdx])
            {
                l += 1;
            }
            if(arr[r] >= arr[pivotIdx])
            {
                r -= 1;
            }
        }

        swap(pivotIdx, r , arr);
        boolean leftsubarray = r - 1 - low < high - (r + 1);
        if(leftsubarray)
        {
            sort(arr,l,r-1);
            sort(arr, r+1 , high);
        }else{
            sort(arr,r+1, high);
            sort(arr, low , r-1);
            
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
        int arr[] = {10, 7, 8, 9, 1, 5}; 
        int n = arr.length; 
  
        QuickSort ob = new QuickSort(); 
        ob.sort(arr, 0, n-1); 
  
        System.out.println("sorted array"); 
        printArray(arr); 
    } 
} 
