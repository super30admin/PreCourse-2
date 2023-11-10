//Complexity:
//Time: O(n log n)
//Space: O(n)
//Difficulty: understanding the pivot in partition.
//Approach: Taking last element as pivot. Check from second last element, if it is greater than pivot, then decrease s and swap the element at s with element at i.
//At last, swap the pivot with s to put pivot at sorted position.
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
        int p = arr[high];
        int s = high;

        for(int i = high-1; i>=0; i--) {
            if(arr[i] > p) {
                s--;
                swap(arr, i, s);
            }
        }
        swap(arr, high, s);
        return s;
    } 
    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    void sort(int arr[], int low, int high) 
    {  
            // Recursively sort elements before 
            // partition and after partition 
            int s = partition(arr, low, high);
            if(s == high) {
                return;
            } else if(s < high) {
                sort(arr, s+1, high);
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
