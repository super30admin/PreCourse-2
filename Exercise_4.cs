// Time Complexity : O(n log n), where n is the size if the array
// Space Complexity : O(n), where n is the size if the array
class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int[] arr, int l, int m, int r) 
    {  
       //Your code here  
       int s1 = m-l+1, s2 = r-m;
       int[] arr1 =  new int[s1];
       int[] arr2 = new int[s2];

        for(int i=l,j=0; i<=m && j<s1; i++,j++)
            arr1[j] = arr[i];
           
        for(int i=m+1, j=0; i<=r && j<s2; i++, j++)
            arr2[j] = arr[i];

       int p= l, p1 = 0, p2 = 0; 
       while(p1<s1 && p2<s2)
       {
            if(arr1[p1] <= arr2[p2])
                arr[p++] = arr1[p1++];
            else
                arr[p++] = arr2[p2++];
       }
       
       while(p1<s1)
            arr[p++] = arr1[p1++];
        while(p2<s2)
            arr[p++] = arr2[p2++];
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int[] arr, int l, int r) 
    { 
	    //Write your code here
        if(l>=r) return;
        int m = l + (r-l)/2 ;
        //Call mergeSort from here 
        sort(arr, l, m);
        sort(arr, m+1, r);
        merge(arr, l, m, r);
    } 
  
    /* A utility function to print array of size n */
    static void printArray(int[] arr) 
    { 
        int n = arr.Length; 
        for (int i=0; i<n; ++i) 
            Console.Write(arr[i] + " "); 
        Console.WriteLine(); 
    } 
  
    // Driver method 
    public static void main(String[] args) 
    { 
        int[] arr = {12, 11, 13, 5, 6, 7}; 
  
        Console.WriteLine("Given Array"); 
        printArray(arr); 
  
        MergeSort ob = new MergeSort(); 
        ob.sort(arr, 0, arr.Length-1); 
  
        Console.WriteLine("\nSorted array"); 
        printArray(arr); 
    } 
} 