//Problem 2: Quick Sort

//   Time Complexity : The worst time complexity for this problem is O(n^2) if the elements are already in sorted order and it would be O(n log n)
//                      n times for partinioning and log n times for recursion.
//   Space Complexity : Space complexity would be O(log n)
//   Any problem you faced while coding this : Stack tracing during recursion was difficult to keep track while debugg

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
        int pivot = arr[high];
        if(low <= high){
            for(int i =low;i<=high;i++){
                if(arr[i] < pivot) {
                    swap(arr, i, low);
                    low++;
                }
            }
            swap(arr,low,high);
        }
        return low;
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
            int partionEle = partition(arr,low,high);
            sort(arr,low,partionEle-1);
            sort(arr,partionEle + 1,high);
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
