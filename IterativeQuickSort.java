class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
    	if(arr[i] != arr[j]) {
			 arr[i] = arr[i] + arr[j]; 
			 arr[j] = arr[i] - arr[j]; 
			 arr[i] = arr[i] - arr[j];
    	}
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int low, int high) 
    { 
    	int mid = arr[high];//high as the pivot index
    	int lower_index = low-1;
    	for(int i=low; i<high; i++) {
    		//checking if the mid is smaller than current
    		if(arr[i]<mid) {
    			lower_index++;
    			System.out.println(arr[lower_index]);
    			swap(arr, lower_index, i);
    		}
    	}
    	swap(arr, lower_index+1, high);
    	return lower_index+1;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
    	Stack s = new Stack();
    	s.push(l);
    	s.push(h);
    	
    	// Partition and setting the high and low are done until the stack is empty
    	while(!s.isEmpty()) {
    		h = s.pop();
    		l = s.pop();
    		// this means there is only two elements no need to partition
    		if( h-l <  2) {
    			continue;
    		}
    		else {
    			int index = partition(arr, l, h);
    			System.out.println("Index: "+index);
    			if(index-1 > 1) {
    				s.push(l);
        			s.push(index-1);
    			}
    			if(index+1 < h) {
    				s.push(index+1);
        			s.push(h);	
    			}
    			
    		}
    	}
    } 
  
    // A utility function to print contents of arr 
    void printArr(int arr[], int n) 
    { 
        int i; 
        for (i = 0; i < n; ++i) 
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