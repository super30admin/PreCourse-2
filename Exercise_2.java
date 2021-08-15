// Time Complexity : The recursive solution presented performs comparision to last element as pivot,
// in best case scenario or unordered numbers it partitions at middle and keeps breaking array into half which would present itself as O(n log(n))
// But in case we have already ordered list it will traverse n-1 array each time and partition would remain at the end after each recursion worst case: O(n2)
// Space Complexity : Only an additional pivot and temp constant is required, so space complexity: O(1)
// Did this code successfully run on Leetcode : Could not find question on leet code
// Any problem you faced while coding this : Was facing Array out of bound index with j reaching high instead of high-1 and tried to swap arr[i] with arr[pivot] instead of arr[high]


// Your code here along with comments explaining your approach
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
        // genereic swapping using additional variable to store intermediate value
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
    
    int partition(int arr[], int low, int high) 
    { 
    //Write code here for Partition and Swap 
        // stored pivot value to compare values and performing swaps
        int pivot = arr[high];
        int i=low;
        int j = high-1;
        // breaking condition is when backward moving pointer crosses forward moving pointer
        // as till that point all the left partition would be lesser than pivot
        // and all the right partition greater than pivot
        while(i<j){
            // until we get an element moving from 0 to j which is more than pivot and also greater than element at jth position
            // we increment i pointer value
            while(arr[i]<pivot && arr[i]<=arr[j]) {
                i++;
            }
            // until we get an element moving from high to i which is less than pivot and also lesser than element at ith position
            // we decrement j pointer value
            while(arr[j]>pivot && arr[j]>=arr[i]) {
                j--;
            }
            // if i pointer is still less than j swap element at i and j positions
            if(i<j){
                swap(arr, i, j);
            }
        }
        // swap of ith position element is done with pivot only when ith element is greater else pivot is partitioned
        if(arr[i]> pivot) {
            swap(arr, i, high);
        }
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
        if(low<high)
        {
            // this returns partition position to recursive partitioned array with reference to p
            int p = partition(arr, low, high);
            // recursion in left partition
            sort(arr, low, p-1);
            // recursion in right partition
            sort(arr, p+1, high);
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
