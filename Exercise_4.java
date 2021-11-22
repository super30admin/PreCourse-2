// Time Complexity :O(logn)
// Space Complexity :O(n) needed for auxiliary array
// Did this code successfully run on Leetcode :Yes
// Any problem you faced while coding this :No
class MergeSort 
{  private static int[] aux;
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {   
        for(int k=l;k<=r;k++){
            aux[k]=arr[k];
        }

       //Your code here
       int i=l;
       int j=m+1;
      for(int k=l;k<=r;k++){
          if(i>m){
            arr[k]=aux[j++];
          } 
          else if(j>r){
            arr[k]=aux[i++];
          }
          else if(aux[i]<=aux[j]){
              arr[k]=aux[i];
              i++;
            }
            else{
                arr[k]=aux[j];
                j++;
            }
          }

        System.out.println("Auxiliary array");
        printArray(aux);

    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
        if(l>=r)
        return;
        else{
            int m =l+((r-l)/2);
            sort(arr,l,m);
            sort(arr,m+1,r);
            merge(arr,l,m,r);
        }
        
        
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
  
        aux=new int[arr.length];
        System.out.println("Given Array"); 
        printArray(arr);
  
        MergeSort ob = new MergeSort();
        ob.sort(arr, 0, arr.length-1);
        System.out.println("\nSorted array"); 
        printArray(arr); 
    } 
} 