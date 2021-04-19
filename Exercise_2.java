// Time Complexity : O(nlogn)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No

class QuickSort 
{ 
    /* This function takes last element as pivot, 
       places the pivot element at its correct 
       position in sorted array, and places all 
       smaller (smaller than pivot) to left of 
       pivot and all greater elements to right 
       of pivot */
    void swap(int arr[],int i,int j){
        int temp=arr[i];         // temp variable used for swapping i and j
        arr[i]=arr[j];
        arr[j]=temp;  
    }
    
    int partition(int arr[], int low, int high) 
    { 
   	//Write code here for Partition and Swap 
       int pivot=arr[high]; // Pivot to last element in an array

        int i=low;           // Fix pointer i to low element

        for(int j=low;j<high;j++){ // Iterate between low and high

            if(arr[j]<pivot){    

                swap(arr,i,j);   
                i++;
            }
                               
        }

       swap(arr,i,high);        // swap last element i with high/pivot to fix pivot in correct position such that all elements left of pivot are small
                                // and all elements right of pivot are greater.

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
            if(low<high){                           

                int index=partition(arr,low,high);   // Find pivot index using partition function
    
                sort(arr,low, index-1);              // Apply sort for elements less than pivot
    
                sort(arr,index+1,high);             // apply sort for elements greater than pivot
    
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
