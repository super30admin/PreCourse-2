class QuickSort 
{ 
    /* This function takes last element as pivot, 
       places the pivot element at its correct 
       position in sorted array, and places all 
       smaller (smaller than pivot) to left of 
       pivot and all greater elements to right 
       of pivot */
    void swap(int arr[],int i,int j){   
        int t=arr[i];
        arr[i]=arr[j];
        arr[j]=t;
    }
    
    int partition(int arr[], int low, int high) 
    { 
   	//Write code here for Partition and Swap 
       int pivot=arr[low];
       int start=low;
       int end=high;
       while(start<end){
           for(int i=0; i<end;i++){
               if(arr[start]<=pivot){
                   start++;
               }
           }
           while(arr[end]>pivot){
               end--;
           }
           if(start<end){
               swap(arr,start,end);
           }
       }
       swap(arr,end,low);
       return end;
    } 
    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    void sort(int arr[], int low, int high) 
    {  
        if(low<high){
            int location=partition(arr,low,high);
            sort(arr,low,location-1);
            sort(arr,location+1,high);
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
