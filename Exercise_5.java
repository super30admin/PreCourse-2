class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	if(arr[i] == arr[j]) return;
    	else if(arr[i] > arr[j]) {
    		arr[i] = arr[i] + arr[j];
    		arr[j] = arr[i] - arr[j];
    		arr[i] = arr[i] - arr[j];
    	}
    	else {
    		arr[j] = arr[j] + arr[i];
    		arr[i] = arr[j] - arr[i];
    		arr[j] = arr[j] - arr[i];
    	}
	//Try swapping without extra variable 
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
	int pivot = arr[h];
    	int a = l-1;
    	for(int i=l;i<h;i++) {
    		if(arr[i] < pivot) {
    			a++;
    			swap(arr,a,i);
    		}
    	}
    	swap(arr,a+1,h);
    	return a+1;
        //Compare elements and swap.
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
	Stack st = new Stack();
    	st.push(l);
    	st.push(h);
    	while(!st.isEmpty()) {
    		h = st.pop();
    		l = st.pop();
    		
    		int mid = partition(arr,l,h);
    		if(mid+1 < h) {
    			st.push(mid+1);
    			st.push(h);
    		}
    		if (mid-1 > l) {
    			st.push(l);
    			st.push(mid-1);
    		}
    	}
        //Try using Stack Data Structure to remove recursion.
    } 
  
    // A utility function to print contents of arr 
    void printArr(int arr[], int n) 
    { 
        for (int i = 0; i < n; ++i) 
            System.out.print(arr[i] + " "); 
    } 
  
    // Driver code to test above 
    public static void main(String args[]) 
    { 
        IterativeQuickSort ob = new IterativeQuickSort(); 
        int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 }; 
        ob.QuickSort(arr, 0, arr.length - 1); 
        ob.printArr(arr, arr.length); 
    } 
} 
