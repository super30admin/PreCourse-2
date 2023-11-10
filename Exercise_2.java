/*Algorithm: Quick Sort
 * 1. Get the partition Index
 *      1.1 Last element is always Pivot
 *      1.2 Initially low index is a partition index
 *      1.3 compare pivot with each element and partition array around partition index => Less than <-- Partition Index --> Greater than
 *      1.4 At the end, Swap pivot element with the partition index element
 * 2. Recursively Sort left part of array
 * 3. Recursively Sort right part of the array
 *  
 * Time Complexity: O(n log n) // Best Case
 *                : O(n^2) // Worst Case      
 * Space Complexity: O(n)
*/
class QuickSort 
{ 
    /* This function takes last element as pivot, 
       places the pivot element at its correct 
       position in sorted array, and places all 
       smaller (smaller than pivot) to left of 
       pivot and all greater elements to right 
       of pivot */
    void swap(int arr[], int i, int j){
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
    
    int partition(int arr[], int low, int high) 
    { 
   	    //Write code here for Partition and Swap 
        int pivot = arr[high];  // Last element is always Pivot
        int partitionIndex = low; // Initially low index is a partition index

        //Logic to partition array around partition index => Less than <-- Partition Index --> Greater than
        for(int i = low; i < high; i++)
        {
            if(arr[i] <= pivot)
            {
                swap(arr, i, partitionIndex);
                partitionIndex++;
            }
        }
        swap(arr, partitionIndex, high); // At the end, Swap pivot element with the partition index element 

        return partitionIndex;
    } 

    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    void sort(int arr[], int low, int high) 
    {  
        // Recursively sort elements before partition and after partition 
        //Base condition ==> When there is only one element in array means no further divide, previous recursive call send incremented low index, then break.
        if(low > high)
        {
            return;
        }

        //Get the partition Index
        int partitionIndex = partition(arr, low, high);
        //Sort left part of array
        sort(arr, low, partitionIndex-1);
        //Sort right part of the array
        sort(arr, partitionIndex+1, high);
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