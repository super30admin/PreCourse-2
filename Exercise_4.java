class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int a[], int l, int m, int r)
    {  
       //Your code here
        int n1, n2, i, j, k;
        n1 = m - l + 1;
        n2 = r - m;

        int left[] = new int[n1];
        int right[] = new int[n2];

        for(i = 0; i < n1; i++) {
            left[i] = a[l + i];
        }
        for(i = 0; i < n2; i++) {
            right[i] = a[m + i + 1];
        }

        i = 0;
        j = 0;
        k = l;
        while(i < n1 && j < n2) {
            if(left[i] < right[j]) {
                a[k] = left[i];
                i++;
            } else {
                a[k] = right[j];
                j++;
            }
            k++;
        }
        while(i < n1) {
            a[k] = left[i];
            i++;
            k++;
        }
        while(j < n2) {
            a[k] = right[j];
            j++;
            k++;
        }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int a[], int l, int r)
    { 
	    //Write your code here
        //Call mergeSort from here
        if(l >= r) return;
        int m = l + (r - l) / 2;
        sort(a, l, m);
        sort(a, m + 1, r);
        merge(a, l, m, r);
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