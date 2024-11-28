class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int low, int mid, int high) 
    {  
       //Your code here
		int[] L = new int[min - low + 2];
		
		for (int i = low; i <= min; i++) {
			L[i - low] = list[i];
		}
		L[min - low + 1] = Integer.MAX_VALUE;
		int[] R = new int[high - min + 1];
		
		for (int i = min + 1; i <= high; i++) {
			R[i - min - 1] = list[i];
		}
		
		R[high - min] = Integer.MAX_VALUE;
		
		int i = 0, j = 0;
		
		for (int k = low; k <= high; k++) {
			if (L[i] <= R[j]) {
				list[k] = L[i];
				i++;
			}
			else {
				list[k] = R[j];
				j++;
			}
		} 	   
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int low, int high) 
    { 
		//Write your code here
        //Call mergeSort from here 
		if (low == high)
			return;
		else {
			int mid = (low + high) / 2;
			mergeSort(list, low, mid);
			mergeSort(list, mid + 1, high);
			merge(list, low, mid, high);
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