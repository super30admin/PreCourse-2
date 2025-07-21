// time complexity
//swap-O(1)
//partition-O(n) n being the length of partition
//quicksort-O(nlogn)/O(n^2)
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
        arr[i]=arr[i]^arr[j];
        arr[j]=arr[i]^arr[j];
        arr[i]=arr[i]^arr[j];
    }
    
    int partition(int arr[], int low, int high) 
    { 
   	//Write code here for Partition and Swap
        int pivot=arr[high];
        int boundary=low-1;

        for (int i = low; i < high; i++) {
            if(arr[i]<=pivot){
                boundary++;
                swap(arr,boundary,i);
            }
        }
        swap(arr,boundary,high);
        return boundary+1;

    }

    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    void sort(int arr[], int low, int high) 
    {  
            // Recursively sort elements before 
            // partition and after partition
        if(low<high){
            int index=partition(arr,low,high);
            sort(arr, low, index-1);
            sort(arr, index, high);
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
