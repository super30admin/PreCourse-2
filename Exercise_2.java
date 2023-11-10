class QuickSort 
{ 
    
    // Time Complexity : O(Nlog(N))
    // Space Complexity : O(1)
    // Did this code successfully run on Leetcode : Yes
    // Any problem you faced while coding this : No
   
    
    int partition(int arr[], int low, int high) 
    { 
   	/* This function takes first element as pivot, 
       places the pivot element at its correct 
       position in sorted array, and places all 
       smaller (smaller than pivot) to left of 
       pivot and all greater elements to right 
       of pivot */
       int count=0;
       //finding total number of elements lower than pivot element
       int pivotElement = arr[low];
       for(int i=low;i<=high;i++){
           if(arr[i]<pivotElement){
               count++;
           }
       }
       // swapping the pivot element to correct position
       int temp = arr[low+count];
       arr[low+count]= pivotElement;
       arr[low] = temp;
    
       //putting elements lower than pivot its left and greater than on its right
       int lower = low;
       int higher = high;
       while(lower<higher){
            if(arr[lower] <pivotElement){
                lower++;
            }else if(arr[higher]>=pivotElement){
                higher--;
            }else{
                 temp = arr[lower];
                arr[lower]= arr[higher];
                arr[higher]= temp;       
            }
       }
       //returns the index of pivot element
       return low+count;


    } 
    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    void sort(int arr[], int low, int high) 
    {  
        if(low>=high){
            return;
        }
        int index= partition(arr,low,high);
         // Recursively sort elements before 
            // partition and after partition 
        sort(arr,low,index-1);
        sort(arr,index+1,high);

           
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
        int arr[] = {10, 8, 8, 9, -1, 5}; 
        int n = arr.length; 
  
        QuickSort ob = new QuickSort();
          
        ob.sort(arr, 0, n-1); 
  
        System.out.println("sorted array"); 
        printArray(arr); 
    } 
} 
