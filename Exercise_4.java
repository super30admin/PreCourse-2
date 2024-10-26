//Time complexity:nlog(n)
//while loop takes o(n)
// sort function takes log(n) step


class MergeSort
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here
       int merged[]  =new int[r-l+1];
       int id1= l;
       int id2 = m+1;
       int x=0;

       while (id1 <= m && id2 <= r)
       {
           if (arr[id1] <= arr[id2])
           {
               merged[x++]=arr[id1++];
           }
           else {
               merged[x++]=arr[id2++];
           }
       }
       while (id1 <= m)
       {
           merged[x++]=arr[id1++];
       }
       while (id2 <= r)
       {
           merged[x++]=arr[id2++];
       }

    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here
        if (l>=r)
        {return;}
        int mid= l +(r-l)/2;
        sort(arr, l, mid);
        sort(arr, mid+1, r);
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
        int arr[] = {12, 11, 13, 5, 6, 7}; 
  
        System.out.println("Given Array"); 
        printArray(arr); 
  
        MergeSort ob = new MergeSort(); 
        ob.sort(arr, 0, arr.length-1); 
  
        System.out.println("\nSorted array"); 
        printArray(arr); 
    } 
} 