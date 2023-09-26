class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here

        int tempArr1[] = new int[m+1-l];
        int tempArr2[] = new int[r-m];

        for (int i = 0; i < m+1-l; i++)
            tempArr1[i] = arr[l + i];
        for (int i = 0; i < r-m; i++)
            tempArr2[i] = arr[m + 1 + i];

        int i=0 ,j = 0;
        int mainArrPtr = l;
        while (i < m+1-l && j < r-m) {
            if (tempArr1[i] <= tempArr2[j]) {
                arr[mainArrPtr] = tempArr1[i];
                i++;
            }
            else {
                arr[mainArrPtr] = tempArr2[j];
                j++;
            }
            mainArrPtr++;
        }

        while (i < m+1-l) {
            arr[mainArrPtr] = tempArr1[i];
            i++;
            mainArrPtr++;
        }

        while (j < r-m) {
            arr[mainArrPtr] = tempArr2[j];
            j++;
            mainArrPtr++;
        }

    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here
        if(l<r){
            int mid = (l+r)/2;

            sort(arr, l, mid);
            sort(arr, mid+1, r);
            merge(arr,l,mid,r);
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
        int arr[] = {12, 11, 13, 5, 6, 7,22,34,54,0,12,5};
  
        System.out.println("Given Array"); 
        printArray(arr); 
  
        MergeSort ob = new MergeSort(); 
        ob.sort(arr, 0, arr.length-1); 
  
        System.out.println("\nSorted array"); 
        printArray(arr); 
    } 
} 