class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {
        System.out.println(l+ " "+m+" "+r);
        int i = l;
        int j = m;
        int k = 0;
        //Your code here
        while(i<=l && j<=m) {
            if(arr[i] < arr[j]) {
                System.out.println(arr[i]);
                arr[k] = arr[i];
                i++;
                k++;
            } else if(arr[j] < arr[i]) {
                arr[k] = arr[j];
                j++;
                k++;
            } else {
                arr[k] = arr[i];
                i++;
                j++;
                k++;
            }

        }
        while(i<=l && k<=r) {
            arr[k] = arr[i];
            i++;
            k++;
        }
        while(j<=m && k<=r) {
            arr[k] = arr[j];
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
        if(l<r) {
            int m = (int)Math.floor((l+r)/2);
            sort(arr, l, m);
            sort(arr, m+1, r);
            merge(arr, l, m, r);
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