// Time complexity: O(n2)
// Space Complexity: O(n)

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
        
        // select the last element as pivot
        int pivot = arr[high];
        int pivot_index = low;

        // move all the elements less than pivot to the left of pivot_index
        for(int i=low;i<high;i++) {
            if(arr[i] <= pivot) {
                swap(arr, i, pivot_index);
                pivot_index++;
            }
        }

        // Finally swap the pivot with pivot_index to place the pivot element at the right position
        swap(arr, pivot_index, high);

        return pivot_index;
    } 

    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    void sort(int arr[], int low, int high) 
    {  
        // base condition
        if (low >= high) {
            return;
        }

        int pivot_index = partition(arr, low, high);

        // Call sort function recursively for left and right array halves
        sort(arr, low, pivot_index - 1);
        sort(arr, pivot_index + 1, high);
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
