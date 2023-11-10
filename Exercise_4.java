class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
        int temp[] = new int[r-l+1];
        int ptr1=l,ptr2=m+1;
        int i=0;
        while(ptr1<=m && ptr2<=r)
        {
            if(arr[ptr1]<=arr[ptr2])
            {
                temp[i]=arr[ptr1];
                ptr1++;
            }
            else
            {
                temp[i]=arr[ptr2];
                ptr2++;
            }
            i++;
        }
        if(ptr1<=m)
        {
            while(ptr1<=m)
            {
                temp[i++]=arr[ptr1++];
            }
        }
        if(ptr2<=r)
        {
            while(ptr2<=r)
            {
                temp[i++]=arr[ptr2++];
            }
        }
        int j;
        for(i=0,j=l;i<temp.length;i++,j++)
        {
            arr[j]=temp[i];
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
        int mid=l+(r-l)/2;
        sort(arr,l,mid);
        sort(arr,mid+1,r);
        merge(arr,l,mid,r);
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