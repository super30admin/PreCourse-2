class MergeSort 
{ 
       // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
       // create two sub arrays of length l to m and m to r
        int l1 = m - l + 1;
        int l2 = r - m;

        int[] arr1 = new int[l1];
        int[] arr2 = new int[l2];
        // copy the values from original array to the two new subarrays
        for(int i=0; i<l1; i++) {
            arr1[i] = arr[l+i];
        }

        for(int i=0; i<l2; i++) {
            arr2[i] = arr[m + 1 + i];
        }

        int i=0, j=0, k=l; // i - index for left sub array and j - index for the right sub array and k - index for the original array
        while (i<l1 && j<l2) { //compare the subarrays and fill the original array in the sorted order
            if(arr1[i] <= arr2[j]) {
                arr[k++] = arr1[i++];
            } else {
                arr[k++] = arr2[j++];
            }
        }

        //if there are elements remaining in left sub array
        while(i < l1) {
            arr[k++] = arr1[i++];
        }

        //if there are elements remaining in right sub array
        while(j < l2) {
            arr[k++] = arr2[j++];
        }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 
        if(l >= r)
            return;
        
        int mid = l + (r-l)/2;
        sort(arr, l , mid);
        sort(arr, mid + 1, r);
        merge(arr, l, mid, r);
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