class Exercise_2 
{ 
    /* This function takes last element as pivot, 
       places the pivot element at its correct 
       position in sorted array, and places all 
       smaller (smaller than pivot) to left of 
       pivot and all greater elements to right 
       of pivot */
    void swap(int arr[],int i,int j){
        //store first element in temp variable
        int temp= arr[i];
        //allocate the value of second variable
        arr[i]=arr[j]; 
        //allocate stored value of first variable in second variable
        arr[j] = temp; 
    }
    
    int partition(int arr[], int low, int high) 
    { 
        //assign the last element as pivot
       int pivot = arr[high];
  
       //for reference store index of smaller element
       int x = (low - 1);
 
       for (int i = low; i <= high - 1; i++) {
            //check if the current element is smaller than pivot
           if (arr[i] < pivot) {
               //increament smaller index  
               x++;
               swap(arr, x, i);
           }
       }
       swap(arr, x + 1, high);
       return (x + 1); 
    } 
    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    void sort(int arr[], int low, int high) 
    {  
        //check if low does not exceed high
        if(low<high){
            //we have found the split index 
            int split=partition(arr,low,high);
            //sort elements before split index
            sort(arr, low, split - 1);
            //sort elements after split index
            sort(arr, split + 1, high);
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
  
        Exercise_2 ob = new Exercise_2(); 
        ob.sort(arr, 0, n-1); 
  
        System.out.println("sorted array"); 
        printArray(arr); 
    } 
} 
