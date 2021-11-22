import java.util.Arrays;

class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
    
       //Your code here  
       int larr[]=new int[m-l+1];
       int rarr[]=new int[r-m];

       for(int i=0;i<m-l+1;i++)
       {
           larr[i]=arr[l+i];
       }

       for(int i=0;i<r-m;i++)
       {
           rarr[i]=arr[m+1+i];
       }

       int size1=m-l+1;
       int size2=r-m;
       int minSize=Math.min(size1,size2);
       int k=l;
       int i=0,j=0;
       while(i<size1 && j<size2)
       {
           if(larr[i]<=rarr[j])
           {
             arr[k++]=larr[i++];
           }
           else{
               arr[k++]=rarr[j++];
           }
       }
       while(i<size1)
       {
        arr[k++]=larr[i++];
       }
       while(j<size2)
       {
        arr[k++]=rarr[j++];
       }

    //   System.out.println(Arrays.toString(arr));

    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 
    
        if(l!=r)
        {
            int mid=(l+r)/2;
            sort(arr,l,mid);
            sort(arr,mid+1,r);
            merge(arr,l,mid,r);
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