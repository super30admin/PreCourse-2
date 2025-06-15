// Time Complexity -> O(n log n) as merge sort always divides the array amd then merges the sorted halves
// Space Complexity -> O(n) as at last we took temp array to store the mergings
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No
// Your code here along with comments explaining your approach
// So forMerge sort we use divide and merge strategy
// In Sort() function we use a recursion where we recursively divide the array into two halves (from l to mid) and (from mid+1 to r). We do this until we are left with single element where further division is not possible
// Later we use merge(): that merges two sorted subarrays using two pointers (Left_ptr and Right_ptr) and one temp arraylist
// After sorted and merging is done we copy the final sorted elements from temp array to the original array arr.




import java.util.*;

class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here
       // Main function that sorts arr[l..r] using 
       // merge() 

       ArrayList<Integer> temp = new ArrayList<>();
       int left_ptr = l;
       int right_ptr = m+1;
       int i;
       while(left_ptr<=m && right_ptr<=r){
            if(arr[left_ptr]<=arr[right_ptr])
            {
                temp.add(arr[left_ptr]);
                left_ptr++;
            }
            else{
                temp.add(arr[right_ptr]);
                right_ptr++;
            }

        }

        while(left_ptr<=m){
            temp.add(arr[left_ptr]);
            left_ptr++;
        }

        while(right_ptr<=r){
            temp.add(arr[right_ptr]);
            right_ptr++;
        }

        for(i=l;i<=r;i++)
        arr[i] = temp.get(i-l);
       

    }
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 

        if(l>=r) return;
        int mid = (l+r)/2;
        sort(arr, l, mid);
        sort(arr, mid+1, r);
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