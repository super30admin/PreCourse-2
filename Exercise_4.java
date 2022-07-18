class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here

        int l1 = m-l+1;
        int r1 = r-m;

        int[] l_arr = new int[l1];
        int[] r_arr = new int[r1];

        for(int i=0; i<l1; i++)
            l_arr[i] = arr[l+i];
        for(int i=0; i<r1; i++)
            r_arr[i] = arr[m+i+1];

        int i = 0, j = 0;
        int k = l;

        while(i<l1 && j<r1){
            if(l_arr[i]<=r_arr[j]){
                arr[k] = l_arr[i];
                i++;
            } else {
                arr[k] = r_arr[j];
                j++;
            }
            k++;
        }

        while(i<l1){
            arr[k] = l_arr[i];
            i++;
            k++;
        }

        while(j<r1){
            arr[k] = r_arr[j];
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

            sort(arr,l,mid);
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