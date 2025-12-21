// Time Complexity : Average case - O(n logn),
// Space Complexity : Additional array created in the recursive call which can have max "n" elements, O(n)
// Did this code successfully run on Leetcode :
// Yes
// Any problem you faced while coding this : No

class MergeSort
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {   int arrALen = m-l+1;
        int arrBLen = r-m;
        int[] arrA = new int[arrALen];
        int[] arrB = new int[arrBLen];

        // copy the array into 2 sub arrays
        int startIndex = l;
        for(int i = 0; i < arrALen; i++){
            arrA[i] = arr[startIndex++];
        }

        startIndex = m+1;
        for(int i = 0; i < arrBLen; i++){
            arrB[i] = arr[startIndex++];
        }
        int i = 0, j = 0, index = l;

        // compare the sorted array and combine
        while(i < arrALen && j < arrBLen){
            if(arrA[i] <= arrB[j]){
                arr[index++] = arrA[i++];
            }else{
                arr[index++] = arrB[j++];
            }
        }

        while(i < arrALen){
            arr[index++] = arrA[i++];
        }

        while(j < arrBLen){
            arr[index++] = arrB[j++];
        }

    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	    if(l>=r) return;
        int mid = (l+r)/2;
        // Divide the array from the middle
        sort(arr, l, mid);
        sort(arr, mid+1, r);

        // merge the array comparing sub arrays
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
        int arr[] = {12, 11, 13, 5, 6, 7}; 
  
        System.out.println("Given Array"); 
        printArray(arr); 
  
        MergeSort ob = new MergeSort(); 
        ob.sort(arr, 0, arr.length-1); 
  
        System.out.println("\nSorted array"); 
        printArray(arr); 
    } 
} 