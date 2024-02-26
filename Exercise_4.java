// Time Complexity : O(logn)
// Space Complexity : O(n)
class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
       int lSize = m+1-l;
        int rSize = r-m;

       //Your code here  
       int lArray[] = new int[lSize];
       int rArray[] = new int[rSize];

       for(int i=0; i<lSize; i++)
       {
           lArray[i] = arr[i+l];    
       }
       for(int i=0; i<rSize; i++)
       {
           rArray[i] = arr[i+m+1];   
       }

       int i=0, j=0, k=l;   

       while(i<lSize && j<rSize)
       {
           if(lArray[i] <= rArray[j])    
           {
               arr[k] = lArray[i];   
               i++;
           }
           else
           {
               arr[k] = rArray[j];  
               j++;
           }
           k++;
       }

       while(i<lSize)   
       {
           arr[k] = lArray[i];
           i++;
           k++;
       }
       while(j<rSize)  
       {
           arr[k] = rArray[j];
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
        if(l < r)
        {
            int m = l+(r-l)/2; 

            sort(arr, l, m);   
            sort(arr, m+1, r);

            merge(arr, l, m, r);
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