class QuickSort 
{ 
    /* This function takes last element as pivot, 
       places the pivot element at its correct 
       position in sorted array, and places all 
       smaller (smaller than pivot) to left of 
       pivot and all greater elements to right 
       of pivot */
    void swap(int arr[],int low,int high){
        //Your code here   
    	if (low == high) return;
        int tmp = arr[low];
        arr[low] = arr[high];
        arr[high] = tmp;
    }
    
    int partition(int arr[], int low, int high) 
    { 
   	//Write code here for Partition and Swap 
    	 int pivot = arr[high];
         int i = low; // place for next <= pivot
         for (int j = low; j < high; j++) {
             if (arr[j] <= pivot) {
                 swap(arr, i, j);
                 i++;
             }
         }
         swap(arr, i, high);
         return i;
    } 
    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    void sort(int arr[], int low, int high) 
    {  
            // Recursively sort elements before 
            // partition and after partition 
    	if (low >= high) return;
        int p = partition(arr, low, high);
        sort(arr, low, p - 1);
        sort(arr, p + 1, high);
    	
    } 
  
     
  
    
}

public class Exercise_2{

	// Driver program 
    public static void main(String args[]) 
    { 
        int arr[] = {10, 7, 8, 9, 1, 5}; 
        int n = arr.length; 
  
        System.out.println("Before sorted array"); 
        printArray(arr); 
        System.out.println("---");
        QuickSort ob = new QuickSort(); 
        ob.sort(arr, 0, n-1); 
  
        System.out.println("sorted array"); 
        printArray(arr); 
    }
    
    /* A utility function to print array of size n */
    static void printArray(int arr[]) 
    { 
        int n = arr.length; 
        for (int i=0; i<n; ++i) 
            System.out.print(arr[i]+" "); 
        System.out.println(); 
    }
}
