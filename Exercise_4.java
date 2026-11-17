class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
		int l1=m-l+1;
		int l2=r-m;
		int[] arr1=new int[l1];
		int[] arr2=new int[l2];
		for(int i=l;i<=m;i++){
			arr1[i-l]=arr[i];
		}
		for(int j=0;j<l2;j++){
			arr2[j]=arr[m+1+j];
		}
		int counter1=0;
		int counter2=0;
		int pos=l;
		while(counter1<l1 && counter2<l2){
			if(arr1[counter1]<arr2[counter2]){
				arr[pos]=arr1[counter1];
				pos++;
				counter1++;
			}
		
			else{
				arr[pos]=arr2[counter2];
				pos++;
				counter2++;
			}
		}
		while(counter1<l1){
			arr[pos]=arr1[counter1];
			pos++;
			counter1++;
		}
		while(counter2<l2){
			arr[pos]=arr2[counter2];
			pos++;
			counter2++;
		}
		
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 
		if(l<r){
			int m=l+(r-l)/2;
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
