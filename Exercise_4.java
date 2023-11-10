// Time Complexity : O(nlog n)
// Space Complexity : O(n)

import java.util.*;
class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
    //    store the sorted array after merging the sorted arrays
       ArrayList<Integer> finalList = new ArrayList<>();

       int i =l;
       int j = m+1;

       while(i <= m && j <= r){    // compare the element from the left sub array with right sub array and insert it to the list 
        if(arr[i]<arr[j]){
            finalList.add(arr[i]);
            i++;
        } else {
            finalList.add(arr[j]);
            j++;
        }

       }

       while(i<=m) {    // if the right sub array is completely inserted, append the remaining elements of left sub array to the list
            finalList.add(arr[i]);
            i++;
        } 

        while(j<=r){    // if the left sub array is completely inserted, append the remaining elements of right sub array to the list
            finalList.add(arr[j]);
            j++;
        }

    //    reassigning the final values to the original array
        for(int k=l;k<=r;k++){
            arr[k] = (int) finalList.get(k-l);
        }
       
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 
        if(l<r){
            int m = (l+r)/2;    // the mid element is calculated
            sort(arr, l, m); // left half of the array is sorted
            sort(arr, m+1, r); // right half of the array is sorted

            merge(arr, l, m, r); // left and right sub arrays are merged into 1 array
        } else {
            return;
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