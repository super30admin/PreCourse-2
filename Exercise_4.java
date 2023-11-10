// Time Complexity : O(NlogN)
// Space Complexity : O(N)
// Did this code successfully run on Leetcode :
class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here
       // creating the 2 array which needs to be sorted and merged
       int l1 = m-l+1;
       int l2 = r-m;
       int[] arr1 = new int[l1];
       int[] arr2 = new int[l2];
       for(int i = 0; i < l1; i++) {
        arr1[i] = arr[l+i]; 
       }
       for(int i = 0; i < l2; i++) {
        arr2[i] = arr[m+1+i]; 
       }
       //now sorting the arrays
       int i = 0; 
       int j = 0;
       int k = l;

       while(i < l1 && j < l2) {
        if(arr1[i] < arr2[j]) {
            arr[k] = arr1[i];
            i++;
        } else {
            arr[k] = arr2[j];
            j++;
        }
        k++;
       }
       // for remaining elements in one of the arrays
       while(i < l1) {
        arr[k] = arr1[i];
        i++;
        k++;
       }

       while(j < l2) {
        arr[k] = arr2[j];
        j++;
        k++;
       }

    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 
        if(l != r) {
            int pivot = (l+r)/2;
            sort(arr, l, pivot);
            sort(arr, pivot+1, r);
           this.merge(arr, l, pivot, r);
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