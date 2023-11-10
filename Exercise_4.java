/*
 Time Complexity: O(nlog(n))->n for merge() and log(n) for recursive calls
 Space Complexity:O(n)->since we have declared temp arrays of size n
 */

class MergeSort
{ 
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r]
    void merge(int arr[], int l, int m, int r)
    {  
       //Your code here
        //first half size
        int size1=m-l+1;
        //second half size
        int size2=r-m;
        //divide elements into 2 unsorted arrays
        int[] left=new int[size1];
        int[] right=new int[size2];

        for(int i=0;i<size1;i++ )
        {
            left[i]=arr[l+i];
        }
        for(int j=0;j<size2;j++)
        {
            right[j]=arr[m+1+j];
        }

        int i=0;
        int j=0;
        int k=l;

        //compare elements from 2 arrays and put them into new array
        while(i<size1 && j<size2)
        {
            if(left[i]<=right[j])
            {
                arr[k]=left[i];
                i++;
            }
            else
            {
                arr[k]=right[j];
                j++;
            }
            k++;
        }
        //if left subarray contain extra elements , put them at last
        while(i<size1)
        {
            arr[k]=left[i];
            i++;
            k++;
        }
        //if right subarray contain extra elements , put them at last
        while(j<size2)
        {
            arr[k]=right[j];
            j++;
            k++;
        }

    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        if(l<r) {
            //find mid to divide array into 2 halves
            int mid =l+(r-l) / 2;
            //Call mergeSort from here
            //call merge sort on first half
            sort(arr,l,mid);
            //call merge sort on second half
            sort(arr,mid+1,r);
            //merge 2 sorted halves to get sorted array
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
        System.out.println("After solution:");
        ob.sort(arr, 0, arr.length-1); 
  
        System.out.println("\nSorted array"); 
        printArray(arr); 
    } 
} 