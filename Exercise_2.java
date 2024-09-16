class QuickSort 
{    int pivot,temp,index,pindex,i,j;
    /* This function takes last element as pivot, 
       places the pivot element at its correct 
       position in sorted array, and places all 
       smaller (smaller than pivot) to left of 
       pivot and all greater elements to right 
       of pivot */
    void swap(int arr[],int i,int j){
        temp=arr[i];
        arr[i]=arr[j];
        arr[j]=temp; //Your code here   
    }
    
    int partition(int arr[], int low, int high) 
 { 
        int pivot = arr[high];
        int index = low - 1;
  
        for (int j = low; j <high ; j++) {
            if (arr[j] <= pivot) {
                index++;
               
                swap(arr, index, j);
            }
        }
        
        swap(arr, index + 1, high);
        return (index + 1); 
   	    
        //Write code here for Partition and Swap 
    } 
    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    void sort(int arr[], int low, int high) 
    {   if (low < high) {
        /* pi is partitioning index, arr[pi] is
        now at right place */
        int pi = partition(arr, low, high);

        // Recursively sort elements before
        // partition and after partition
        sort(arr, low, pi - 1);
        sort(arr, pi + 1, high);
    }
        // Recursively sort elements before 
            // partition and after partition 
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
