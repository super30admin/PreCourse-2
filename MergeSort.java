import java.util.Arrays;

class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    
    public int[] sort(int arr[],int start,int end)
    {
        if(end-start<=1)
        {
            return Arrays.copyOfRange(arr, start, end);
        }

        int mid = start + (end - start)/2;

        int left[] = sort(arr,start,mid);
        int right[] = sort(arr,mid,end);


        int l = 0,r=0;

        int ans[] = new int[left.length+right.length];
        int k = 0;

        while(l<left.length && r<right.length)
        {
            if(left[l]<=right[r])
            {
                
                ans[k]=left[l];
                k++;
                l++;
            }
            else if(left[l]>right[r])
            {
                ans[k]=right[r];
                k++;
                r++;
            }
        }

        if(l<left.length)
        {
            while(l<left.length)
            {
                ans[k]=left[l];
                k++;
                l++;
            }
        }

        if(r<right.length)
        {
            while(r<right.length)
            {
                ans[k]=right[r];
                k++;
                r++;
            }
        }

        return ans;

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
        int[] ans = ob.sort(arr, 0, arr.length-1); 
  
        System.out.println("\nSorted array"); 
        printArray(ans); 
    } 
} 