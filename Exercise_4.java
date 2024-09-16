/*class MergeSort 
{ 
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m].
    // Second subarray is arr[m+1..r].
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
    	int index=l;
    	int first=m-l+1;
    	int second=r-m;
    	
    	int[] firsthalf= new int[first];
    	int[] secondhalf= new int[second];
    	
    	
    	for(int i=0;i<firsthalf.length;i++) {
    		firsthalf[i]=arr[l+i];    		
    	}
    	
    	for(int j=0;j<secondhalf.length;j++) {    		
    		secondhalf[j]=arr[m+1+j];    		
    	}
    	
    	int i=0,j=0;
    	
    	while(i<first && j< second) {
    		if(firsthalf[i]<secondhalf[j]) {
    			arr[index]=firsthalf[i];
    			i++;
    		}else {
    			arr[index]=secondhalf[j];
    			j++;
    		}
    		index++;
    	}
    	
    	while(i<firsthalf.length) {
    		arr[index]=firsthalf[i];
    		i++;
    		index++;    		
    	}
    	
    	while(j<secondhalf.length) {
    		arr[index]=secondhalf[j];
    		j++;
    		index++;    		
    	}
    } 

    
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here +++++
    	if(l<r) {
    	
    	int mid= (l+r)/2;
    	sort(arr,l,mid);
    	sort(arr,mid+1,r);	  
    	
    	
    	merge(arr,l,mid,r);
    	}
    	
    } 
  
    /* A utility function to print array of size n */
   /* static void printArray(int arr[]) 
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
} */