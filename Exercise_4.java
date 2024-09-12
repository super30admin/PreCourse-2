class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int  arrB[], int l, int m, int r) 
    {  
         //Your code here  
        int i = l;
        int k = l;
        int j = m+1;
        while(i<=m && j<=r) {
            if(arrB[i] <= arrB[j]) {
                arr[k++] = arrB[i++];
            }
            else {
                arr[k++] = arrB[j++];
            }
        }
        while(i<=m) {
            arr[k++] = arrB[i++];
        }
        while(j<=r) {
            arr[k++] = arrB[j++];
        }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	    //Write your code here
        //Call mergeSort from here 
        int[] arrB = new int[arr.length];
        System.arraycopy(arr, l, arrB, l, arr.length-1);
        sort(arr, arrB, 0, arr.length-1);
    } 

    void sort(int A[], int B[], int p, int r){
        if(p<r) {
    		int q = p + (r-p)/2;
    		sort(B, A, p, q);
    		sort(B, A, (q+1), r);
    		merge(A, B, p, q, r);
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