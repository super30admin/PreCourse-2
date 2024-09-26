//Time Complexity: O(nlogn)
//Space Complexity: O(n logn)
// I am trying to understand the space complexity. Please let me know if space complexity for my code is wrong.


class MergeSort
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[m...r]
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
       int p1 =l, p2=m+1,index=0;
       int[] newArr=new int[r-l+1];
        while (p1<=m && p2<=r)
        {
            if(arr[p1]<=arr[p2])
            {
                newArr[index] = arr[p1++];
                // p1++;
            }
            else
            {
                newArr[index] = arr[p2++];
            }
            index++;
        }
        while(p1<=m)
        {
            newArr[index]=arr[p1++];
            index++;
        }
        while(p2<=r)
        {
            newArr[index]=arr[p2++];
            index++;
        }

       for(int i=0;i<index;i++)
       {
           arr[l]=newArr[i];
           l++;
       }
    } 
  
    // Ma// merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 
        if(l>=r ) // || l==mid || mid+1==r
         return;
        int mid=(l+r)/2;
        sort(arr,l,mid);
        sort(arr,mid+1,r);
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