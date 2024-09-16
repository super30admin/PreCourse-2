// Time Complexity :O(nlogn)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : Problem not on leetcode but working on eclipse
// Any problem you faced while coding this : Did not know the concept
// Your code here along with comments explaining your approach

class QuickSort 
{ 
    /* This function takes last element as pivot, 
       places the pivot element at its correct 
       position in sorted array, and places all 
       smaller (smaller than pivot) to left of 
       pivot and all greater elements to right 
       of pivot */
    void swap(int arr[],int i,int j){
        //Your code here   
        int temp = arr[i]; // creating temp and storing ith element in it
        arr[i]= arr[j]; // storing jth element at i position
        arr[j] = temp; // storing at jth position the temp value that stores initial value at i
    }
    
    int partition(int arr[], int low, int high) 
    { 

       //Write code here for Partition and Swap 
       int pivot = high; // taking pivot as last element 
       int small = low; // taking the small variable as first element
      
       for(int i = low; i <= high; i++) // looping through the array
       {
           if(arr[i]<arr[pivot]) // if the current element is smaller than the element at pivot
           {
            swap(arr, i, small); // swap the ith and element at small index to place values smaller than the pivot to the left of pivot
               small++; // increment small
           }
       }
       swap(arr, pivot, small); // after the loop is completed, place the pivot at its right position by swapping pivot element and element at small index
     

       return small; // return small i.e index at which the pivot is present now

    } 
    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    void sort(int arr[], int low, int high) 
    {  
            // Recursively sort elements before 
            // partition and after partition 
            if(low<high) // for an array, lower pointer should not cross the upper one
            {
            int part = partition(arr, low, high); // finds the partition
            sort(arr, low, part -1); // calls the sort function for new lower partition
            sort(arr, part+1, high); // calls the sort function for new upper partition
            }

    } 
  
    /* A utility function to print array of size n */
    static void printArray(int arr[]) 
    { 
        int n = arr.length; 
        for (int i=0; i<n; ++i) 
            System.out.print(arr[i]+" "); 
        System.out.println(); 
    } 
  
    // Driver program 
    public static void main(String args[]) 
    { 
        int arr[] = {10, 7, 8, 9, 1, 5}; 
        int n = arr.length; 
  
        QuickSort ob = new QuickSort(); 
        ob.sort(arr, 0, n-1); 
  
        System.out.println("sorted array"); 
        printArray(arr); 
    } 
} 
