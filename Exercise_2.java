//Time Complexity:
// Worst case: O(n^2)
// Best and Average case: O(nlogn)
//Space Complexity:
// Worst case: O(n)
// Best and Average Case: O(logn)


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
    
    int partition(int arr[], int low, int high) 
    { 
   	  //Write code here for Partition and Swap 
       int left = low;
       int right = high;
       int pivot = arr[high];

       while(left < right)
       {
           while(arr[left] <= pivot && left < right)
           {
               left = left+1;
           }
           while(arr[right] >= pivot && left < right)
           {
               right = right-1;
           }
            swap(arr, left, right);                   
       }
       swap(arr, left, high);
       return left;
    } 
    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    void sort(int arr[], int low, int high) 
    {  
        // Recursively sort elements before 
        // partition and after partition 
        if(low >= high)
        {
            return; // array of single element
        }

        int left = partition(arr, low, high);
      
        sort(arr, low, left-1);
        sort(arr, left+1, high);

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
