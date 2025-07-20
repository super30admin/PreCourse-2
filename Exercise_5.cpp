#include <bits/stdc++.h> 
using namespace std; 
  
// A utility function to swap two elements 
void swap(int* a, int* b) 
{ 
    int t = *a; 
    *a = *b; 
    *b = t; 
} 
  
/* This function is same in both iterative and recursive*/
int partition(int arr[], int l, int h) 
{ 
    int pivot =arr[l];
    int cnt=0;
    for(int i=l+1;i<=h;i++){
        if(arr[i]<= pivot){
            cnt++;
        }
    }
    //place pivot at right position
    int pivotIndex = l+cnt;
    swap(arr[pivotIndex],arr[l]);

    //left and right part of array
    int i=l,j=h;
    while(i<pivotIndex && j>pivotIndex){
        while(arr[i]<pivot){
            i++;
        }

        while(arr[j]>pivot){
            j--;
        }

        if(i<pivotIndex && j>pivotIndex){
            swap(arr[i++],arr[j--]);
        }
    }
    return pivotIndex; 
} 
//Time Complexity : O(n*logn)
//Space Complexity : O(n)  
/* A[] --> Array to be sorted,  
l --> Starting index,  
h --> Ending index */
void quickSortIterative(int arr[], int l, int h) 
{ 
    //Try to think that how you can use stack here to remove recursion.
    // Create an auxiliary stack 
	int stack[h - l + 1]; 

	// initialize top of stack 
	int top = -1; 

	// push initial values of l and h to stack 
	stack[++top] = l; 
	stack[++top] = h; 

	// Keep popping from stack while is not empty 
	while (top >= 0) { 
		// Pop h and l 
		h = stack[top--]; 
		l = stack[top--]; 

		// Set pivot element at its correct position 
		// in sorted array 
		int p = partition(arr, l, h); 

		// If there are elements on left side of pivot, 
		// then push left side to stack 
		if (p - 1 > l) { 
			stack[++top] = l; 
			stack[++top] = p - 1; 
		} 

		// If there are elements on right side of pivot, 
		// then push right side to stack 
		if (p + 1 < h) { 
			stack[++top] = p + 1; 
			stack[++top] = h; 
		} 
	} 
} 
  
// A utility function to print contents of arr 
void printArr(int arr[], int n) 
{ 
    int i; 
    for (i = 0; i < n; ++i) 
        cout << arr[i] << " "; 
} 
  
// Driver code 
int main() 
{ 
    int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 }; 
    int n = sizeof(arr) / sizeof(*arr); 
    quickSortIterative(arr, 0, n - 1); 
    printArr(arr, n); 
    return 0; 
} 