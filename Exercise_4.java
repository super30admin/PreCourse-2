// Time Complexity : O(n*log(n))
// Space Complexity :using extra array O(n)
// Did this code successfully run on Leetcode : yes
// Any problem you faced while coding this : no
class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
       int i=l;
       int ind=0;
       int j=m+1;
       int len = arr.length ;
       int[] tem = new int[len];
       while(i<=l && j<=r){
           if(arr[i]<arr[j]){
               tem[ind] = arr[i];
               i++;
           }
           else{
               tem[ind] = arr[j];
               j++;
           }
            ind++;
       }
        if(i>m){
            while(j<=r){
                tem[ind] = arr[j];
               j++;
               ind++;
            }
        }
        if(j>r){
            while(i<=m){
                tem[ind] = arr[i];
               i++;
               ind++;
            }
        }

        for(int k=l;k<ind;k++){
            arr[l]=tem[k];
            l++;
        }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 
        if(l<r){
            int m = (l+r)/2;
            //System.out.println(l+" "+r+" "+m);
            sort(arr,l,m);
            sort(arr,m+1,r);
            merge(arr,l,m,r);
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