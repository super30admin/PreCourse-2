//Time complexity o(nlog(n))
//Space complexity o(n)
class MergeSort
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here

            int a[]=new int[r-l+1];
            int i=0;
            int p=l;
            int q=m+1;
            while(p<=m&&q<=r){
                a[i++]=arr[p]<arr[q]?arr[p++]:arr[q++];
            }
        while(p<=m){
            a[i++]=arr[p++];
        }
        while(q<=r){
            a[i++]=arr[q++];
        }

            for(int j=l;j-l<a.length;j++){
                arr[j]=a[j-l];
            }


    } 
  
    // Main function that sorts arr[l..r] using 
    // merge()
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here
        if(l<r){
            int mid=l+(r-l)/2;
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