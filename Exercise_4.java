// Time Complexity : O(nlogn)
// Space Complexity : O(n)
// Did this code successfully run on Leetcode : yes
// Any problem you faced while coding this : no
public class Exercise_4
{
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    void merge(int arr[], int l, int m, int r)
    {
       //Your code here
       int[] left = new int[m-l+1];
       int[] right = new int[r-m];

       for(int i=0; i<m-l+1; i++)
       {
         left[i] = arr[l+i];
       }

       for(int i=0; i<r-m; i++)
       {
         right[i] = arr[m+1+i];
       }

       int i=0, j=0, k=l;

       while(i<left.length && j<right.length)
       {
         if(left[i] <= right[j])
         {
           arr[k] = left[i];
           i++;
         }
        else
        {
          arr[k] = right[j];
          j++;
        }
          k++;
       }

       while(i<left.length)
       {
         arr[k] = left[i];
         k++;
         i++;
       }

       while(j<right.length)
       {
         arr[k] = right[j];
         k++;
         j++;
       }
    }

    // Main function that sorts arr[l..r] using
    // merge()
    void sort(int arr[], int l, int r)
    {
	      //Write your code here
        //Call mergeSort from here
        if(l<r)
        {
          int mid = l + (r-l)/2;

          sort(arr, l, mid);
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

        Exercise_4 ob = new Exercise_4();
        ob.sort(arr, 0, arr.length-1);

        System.out.println("\nSorted array");
        printArray(arr);
    }
}
