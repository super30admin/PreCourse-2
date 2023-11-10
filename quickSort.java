//Precourse 2: Exercise 2    --  Implementing Quicksort 
// Time Complexity : O(n^2) because we divided the array into half and kept searching in it. In short we straight away reducing the half part of array
// Space Complexity : O(n) for storing n elements also as this sorting technique is in place.
// Any problem you faced while coding this : no

/*Output
sorted array
1 5 7 8 9 10 
*/
import java.io.*;
public class quickSort {

	/* This function takes last element as pivot, 
    places the pivot element at its correct 
    position in sorted array, and places all 
    smaller (smaller than pivot) to left of 
    pivot and all greater elements to right 
    of pivot */
 void swap(int arr[],int i,int j){
     //Your code here   
	 int temp=arr[i];
	 arr[i]=arr[j];
	 arr[j]=temp;
 }
 
 int partition(int arr[], int low, int high) 
 { 
	//Write code here for Partition and Swap 
	int pivot = arr[high];
	int i = (low - 1);   //initialing 2 pointers i and j for left side and right side pointers from pivot
	  
    for(int j = low; j <= high - 1; j++)
    {
        // If current element is smaller than pivot
        if (arr[j] < pivot) 
        { 
            // Increment index of smaller element
            i++; 
            swap(arr, i, j);
        }
    }
    swap(arr, i + 1, high);
    return (i + 1);
 } 
 
 /* The main function that implements QuickSort() 
   arr[] --> Array to be sorted, 
   low  --> Starting index, 
   high  --> Ending index */
 void sort(int arr[], int low, int high) 
 {  
         // Recursively sort elements before partition and after partition 
	 if (low < high) 
	    {
	        int pindex = partition(arr, low, high);
	  
	        // to sort elements before partition and after partition
	        sort(arr, low, pindex - 1);
	        sort(arr, pindex + 1, high);
	    }
 } 

 /* A utility function to print array of size n */
 static void printArray(int arr[]) 
 { 

     for (int i=0; i<arr.length; ++i) 
         System.out.print(arr[i]+" "); 
     System.out.println(); 
 } 

 // Driver program 
 public static void main(String args[]) 
 { 
     int arr[] = {10, 7, 8, 9, 1, 5}; 
     int n = arr.length; 

     quickSort ob = new quickSort(); 
     ob.sort(arr, 0, n-1); 

     System.out.println("sorted array"); 
     printArray(arr); 
 } 
	
}
