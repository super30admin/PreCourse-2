// Time Complexity : O(n log n)
// Space Complexity : O(n log n)
// Any problem you faced while coding this : None.

class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       int subArr1;
       int subArr2;
       
       subArr1 = m - l + 1;
       subArr2 = r - m;

       // Temp arrays to store the right and left sides of the arrays
       int leftSide[]  = new int[subArr1];
       int rightSide[] = new int[subArr2];

       // Move elements to temp array

       for(int i = 0; i < subArr1; ++i){
           leftSide[i] = arr[l + i];
        }
       for(int j = 0; j < subArr2; ++j){
            rightSide[j] = arr[m + 1 + j];
        }

        int i; //subArr1 index
        int j; //subArr2 index
        int k; //merged array index

        i = 0;
        j = 0;
        k = l;

        // Start merging the indexes from both subarrays
        while(i < subArr1 && j < subArr2) {
            if (leftSide[i] <= rightSide[j]) { //left side should not overlap over the right side
                arr[k] = leftSide[i];
                i++;
            }
            else{
                arr[k] = rightSide[j];
                j++;
            }
            k++;
        }

        // copy elements from left side
        while (i < subArr1) {
            arr[k] = leftSide[i];
            i++;
            k++;
        }

        // copy elements from right side
        while (i < subArr2) {
            arr[k] = rightSide[j];
            j++;
            k++;
        }

    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
        // left index must be lower than the right index
        if (l < r) {
            int m; 
            m = l + (r - l) / 2;
            
            //sort left
            sort(arr, l, m);
            //sort right
            sort(arr, m+1, r);

            // Merge subarrays
            merge(arr, l, m, r);
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
  
        MergeSort ob = new MergeSort(); 
        ob.sort(arr, 0, arr.length-1); 
  
        System.out.println("\nSorted array"); 
        printArray(arr); 
    } 
} 