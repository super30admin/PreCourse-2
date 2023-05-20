class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    // Time Complexity is o(nlog(n))
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here
       int idx1=l;
       int idx2=m+1;
       int[] merged= new int[r-l+1];
       int x=0;
       while(idx1<=m && idx2<=r)
       {
        if(arr[idx1] <= arr[idx2])
        {
            merged[x] = arr[idx1];
            x++;
            idx1++;
        }
        else
        {
            merged[x]=arr[idx2];
            x++;
            idx2++;
        }
       }
       while(idx1<=m)
       {
        merged[x]=arr[idx1];
        idx1++;
        x++;
       }

       while(idx2<=r)
       {
        merged[x]=arr[idx2];
        idx2++;
        x++;
       }
       int j=l;
       for(int i=0;i<merged.length;i++)
       {
          arr[j]=merged[i];
          j++;
       }


    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 
        if(l>=r)
        {
            return;
        }
        int mid = l + (r-l)/2;
        sort(arr, l, mid);
        sort(arr,mid+1,r);
        merge(arr, l, mid, r);

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
        int arr[] = {12, 11, 13, 5, 6, 7,45,6,78,12,36}; 
  
        System.out.println("Given Array"); 
        printArray(arr); 
  
        MergeSort ob = new MergeSort(); 
        ob.sort(arr, 0, arr.length-1); 
  
        System.out.println("\nSorted array"); 
        printArray(arr); 
    } 
} 
