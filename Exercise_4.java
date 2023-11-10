//time complexity: O(n*logn)
class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
       int i=l;
       int j=m+1;
       int []newArray= new int[r+1];
       int k=l;
       while(i<=m+1 && j<=r) {
           newArray[k++]= arr[i]<arr[j]?arr[i++]:arr[j++];
       }
       for(;i<=m;i++) {
           newArray[k++]=arr[i];
       }
       for(;j<=r;j++) {
           newArray[k++]=arr[j];
       }
       for(int x=l;x<=r;x++) {
           arr[x]=newArray[x];
       }  
        
    }
    
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 
        if(l<r) {
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