//Time complexity - O(nLogn)
//Space complexity - O(n)
//Able to submit sorting problem in leetcode with merge sort
public class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
       int n1 = m-l+1;
       int n2 = r-m;
       int a = l;
       int[] L1 = new int[n1];
       int[] L2 = new int[n2];
       for(int i=0;i<n1;i++){
           L1[i] = arr[a];
           a=a+1;
       }
       for(int i=0;i<n2;i++){
           L2[i]=arr[a];
           a=a+1;
       }
       
       int p=0;
       int q=0;
       while(p<n1 && q<n2){
           if(L1[p]<L2[q]){
               arr[l]=L1[p];
               p=p+1;
           }
           else{
               arr[l]=L2[q];
               q=q+1;
           }
           l=l+1;
       }
       while(p<n1){
           arr[l]=L1[p];
           l=l+1;
           p=p+1;
       }
       while(q<n2){
           arr[l]=L2[q];
           l=l+1;
           q=q+1;
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
            sort(arr, l, m);
            sort(arr, m+1, r);
            merge(arr, l, m, r);
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