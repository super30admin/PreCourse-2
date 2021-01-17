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
       // pivot (Element to be placed at right position)
    int pi = arr[high];  
 
    int i = (low - 1);  // Index of smaller element

    for (int j = low; j <= high- 1; j++)
    {
        // If current element is smaller than the pivot
        if (arr[j] < pi)
        {
            i++;    // increment index of smaller element
            swap (arr,i,j);
        }
    }
    swap (arr, i + 1 , high);
    return (i + 1);
    } 
    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    void sort(int arr[], int low, int high) 
    {  
            // Recursively sort elements before 
            // partition and after partition 
            if (low < high)
    {
        /* pi is partitioning index, arr[pi] is now
           at right place */
        int pi = partition(arr, low, high);

        sort(arr, low, pi - 1);  // Before pi
        sort(arr, pi + 1, high); // After pi
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





// class QuickSort 
// { 
//     /* This function takes last element as pivot, 
//        places the pivot element at its correct 
//        position in sorted array, and places all 
//        smaller (smaller than pivot) to left of 
//        pivot and all greater elements to right 
//        of pivot */
//     void swap(int arr[],int i,int j){
//         //Your code here 
//         int temp = arr[i];
//         arr[i] = arr[j];
//         arr[j] = temp;  
//     }
    
//     int partition(int arr[], int low, int high) 
//     { 
//        //Write code here for Partition and Swap 
//        return 0;
//     } 
//     /* The main function that implements QuickSort() 
//       arr[] --> Array to be sorted, 
//       low  --> Starting index, 
//       high  --> Ending index */
//     void sort(int arr[], int low, int high) 
//     {  
//             // Recursively sort elements before 
//             // partition and after partition 
//             if(low < high){
                
//             }
//     } 
  
//     /* A utility function to print array of size n */
//     static void printArray(int arr[]) 
//     { 
//         int n = arr.length; 
//         for (int i=0; i<n; ++i) 
//             System.out.print(arr[i]+" "); 
//         System.out.println(); 
//     } 
  
//     // Driver program 
//     public static void main(String args[]) 
//     { 
//         int arr[] = {10, 7, 8, 9, 1, 5}; 
//         int n = arr.length; 
  
//         QuickSort ob = new QuickSort(); 
//         // ob.sort(arr, 0, n-1); 
  
//         System.out.println("sorted array"); 
        
//         printArray(arr); 
//         System.out.println(arr[0]+arr[1]);
//         // ob.swap(arr,1,0);
//         // System.out.println(arr[0]+arr[1]);
//     } 
// } 
