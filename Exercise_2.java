// Time Complexity : O(nlog n)
// Space Complexity : O(n)

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
        int temp = arr[i]; // temp variable is used to swap the elements
        arr[i] = arr[j];
        arr[j] = temp;  
    }
    
    int partition(int arr[], int low, int high) 
    { 
   	//Write code here for Partition and Swap 
        int i=low, j=high-1, pivot=arr[high]; // the last element in the array is choosen as the pivot

        while(i<j){
            while(arr[i]<=pivot && i<high-1){ // increment i if the element is less than or equal to pivot
                i++;
            }

            while(arr[j]>pivot && j>low){ // decrement j if the element is greater than pivot
                j--;
            }

            if(i<j){        // swap elements at position i and j if i<j
                swap(arr, i, j);
            }
        }

        swap(arr, i, high); // if i>=j, swap element at i with pivot

        return i; // i is the position where the pivot is fixed
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
                int pivotIdx = partition(arr, low, high);  // save the pivot fixed index
                sort(arr, low, pivotIdx-1);  // sort the left side array to the pivot
                sort(arr, pivotIdx+1, high); // sort the right side array to the pivot
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
  
        System.out.println("sorted array:"); 
        printArray(arr); 
    } 
} 
