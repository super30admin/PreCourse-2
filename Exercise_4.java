// Time Complexity : O(NlogN)
// Space Complexity : O(N) as during merge everytime the array was created
// Did this code successfully run on Leetcode : Ran it locally on IDE and works
                          //with multiple test cases
// Any problem you faced while coding this : No

class MergeSort
{
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    /*
      followed the approach metnitoned through out except stopped sorting when
      breaking the array and size becomes 2 then just swapped the positions,
      instead of sending them to merge.
    */
    void merge(int arr[], int l, int m, int r)
    {
       //Your code here
       int len = r - l + 1;
       int[] temp_merged = new int[len];

       for(int i = l; i <= r; i++)
       {
         temp_merged[i-l] = arr[i];
       }

       int first = l;
       int second = m + 1;
       int count = l;

       while(first <= m && second <= r)
       {
         if(temp_merged[first - l] <= temp_merged[second - l])
         {
           arr[count++] = temp_merged[first - l];
           first++;
         }
         else
         {
           arr[count++] = temp_merged[second - l];
           second++;
         }
       }

       while(first <= m)
       {
    	   arr[count++] = temp_merged[first - l];
         first++;
       }

       while(second <= r)
       {
    	   arr[count++] = temp_merged[second - l];
         second++;
       }

       return;
    }

    // Main function that sorts arr[l..r] using
    // merge()
    void sort(int arr[], int l, int r)
    {
      //Write your code here
      //Call mergeSort from here
      if(r - l == 1)
      {
        if(arr[r] < arr[l]){
          this.swap(arr,l ,r);
        }
        return;
      }

      if(r == l) return;

      int m = l + (r - l)/2;

      this.sort(arr,l,m);
      this.sort(arr,m+1,r);

      this.merge(arr, l, m, r);
    }

    void swap(int arr[], l , r)
    {
      int temp = arr[l];
      arr[l] = arr[r];
      arr[r] = temp;
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
