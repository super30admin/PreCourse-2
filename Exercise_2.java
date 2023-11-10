class QuickSort 
{ 
    /* This function takes last element as pivot, 
       places the pivot element at its correct 
       position in sorted array, and places all 
       smaller (smaller than pivot) to left of 
       pivot and all greater elements to right 
       of pivot */
    void swap(int arr[],int i,int j){
        //Your code here   
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
    
    //TC : O(nlogn)
    //SC : O(n)
    int partition(int arr[], int low, int high, int PivotIndex) 

    { 
   	//Write code here for Partition and Swap 
        int pivot = arr[PivotIndex]; 
        int lastmin = low;
        for(int current = low; current <=high;++current){
            if(arr[current] < pivot){
                swap(arr, current,++lastmin);
            }
  
        }
        swap(arr,PivotIndex,lastmin);
        return lastmin;

    } 
    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */

    void sort(int[] arr){
        auxQuickSort(arr, 0, arr.length-1);
         
    }

    void auxQuickSort(int arr[], int low, int high) 
    {  
            // Recursively sort elements before 
            // partition and after partition 

            if( low >= high) return;

            int pivotIndex = getPivotIndex(arr, low, high);
            int p = partition(arr, low, high, pivotIndex);
            auxQuickSort(arr, low, p-1);
            auxQuickSort(arr, p+1, high);

    } 
  
    private int getPivotIndex(int[] arr, int low, int high) {
        return low;
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

    public class Exercise_2{
        public static void main(String args[]) 
        { 
            int arr[] = {10, 7, 8, 9, 1, 5}; 
            int n = arr.length; 
            System.out.println("Unsorted array"); 
            QuickSort.printArray(arr); 
      
            QuickSort ob = new QuickSort(); 
            ob.sort(arr); 
      
            System.out.println("sorted array"); 
            QuickSort.printArray(arr); 
        } 
    }

