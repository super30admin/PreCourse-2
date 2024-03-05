// Time Complexity :O(N)
// Space Complexity: O(N)

class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
        int leftsize = m -l +1;
        int rightsize = r-m;

        int[] leftarray = new int[leftsize];
        int[] rightarray = new int[rightsize];

       //Your code here  
       for(int i=0 ; i<leftsize ; i++)
       {
            leftarray[i] = arr[l+i];
       }

       for(int j=0 ; j<rightsize; j++)
       {
            rightarray[j] = arr[m+1+j];
       }

       int i=0, j=0, k=l;

       while(i < leftsize && j < rightsize)
       {
            if(leftarray[i] <= rightarray[j])
            {
                arr[k] = leftarray[i];
                i++;
            }
            else
            {
                arr[k] = rightarray[j];
                j++;
            }
            k++;
        }

        // loop thru and add the remaining elements in the left array to output array.
        while( i < leftsize)
        {
            arr[k] = leftarray[i];
            i++;
            k++;
        }

        //loop thru and add the remaining elements in the right array to the output array.
        while( j < rightsize)
        {
            arr[k] = rightarray[j];
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
            int mid = l+(r-l)/2;

            sort(arr, l , mid);
            sort(arr, mid+1, r);

            merge(arr, l, mid, r);
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