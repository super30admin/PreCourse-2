// Time Complexity :  O(nlogn) for average case and O(n^2) for worst case
// Space Complexity :  O(n)
// Did this code successfully run on Leetcode : No
// Any problem you faced while coding this : No

class QuickSort 
{ 
    /* This function takes last element as pivot, 
       places the pivot element at its correct 
       position in sorted array, and places all 
       smaller (smaller than pivot) to left of 
       pivot and all greater elements to right 
       of pivot */
    void swap(int arr[], int i,int j){
        //Your code here           
         
          int temp = arr[i];
          arr[i] = arr[j];
          arr[j] = temp;
    }
    
    int partition(int arr[], int low, int high) 
    { 
   	//Write code here for Partition and Swap 

       int i = low - 1;

      
        for(int j=low;j<high;j++){

            if(arr[j]<arr[high]){
                i = i+1;
                swap(arr, i, j);                 
            }
        }
       
       swap(arr, i+1, high);        
       return i+1;
    } 
    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    void sort(int arr[], int low, int high) 
    {  
            // Recursively sort elements before 
            // partition and after partition 

            if(low < high){
                int pi = partition(arr, low, high);

                sort(arr, low, pi-1);   //recursively sort left of pi
                sort(arr, pi+1, high);   //recursively  sort right of pi
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
