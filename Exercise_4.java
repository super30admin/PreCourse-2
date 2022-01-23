//time complexity = O(nlogn)
//space complexity = O(n)

class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
        int k = 0;
		int i = l;
		int j = m + 1;
		int t[] = new int[r - l + 1];

		while (i <= m && j <= r)
			// compare a[i] with a[j] and then assign value to t[k].
			//Last increment value of k(k++)
			t[k++] = arr[i] < arr[j] ? arr[i++] : arr[j++];

			while (i <= m)
				t[k++] = arr[i++];

			while (j <= r)
				t[k++] = arr[j++];

			System.arraycopy(t, 0, arr, l, t.length);
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here
        if(l < r)
		{
			int mid = (l + r) / 2;
			System.out.println("mid " + mid);
			sort(arr, l, mid);
			sort(arr, mid + 1, r);
			merge(arr, l, mid, r);
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