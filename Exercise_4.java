// Time Complexity : O(nlog n) as the input list is divided n times before mergeing the sorted list.
// Space Complexity : O(n) as extra array is used to store the sub elements from the input lists. Hence not an in place operation.
// Did this code successfully run on Leetcode : yes
// Any problem you faced while coding this : no
// Your code here along with comments explaining your approach
class MergeSort
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here
        int ptr = l;
        int left_size = m-l+1;
        int right_size = r-m;
        int[] left_arr = new int[left_size];
        int[] right_arr = new int[right_size];
        for(int i=0;i<left_size;i++){
            left_arr[i] = arr[l+i];
        }
        for(int j=0;j<right_size;j++){
            right_arr[j] = arr[m+j+1];
        }
        int i=0,j=0;
        while(i<left_size && j<right_size){
            if(left_arr[i] <= right_arr[j]){
                arr[ptr] = left_arr[i];
                ptr++;
                i++;
            }
            else{
                arr[ptr] = right_arr[j];
                ptr++;
                j++;
            }
        }
        while(i<left_size){
            arr[ptr] = left_arr[i];
            ptr++;
            i++;
        }
        while(j<right_size){
            arr[ptr] = right_arr[j];
            ptr++;
            j++;
        }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here
       if(l<r){
           int mid = (r+l)/ 2;
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