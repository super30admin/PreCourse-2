/* Time Complexity : O(nlogN) Worst case O(n2)
// Space Complexity :O(n)
// Did this code successfully run on Leetcode :yes
// Any problem you faced while coding this :no
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
        int pivotIndex = high;
        while(low<high){
            while(arr[low]<=pivot && low<high){
                low++;
            }
            while(arr[high]>=pivot && low<high){
                high--;
            }
            if(low<high){
                swap(arr,low,high);
            }
           
        }
        System.out.println("Swapping pivot elements "+ arr[pivotIndex] +"and " + arr[high]);
        swap(arr,pivotIndex,high);
        return high;

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

            int pivot = partition(arr,low,high);
            sort(arr,low,pivot-1);
            sort(arr,pivot+1,high);
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
/*Ouput:
 * 
 * Pivot index 5
Swapping elements 10and 1
Swapping pivot elements 5and 7
Pivot index 5
Swapping pivot elements 7and 8
Pivot index 5
Swapping pivot elements 8and 9
Pivot index 5
Swapping pivot elements 9and 10
sorted array
1 5 7 8 9 10 
 */
