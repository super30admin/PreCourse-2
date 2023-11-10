// Time Complexity : O(NlogN)
// Space Complexity : O(N)
// Did this code successfully run on Leetcode : ran it successfully on local machine
/* Any problem you faced while coding this : Had to read about the steps of the algo and also about recursion and 
found it bit difficult to calculate the time and space complexity of any algo*/

/*
-- Divide the array into 2 halves based on the middle element
-- Continue dividing till we cannot further divide the array
-- Now start merging and thereby sorting the subarrays by comparing and arranging the elements of the subarray 
*/ 
// Your code here along with comments explaining your approach

class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here
        int leftLen = m-l+1;
        int rightLen = r-(m+1)+1;
        int[] left = new int[leftLen];
        int[] right = new int[rightLen];
        int k = 0;
        for(int i=l;i<=m;++i){
            left[k] = arr[i];
            k++;
        }
        k = 0;
        for(int i=m+1;i<=r;++i){
            right[k] = arr[i];
            k++; 
        }
        int i = 0;
        int j = 0;
        k = l;
        while(i<leftLen && j<rightLen){
            if(left[i]<=right[j]){
                arr[k] = left[i];
                i++;
                k++;
            }else{
                arr[k] = right[j];
                j++;
                k++;
            }
        }
        while(i<leftLen){
            arr[k] = left[i];
            i++;
            k++;
        }
        while(j<rightLen){
            arr[k] = right[j];
            j++;
            k++;
        }
       //

    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here
        if(l>=r){
            return;
        }
        int m = (l + r)/2; 
        sort(arr,l,m);
        sort(arr,m+1,r);
        merge(arr, l, m, r);

   
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
