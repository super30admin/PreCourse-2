/*
 * 
 * Time Complexity : O(nlogn) ~ logn to divide, n to merge
 * Space Complexity : O(n) ~ temporary arrays initialized during merge
 * Did this code successfully run on Leetcode : Yes
 *  Any problem you faced while coding this : 
 * -- Struggled to figure out merge code
 * -- Found it quite tricky to play with the indices, specially m and r
 * -- Referred to this video ~ https://www.youtube.com/watch?v=SHqvb69Qy70

 */


class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
       int n1 = m - l + 1;
        int n2 = r - m;

        int[] lArr = new int[n1];
        int[] rArr = new int[n2];

        for(int i = 0;i<n1;i++) {
            lArr[i] = arr[l + i];
        }

        for(int i = 0;i<n2;i++) {
            rArr[i] = arr[m + 1 + i];
        }

        int i = 0;
        int j = 0;
        int k = l;

        while(i < n1 && j < n2) {
            if(lArr[i] < rArr[j]) {
                arr[k] = lArr[i];
                i++;
                k++;
            } else {
                arr[k] = rArr[j];
                j++;
                k++;
            }
        }

        while(i < n1) {
            arr[k] = lArr[i];
            i++;
            k++;
        }

        while(j < n2) {
            arr[k] = rArr[j];
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
        if(l == r) {
            return;
        }

        int middle = (l+r)/2;
        sort(arr, l, middle);
        sort(arr, middle+1, r);
        merge(arr, l, middle, r);
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