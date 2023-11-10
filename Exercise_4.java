/*
    Time Complexity = O(NlogN)
    Space Complexity = O(N)
    Did this code successfully run on Leetcode : yes
 */


class MergeSort
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here
       int[] merged = new int[r-l+1];
       int s1 = l;
       int s2 = m+1;

        int i = 0;
        for(i = 0; i < merged.length; i++){
            if(s2 > r || s1 > m){
                break;
            }


           if(arr[s2] <= arr[s1]){
               merged[i] = arr[s2];
               s2++;
           }else{
               merged[i] = arr[s1];
                   s1++;
           }
       }

        if(s2 > r) {
            for (int j = s1; j<= m; j++ ) {
                merged[i] = arr[j];
                i++;
            }
        }

        if(s1 > m) {
            for (int j = s2; j<= r; j++ ) {
                merged[i] = arr[j];
                i++;
            }
        }

       int idx = 0;
       for(int j = l; j <= r; j++){
          arr[j] = merged[idx];
          idx++;
       }

    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here
        if(l==r){
            return;
        }
        int mid = (l+r)/2;
        sort(arr,l,mid);
        sort(arr,mid+1,r);

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
        int arr[] = {12, 11, 13, 5, 6, 7, 8};
  
        System.out.println("Given Array"); 
        printArray(arr); 
  
        MergeSort ob = new MergeSort(); 
        ob.sort(arr, 0, arr.length-1); 
  
        System.out.println("\nSorted array"); 
        printArray(arr); 
    } 
} 