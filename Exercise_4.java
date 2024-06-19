//Time Complexity: O(nlogn)
//Space Complexity: O(nlogn)
class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
	    int leftArr=new int[m];
		int rightArr=new int[arr.length-m];
		int j=0;
		for(int i=0;i< arr.length;i++){
			if(i<m){
				leftArr[i]=arr[i];
			}else{
				rightArr[j]=arr[i];
				j++;
			}
		}
		
		int i=0; int j=0;
		int k=0;		
		whille(i<leftArr.length && j<rightArr.length){
			if(leftArr[i]<rightArr[j]){
				arr[k]=leftArr[i];
				i++;				
			}
			else{
				arr[k]=rightArr[j];
				j++;
			}
			k++;
		}
		
		while(i<leftArr.length){
			arr[k]=leftArr[i];
			k++;
			i++;
		}
		while(j<rightArr.length){
			arr[k]=rightArr[j];
			j++;
			k++;
		}
	}	
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 	//Write your code here
        //Call mergeSort from here 
		if(l<0 || r>arr.length || l>=r || r-l<=1)
			return;
		int mid=(l+r)/2;		
		sort(arr, l, mid-1);
		sort(arr, mid, r);
		merge(arr, l, mid, r);
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