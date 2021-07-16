class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
        //int[] tempArr = new int[r-l+1];
        int [] tempArr = new int[r-l+1];

        int index1 = l;
        int index2= m+1;

        int index =0;

        while(index1<=l && index2<=r)
        {
            if(arr[index1]<=arr[index2])
            {
                tempArr[index++] = arr[index1++];
            } 
            else
            {
                tempArr[index++] = arr[index2++];

            }
        }
        // for remaining elements in first list if they exist

        while(index1<=m)
        {
            tempArr[index++]=arr[index1++];

        }

        // for remaining elements in second list if they exist

        while(index2<=r)
        {
            tempArr[index++]=arr[index2++];

        }

        index=0;
        for(int i=l;i<=r;i++)
        {
            arr[i]= tempArr[index++];
        }




       //Your code here  
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
        if(l<r)
        {
            int mid = l+(r-l)/2;
            sort(arr,l,mid);
            sort(arr,mid+1,r);
            merge(arr,l,mid,r);

        }
        //merge()


	//Write your code here
        //Call mergeSort from here 
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