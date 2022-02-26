/*
Time Complexity : O(N * Log N)
Space Complexity : O(N) extra array
Did this code successfully run on Leetcode : yes
Any problem you faced while coding this : No

*/

class MergeSort 
{ 
    void merge(int arr[], int l, int m, int r) 
    {  
       
       int i=l;
       int ind=0;
       int j=m+1;
       int len = arr.length ;
       int[] arr1 = new int[len];

       while(i<=l && j<=r){
           if(arr[i]<arr[j]){
               arr1[ind] = arr[i];
               i++;
           }
           else{
               arr1[ind] = arr[j];
               j++;
           }
            ind++;
       }
        if(i>m){
            while(j<=r){
                arr1[ind] = arr[j];
               j++;
               ind++;
            }
        }
        if(j>r){
            while(i<=m){
                arr1[ind] = arr[i];
               i++;
               ind++;
            }
        }

        for(int k=l;k<ind;k++){
            arr[l]=arr1[k];
            l++;
        }
    } 

    void sort(int arr[], int l, int r) 
    { 
        if(l<r){
            int m = (l+r)/2;
            sort(arr,l,m);
            sort(arr,m+1,r);
            merge(arr,l,m,r);
        }

    } 

    static void printArray(int arr[]) 
    { 
        int n = arr.length; 
        for (int i=0; i<n; ++i) 
        System.out.print(arr[i] + " "); 
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