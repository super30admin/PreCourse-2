Time Complexity - O(nlogn)
Space Complexity - O(n)

class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
      int n1 = m - l + 1;
        int n2 = r - m;
		int first[] = new int[n1];
        int second[] = new int[n2];
		for (int i = 0; i < n1; ++i)
            first[i] = arr[l + i];
        for (int j = 0; j < n2; ++j)
            second[j] = arr[m + 1 + j];
		 int i = 0, j = 0;
		  int k = l;
        while (i < n1 && j < n2) {
            if (first[i] <= second[j]) {
                arr[k] = first[i];
                i++;
            }
            else {
                arr[k] = second[j];
                j++;
            }
            k++;
        }
		 while (i < n1) {
            arr[k] = first[i];
            i++;
            k++;
        }
		while (j < n2) {
            arr[k] = second[j];
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
           
            int m = l + (r - l) / 2;
            sort(arr, l, m);
            sort(arr, m + 1, r);
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