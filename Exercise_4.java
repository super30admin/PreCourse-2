// Time Complexity : O(n log(n)) -> I think it should be o(n)
// Space Complexity : O(n)
// Did this code successfully run on Leetcode :
// Any problem you faced while coding this : I referred few videos to so this 
class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
       int[] merged = new int[r-l+1];
       int idx1=l;       //pointer to first sub array
       int idx2=m+1;     //pointer to second sub array
       int k=0;             
       while(idx1<=m && idx2 <=r){
        if(arr[idx1] <= arr[idx2] ){          
            merged[k] = arr[idx1];
            k++;
            idx1++;
        }
        else{
            merged[k] = arr[idx2];
            k++;
            idx2++;
        }
       }
       while(idx1<=m){             //loop that will copy all the remaining any elements in the same order as they will be already sorted
        merged[k] = arr[idx1];
            k++;
            idx1++;
       }
       while(idx2<=r){     //loop that will copy all the remaining any elements in the same order as they will be already sorted
        merged[k] = arr[idx2];
            k++;
            idx2++;
       }

       for(int i=0, j=l;i<merged.length;i++,j++ ){        //copying the merged array into original array
            arr[j]=merged[i];
       }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
        if(l>=r){
            return;
        }
        int mid = l+(r-l)/2;

        
        sort(arr,l,mid);
        sort(arr,mid+1,r);
        merge(arr,l,mid,r);
	//Write your code here
        //Call mergeSort from here 
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