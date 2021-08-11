class QuickSort 
{ 
    /* This function takes last element as pivot, 
       places the pivot element at its correct 
       position in sorted array, and places all 
       smaller (smaller than pivot) to left of 
       pivot and all greater elements to right 
       of pivot */
   
    
    int partition(int arr[], int low, int high) 
    { 
   	//Write code here for Partition and Swap
       int count=0;
       int pivotElement = arr[low];
       for(int i=low;i<=high;i++){
           if(arr[i]<pivotElement){
               count++;
           }
       }
       
       int temp = arr[low+count];
       arr[low+count]= pivotElement;
       arr[low] = temp;
    
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
        sort(arr,low,index-1);
        sort(arr,index+1,high);

            // Recursively sort elements before 
            // partition and after partition 
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
