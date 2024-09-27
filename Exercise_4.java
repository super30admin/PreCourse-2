class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here
       int[] arr2 = new int[arr.length];
       System.arraycopy(arr, 0, arr2, 0, arr.length);
       int i = l, k = l, j = m + 1;
       while (i <= m && j <= r) {
           if (arr2[i] <= arr2[j]) {
               arr[k] = arr2[i];
               k++;
               i++;
           } else {
               arr[k] = arr2[j];
               k++;
               j++;
           }
       }

       while (i <= m) {
           arr[k] = arr2[i];
           k++;
           i++;
       }

       while (j <= r) {
           arr[k] = arr2[j];
           k++;
           j++;
       } 
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here
        if(l<r){
            int mid = l +(r-l)/2;
            sort(arr,l,mid);
            sort(arr,mid+1,r);
            merge(arr,l,mid,r);
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