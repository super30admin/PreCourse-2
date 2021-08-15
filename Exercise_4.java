class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
       //int n=arr.length;
       int nL = m-l+1;
       int nR = r-m;
       int[] left = new int[nL];
       int[] right = new int[nR];
    //    for(int i=0;i<=m-1;i++){
    //        left[i]=arr[i];
    //    }
    //    12 11 13 5 6 7
    //             m
    //    for(int j=m;j<=n-1;j++){
    //     right[j-m]=arr[j];
    //    }

    for (int i = 0; i < nL; ++i)
     left[i] = arr[l + i];
    for (int j = 0; j < nR; ++j)
     right[j] = arr[m + 1 + j];

    int k = l;
    int i = 0, j = 0;
    while (i < nL && j < nR) {
        if (left[i] <= right[j]) {

            arr[k] = left[i];
            i++;
            k++;
        } else {
            arr[k] = right[j];
            j++;
            k++;
        }
    }
    while (i < nL) {
        arr[k] = left[i];
        i++;
        k++;
    }
    while (j < nR) {
        arr[k] = right[j];
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
        if(l<r){
            int mid = l + (r-l)/2;
            sort(arr,l,mid-1);
            sort(arr,mid+1,r);
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
        int arr[] = {12, 11, 13, 5, 6, 7}; 
  
        System.out.println("Given Array"); 
        printArray(arr); 
  
        MergeSort ob = new MergeSort(); 
        ob.sort(arr, 0, arr.length-1); 
  
        System.out.println("\nSorted array"); 
        printArray(arr); 
    } 
} 