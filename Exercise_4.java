// Time Complexity : O(NlogN)
// Space Complexity : O(N)
// Did this code successfully run on Leetcode :
// Any problem you faced while coding this :No

class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
       //First find sizes of the first and second array
       int size1 = m - l + 1; 
       int size2 = r - m;

       //Create temporary arrays
        int[] arr1 = new int[size1];
        int[] arr2 = new int[size2];
    
        //copy data to temporary arrays
        for( int i = 0 ; i < size1 ; i++){
            arr1[i] = arr[l+i];
        }
        for( int j = 0 ; j < size2 ; j++){
            arr2[j] = arr[m+1+j];
        }

        //Merge arrays
        int firstArrPointer = 0, secondArrPointer = 0;
        int subArrPointer = l;

        while( firstArrPointer < size1 && secondArrPointer < size2){
            if(arr1[firstArrPointer] <= arr2[secondArrPointer]){
                arr[subArrPointer] = arr1[firstArrPointer];
                firstArrPointer++;
            }
            else{
                arr[subArrPointer] = arr2[secondArrPointer];
                secondArrPointer++;
            }
            subArrPointer++;
        }

        //copy remaining elements of first and second array
        while( firstArrPointer < size1 ){
            arr[subArrPointer] = arr1[firstArrPointer];
            firstArrPointer++;
            subArrPointer++;
        }
        while( secondArrPointer < size2 ){
            arr[subArrPointer] = arr2[secondArrPointer];
            secondArrPointer++;
            subArrPointer++;
        }
            
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
    //Call mergeSort from here 
        if(l < r){
            int mid = l+(r-l)/2; //find mid

            sort(arr, l, mid); // sort first half
            sort(arr, mid+1, r); // sort second half

            merge(arr, l, mid, r); // merge the sorted arrays
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