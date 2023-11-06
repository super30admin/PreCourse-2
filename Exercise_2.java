//Time complexity : Worst Case -> O(N^2), Average and Best Case -> O(N logN)
//Space Complexity : O(N) -> If recursive stack space is considered, O(1) -> If it is not considered
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
        //Eg : arr[i] = 10, arr[j] = 15
        int temp = arr[i]; //temp=10
        arr[i] = arr[j]; //arr[i]=15
        arr[j] = temp; //arr[j]=10
    }
    
    int partition(int arr[], int low, int high) 
    { 
   	//Write code here for Partition and Swap
        //Considering pivot as the last element of the range
        int pivot = arr[high];
        //Maintaining a pointer to push further the elements with greater value
        int i = low;

        //Check each element in the range if it is less than pivot,
        //If yes, then swap i and j
        for(int j=low; j<high; j++) {
            if(arr[j] < pivot) {
                if(i != j)
                    swap(arr, i, j);
                i++;
            }
        }

        //place the pivot at its correct position
        if(i != high)
            swap(arr, i, high);

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
        if(low < high) {
            int x = partition(arr, low, high);

            sort(arr, low, x-1);
            sort(arr, x+1, high);
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
        int arr[] = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1};
        int n = arr.length; 
  
        QuickSort ob = new QuickSort(); 
        ob.sort(arr, 0, n-1); 
  
        System.out.println("sorted array"); 
        printArray(arr); 
    } 
} 
