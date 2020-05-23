// Time Complexity :O(n^2) 
// Space Complexity : O(n)  n-length of the array.
// Did this code successfully run on Leetcode : N/A
// Any problem you faced while coding this :Recursively sorting
class QuickSort 
{ 
    /* This function takes last element as pivot, 
       places the pivot element at its correct 
       position in sorted array, and places all 
       smaller (smaller than pivot) to left of 
       pivot and all greater elements to right 
       of pivot */
    void swap(int arr[],int i,int j){
        //code to swap  
		int temp=arr[i];
		arr[i]=arr[j];
		arr[j]=temp;
    }
    
    int partition(int arr[], int low, int high) 
    { 
		//Write code here for Partition and Swap 
		for(int i=low;i<=high;i++)
		{
			if(arr[i]<arr[high]) //If pivot is greater than the number then we swap and increment the low pointer
			{
			swap(arr,i,low);
			low++;
			}
		} 
		swap(arr,low,high);// Swap the pivot element to it correct position
	return low; // return the pivot position

    } 
    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    void sort(int arr[], int low, int high) 
    {  
        // Recursively sort elements before 
        // partition and after partition 
		
		if(low<high)
		{
		int pivot=partition(arr,low,high);// Getting the pivot position
			sort(arr,low,pivot-1); // Sorting to the left of pivot
			sort(arr,pivot+1,high);// Sorting to the right of pivot
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
