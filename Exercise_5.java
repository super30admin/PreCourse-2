package precourse2;
//Time Complexity : O(nlogn)
//Space Complexity :O(n)
//Did this code successfully run on Leetcode :Yes
//Any problem you faced while coding this :No

class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 
    	if(i!=j) {
    		arr[i]=arr[i]+arr[j];
    		arr[j]=arr[i]-arr[j];
    		arr[i]=arr[i]-arr[j];    		
    	}
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    {
    	int pivot=arr[l+(h-l)/2];
    	while(l<=h) {
    		while(arr[l]<pivot) {
    			l++;
    		}
    		while(arr[h]>pivot) {
    			h--;
    		}
    		if(l<=h) {
    			swap(arr,l,h);
    			l++;
    			h--;
    		}
    	}
		return l; 
        //Compare elements and swap.
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
    	//if(l>=h)	return;
    	int stack[]=new int[h-l+1];
    	int top=-1;
    	stack[++top]=l;
    	stack[++top]=h;
    	while(top>=0) {
    		h=stack[top--];
    		l=stack[top--];
    		int pivot=partition(arr,l,h);
    		if(pivot-1>l) {
    			stack[++top]=l;
    			stack[++top]=pivot-1;
    		}
    		if(pivot+1<h) {
    			stack[++top]=pivot+1;
    			stack[++top]=h;
    		}
    	}
    } 
  
    // A utility function to print contents of arr 
    void printArr(int arr[], int n) 
    { 
        int i; 
        for (i = 0; i < n; i++) 
            System.out.print(arr[i] + " "); 
    } 
} 
class Exercise_5{
	
	// Driver code to test above 
	public static void main(String args[]) 
	{ 
		IterativeQuickSort ob = new IterativeQuickSort(); 
		int arr[] = { 4, 3, 5, 9,2, 1, 3, 2, 3 }; 
		ob.QuickSort(arr, 0, arr.length - 1); 
		ob.printArr(arr, arr.length); 
	} 
}