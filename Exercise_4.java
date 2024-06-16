// Time Complexity : O(nlogn)
// Space Complexity : 0(n) 
// Did this code successfully run on Leetcode : yes
// Any problem you faced while coding this :

class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here
       //Build left and right sub arrays
        int leftSize = m-l+1;
        int rightSize = r-m;
        int[] leftArr = new int[leftSize];
        int[] rightArr = new int[rightSize];

        for(int i=0;i<leftSize;i++){
            leftArr[i] = arr[l+i];
        }
        for(int i=0;i<rightSize;i++){
            rightArr[i] = arr[m+1+i];
        }  
    
       // i and j are pointers to left and right subarrays
       //Starting with i and j, compare elements in left[i] and right[j], start filling the input array with smaller elements first
       int i=0;
       int j=0;
       int k = l;

        while (i<leftSize && j<rightSize) {
            if (leftArr[i] <= rightArr[j]) {
                arr[k] = leftArr[i];
                i++;
            }
            else {
                arr[k] = rightArr[j];
                j++;
            }
            k++;
        }

        // Copy remaining elements of left array
        while (i<leftSize) {
            arr[k] = leftArr[i];
            i++;
            k++;
        }

        // Copy remaining elements of right Array
        while (j<rightSize) {
            arr[k] = rightArr[j];
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
        int mid= (r+l)/2;
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