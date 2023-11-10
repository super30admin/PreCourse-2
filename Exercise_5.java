/*
Time Complexity: O(n^2)
Space Complexity: O(n)
Code runs successfully on Leetcode.
I did not face any problems while coding.
*/
class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 
	if(i!=j){
		arr[i] = arr[i] + arr[j];
		arr[j] = arr[i] - arr[j];
		arr[i] = arr[i] - arr[j];
	}
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
	int pidx = l;
	int itr = l;
	int pivot = arr[h];
	while(itr <= h){
		if(arr[itr] <= pivot){
			swap(arr, itr, pidx);
				
			itr++;
			pidx++;
		}else{
			itr++;
		}
	}
	return pidx - 1;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
	int[] stack = new int[h - l + 1];
	int top = -1;
	stack[++top] = l;
	stack[++top] = h;
	while(top!=-1){
		h = stack[top--];
		l = stack[top--];
		
		int pidx = partition(arr, l, h);
		
		if(pidx - 1 > l){
			stack[++top] = l;
			stack[++top] = pidx - 1;
		} 

		if(pidx + 1 < h){
			stack[++top] = pidx + 1;
			stack[++top] = h; 
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