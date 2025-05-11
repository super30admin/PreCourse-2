import java.util.ArrayList;

class MergeSort
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here
        //Your code here
        int i = l; int j = m+1;
        ArrayList<Integer> temp = new ArrayList<>();
        //merging both left and right array by comparing elements
        while(i<=m && j<=r){
            if(arr[i] <= arr[j]){
                temp.add(arr[i]);
                i++;
            }
            else{
                temp.add(arr[j]);
                j++;
            }
        }
        //left part remaining elements
        while(i<=m)
        {
            temp.add(arr[i]);
            i++;
        }
        //right part remaining elements
        while(j<=r)
        {
            temp.add(arr[j]);
            j++;
        }
        //putting elements in original array
        for(i = 0;i<temp.size();i++)
        {
            arr[l+i] = temp.get(i);
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
            int mid = l + ((r-l)/2);
            //left half
            sort(arr, l, mid);
            //right half
            sort(arr, mid+1, r);
            //finally merging both of the halves while sorting them
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