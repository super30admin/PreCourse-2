/*
 * Time Complexity: O(NlogN)
 * Space Complexity: O(N)
 */

class MergeSort 
{ 
    private int firstSubArray[];
    private int secondSubArray[];

    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here
       
       int size1 = m-l+1;
       int size2 = r-m;

       int firstSubArray[] = new int[size1];
       int secondSubArray[] = new int[size2];

       for(int i = 0; i < size1; i++){
            firstSubArray[i] = arr[l + i];
       }
       for(int j = 0; j < size2; j++){
            secondSubArray[j] = arr[m + 1 + j];
       }

       int p1 = 0;
       int p2 = 0;

       int k = l;
       while (p1 < size1 && p2 < size2) {
           if (firstSubArray[p1] <= secondSubArray[p2]) {
               arr[k] = firstSubArray[p1];
               p1++;
           } else {
               arr[k] = secondSubArray[p2];
               p2++;
           }
           k++;
       }

       // Copy remaining elements of L[] if any
       while (p1 < size1) {
           arr[k] = firstSubArray[p1];
           p1++;
           k++;
       }

       // Copy remaining elements of R[] if any
       while (p2 < size2) {
           arr[k] = secondSubArray[p2];
           p2++;
           k++;
       }

    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 
        if(l<r){
            int mid = (int)((l+r)/2);

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