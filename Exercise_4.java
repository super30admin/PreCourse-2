/*
Time Complexity: O(nlogn)
Space Complexity: constant throughout, O(n)
Code runs successfully on Leetcode.
I did not face any problems while coding.
*/
class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
	int[] lhalf = new int[m-l+1];
	int[] rhalf = new int[r-m];
	
	for(int i=0; i<lhalf.length; i++){
		lhalf[i] = arr[i + l];
	}

	for(int i=0; i<rhalf.length; i++){
		rhalf[i] = arr[i+m+1];
	}
	
	int k=l;
	int i=0;
	int j=0;
	while(i < lhalf.length && j < rhalf.length){
		if(lhalf[i] <= rhalf[j]){
			arr[k] = lhalf[i];
			i++;
		}else{
			arr[k] = rhalf[j];
			j++;
		}
		k++;
	}
	
	while(i < lhalf.length){
		arr[k] = lhalf[i];
		i++;
		k++;	
	}

	while(j < rhalf.length){
		arr[k] = rhalf[j];
		j++;
		k++;
	}

    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 
	if(l>=r){
		return;
	}
	int m = (l+r)/2;
	sort(arr, l, m);
	sort(arr, m+1, r);
	merge(arr, l, m, r);
	
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