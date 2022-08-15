/*
time complexity O(nlogn)
Space Complexity O(n) for array maintained with the same size as input array

*/
class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
    	int a[]=new int[m-l+1];
    	int b[]=new int[r-m];
    	
    	for(int i=0;i<a.length;i++) {
    		a[i]=arr[l+i];
    	}
    	for(int i=0;i<b.length;i++) {
    		b[i]=arr[m+1+i];
    	}
    	int x=l,y=0,z=0;
    	while(y<(m-l+1)&&z<(r-m)) {
    		if(a[y]<=b[z]) {
    			arr[x]=a[y];
    			y++;
    		}
    		else {
    			arr[x]=b[z];
    			z++;
    		}
    		x++;
    	}
    	while(y<(m-l+1))
    		{
    		arr[x]=a[y];
    		y++;
    		x++;
    		}
    	while(z<(r-m)) {
    		arr[x]=b[z];
    		z++;
    		x++;
    	}
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 
    	if(l==r) {
			return;
		}
		int m=(l+r)/2;
		sort(arr,l,m);
		sort(arr,m+1,r);
		merge(arr,l,m,r);
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