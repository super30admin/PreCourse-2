class Exercise_4 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       // calculate lengths of the two arrays
       int len1 = m - l + 1, len2 = r - m;

       //new left and right arrays of about size
       int left[] = new int[len1], right[] = new int[len2];

       //copy elements to above temp array
       for (int i = 0; i < len1; ++i){
            left[i] = arr[l + i];
       }
        
       //copy elements to above temp array
       for (int j = 0; j < len2; ++j){
            right[j] = arr[m + 1 + j];
       }
    
       //initialize k as start index of the meged array
       int k = l,i = 0, j = 0;;
       while (i < len1 && j < len2) {
           if (left[i] <= right[j]) {
               arr[k] = left[i];
               i++;
           }
           else {
               arr[k] = right[j];
               j++;
           }
           k++;
       }

       // if there are elements left in left array, copy them
       while (i < len1) {
           arr[k] = left[i];
           i++;
           k++;
       }

       //if there are elements right in left array, copy them
       while (j < len2) {
           arr[k] = right[j];
           j++;
           k++;
       }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
        if (l < r) {
            // calculate mid 
            int mid = l + (r - l) / 2;
 
            // we sort both the halves
            sort(arr, l, mid);
            sort(arr, mid + 1, r);
 
            // after sorting merge the halves
            merge(arr, l, mid, r);
        }
    } 
  
    /* A utility function to print array of size n */
    static void printArray(int arr[]) 
    { 
        int n = arr.length; 
        for (int i=0; i<n; ++i) 
            System.out.print(arr[i] + " "); 
        System.out.println(); 
    } 
  
    // Driver method 
    public static void main(String args[]) 
    { 
        int arr[] = {12, 11, 13, 5, 6, 7}; 
  
        System.out.println("Given Array"); 
        printArray(arr); 
  
        Exercise_4 ob = new Exercise_4(); 
        ob.sort(arr, 0, arr.length-1); 
  
        System.out.println("\nSorted array"); 
        printArray(arr); 
    } 
} 