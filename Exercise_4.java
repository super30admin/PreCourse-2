// Time Complexity : O(n logn)
// Space Complexity :O(n)
// Did this code successfully run on Leetcode :Yes
// Any problem you faced while coding this :No

class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here
        int num1 = m-l+1;
        int num2 = r-m;  

        //temp arrs
        int arr1[] = new int[num1];
        int arr2[] = new int[num2];

        for(int i = 0; i<num1; i++){
            arr1[i] = arr[l + i];
        }
        for(int k = 0; k < num2; k++){
            arr2[k] = arr[m+1+k];
        }

        int a = 0, b = 0;
        //set equal to first index of merged subarray
        int c = l;

        while(a < num1 && b < num2){
            if(arr1[a] <= arr2[b]){
                arr[c] = arr1[a];
                a++;
            }else{
                arr[c] = arr2[b];
                b++;
            }
            c++;
        }
        while(a < num1){
            arr[c] = arr1[a];
            a++;
            c++;
        }
        while(b < num2){
            arr[c] = arr2[b];
            b++;
            c++;
        }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 
        if(l<r){
            int mid = (l+r)/2;

            //sort halves then merge
            sort(arr, l, mid);
            sort(arr, mid+1, r);
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