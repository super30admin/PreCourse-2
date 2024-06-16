// Time Complexity : O(n log n)
    // Space Complexity : O(n)
    // Did this code successfully run on Leetcode : Yes 
    // Any problem you faced while coding this :I cannot understand how the array is getting splitted up and sorted through recursion and its confusing. Please help
// Approach:
//merge()-> takes two temperary arrays and stores the values of left and right arrays seperately. Compares the values individually between left and right arrays and collects into a single arr array . Finally checks for left out values in left and right arrays and includes them to the array.


class Exercise_4 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
        int arr1 = m - l + 1;
        int arr2 = r - m;

        int leftarr[] = new int[arr1];
        int rightarr[] = new int[arr2];

        for (int i = 0; i < arr1; ++i)
            leftarr[i] = arr[l + i];
        for (int j = 0; j < arr2; ++j)
            rightarr[j] = arr[m + 1 + j];

        int i = 0, j = 0;
        int k = l;
        while (i < leftarr.length && j < rightarr.length) {
            if (leftarr[i] <= rightarr[j]) {
                arr[k] = leftarr[i];
                i++;
            } else {
                arr[k] = rightarr[j];
                j++;
            }
            k++;
        }
        while (i < leftarr.length) {
            arr[k] = leftarr[i];
            i++;
            k++;
        }

        while (j < rightarr.length) {
            arr[k] = rightarr[j];
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
        if(l<r){
            int mid=(l+r)/2;
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
  
        Exercise_4 ob = new Exercise_4(); 
        ob.sort(arr, 0, arr.length-1); 
  
        System.out.println("\nSorted array"); 
        printArray(arr); 
    } 
} 