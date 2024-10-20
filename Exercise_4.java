// Time Complexity: O(n log n)
// Space Complexity: O(n)
class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
        int arr_1_size = m - l + 1;
	int arr_2_size = r - m;

	int arr_1[] = new int[arr_1_size];
	int arr_2[] = new int[arr_2_size];

	for(int i = 0; i < arr_1_size; i++) {
	    arr_1[i] = arr[l + i];
	}
	for(int j=0; j < arr_2_size; j++) {
	    arr_2[j] = arr[m + 1 + j];
	}
	int i = 0, j = 0;
	int k = l;
	while (i < arr_1_size && j < arr_2_size) {
	    if(arr_1[i] <= arr_2[j]) {
		arr[k] = arr_1[i];
		i++;
	    } else {
		arr[k] = arr_2[j];
		j++;
	    }
	    k++;
	}
	while(i < arr_1_size) {
	    arr[k] = arr_1[i];
	    i++;
	    k++;
	}
	while(j < arr_2_size) {
	    arr[k] = arr_2[j];
	    j++;
	    k++;
	}
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here
	if (l < r) {
	    int m = (l + r)/2;
	    sort(arr, l, m);
	    sort(arr, m+1, r);
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
