// Time Complexity : O (n log n)
// Space Complexity : O (n log n)
// Did this code successfully run on Leetcode : Ran it on VS Code. 
// Any problem you faced while coding this : No

// Your code here along with comments explaining your approach
// Check if l < r and calculate the midpoint index and recursively sort the left and right arrays to the 
// midpoint index. Finally merge the left and right arrays. To merge the array first construct the left and
// right arrays using the lower,midpoint and right indexes. Take two pointers i and j to iterate the left and
// right arrays respectively if value in left is less than value in right then update the value in original array
// with the left otherwise use right array value to update the original array. If either i or j reaches the end
// of the respective arrays then use the other array to fill in the original array.


class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here 
       int[] left = new int[m-l+1];
       for(int i=0;i<=m-l;i++){
           left[i]=arr[i+l];
       }
       int[] right = new int [r-m];
       for(int i=0;i<r-m;i++){
        right[i]=arr[i+m+1];
       }

       for(int i=0,j=0,k=l; k<r-l+1;k++){
            if( i<left.length && j<right.length && left[i]>right[j] ){
                arr[k]=right[j];
                j++;
            }
            else if (  i<left.length && j<right.length && left[i]<right[j] ){
                arr[k]=left[i];
                i++;
            }
            else if(i==left.length && j<right.length){
                arr[k]=right[j];
                j++;
            }
            else if(j==right.length && i<left.length){
                arr[k]=left[i];
                i++;
            }
       }
       
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	    //Write your code here
        //Call mergeSort from here 
        if(l<r){
            int m = Math.floorDiv(l+r, 2);
            sort(arr,l,m);
            sort(arr,m+1,r);
            merge(arr, l, m, r);
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