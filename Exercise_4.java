//Complexity:
//Time:O(n log n)
//space:
//Defficulty: Unable to implement the merge method due to single array use.

class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
       int i=0, j=0, k=0;
       int arr1[] = new int[r-l];
       int arr2[] = new int[r-m];
       for(int n=0; n<=r-l-1; n++) {
        arr1[n] = arr[l+n];
       }
       for(int n=0; n<=r-m-1; n++) {
        arr2[n] = arr[m+n+1];
       }

       while(i<=r-m-1 && j<=r-m-1) {
        if(arr1[i]<=arr2[j]) {
            arr[k] = arr1[i];
            i++;
        } else {
            arr[k] = arr2[j];
            j++;
        }
        k++;
       }
       if(i==m+1){
        for(int n=j;n<arr2.length;n++) {
            arr[i] = arr2[n];
            i++;
        }
       } else {
        for(int n=i;n<arr1.length;n++) {
            arr[m+n] = arr1[n];
        }
       }


    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 
        if(l!=r) {
            int m = Math.round((l+r)/2);
            sort(arr, l, m);
            sort(arr, m+1, r);
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