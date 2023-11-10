class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here
       // need left and right array. In-place merge using swap is not possible
       // we need auxilary space
       int n = r-l+1;
       int[] ret = new int[n];

       int i = l;
       int j = m+1;
       int k = 0;
       while (i<=m && j<=r) {
        if(arr[i] < arr[j]) {
            ret[k] = arr[i];
            i++;
        } else {
            ret[k] = arr[j];
            j++;
        }
        k++;
       }

       // remaining elements
       while(i<=m) {
        ret[k] = arr[i];
        i++;
        k++;
       }
       while(j<=r) {
        ret[k] = arr[j];
        j++;
        k++;
       }

       // copy sorted elements to array
       k=0;
       for (i=l; i<=r; i++) {
        arr[i] = ret[k];
        k++;
       }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
    if (l == r) return;
    if (arr.length >1){
        int mid = l + (r-l)/2;

        sort(arr, l, mid);
        sort(arr, mid+1, r);

        //Call mergeSort from here
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
  
        MergeSort ob = new MergeSort(); 
        ob.sort(arr, 0, arr.length-1); 
  
        System.out.println("\nSorted array"); 
        printArray(arr); 
    } 
} 