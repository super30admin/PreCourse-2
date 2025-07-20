#include <bits/stdc++.h> 
using namespace std;  
  
// A utility function to swap two elements  
void swap(int* a, int* b)  
{  
    //Your Code here 
    int t=*a;
    *a=*b;
    *b=t;
}  
//Time Complexity : O(n*logn)
//Space Complexity : O(n)   
/* This function takes last element as pivot, places  
the pivot element at its correct position in sorted  
array, and places all smaller (smaller than pivot)  
to left of pivot and all greater elements to right  
of pivot */
int partition (int arr[], int low, int high)  
{  
    int pivot =arr[low];
    int cnt=0;
    for(int i=low+1;i<=high;i++){
        if(arr[i]<= pivot){
            cnt++;
        }
    }
    //place pivot at right position
    int pivotIndex = low+cnt;
    swap(arr[pivotIndex],arr[low]);

    //left and right part of array
    int i=low,j=high;
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
  
/* The main function that implements QuickSort  
arr[] --> Array to be sorted,  
low --> Starting index,  
high --> Ending index */
void quickSort(int arr[], int low, int high)  
{  
    //base case
    if(low>=high) return ;

    int p=partition(arr,low,high);//partition

    //Now a recursive call
    quickSort(arr,low,p-1);

    quickSort(arr,p+1,high);
}  
  
/* Function to print an array */
void printArray(int arr[], int size)  
{  
    int i;  
    for (i = 0; i < size; i++)  
        cout << arr[i] << " ";  
    cout << endl;  
}  
  
// Driver Code 
int main()  
{  
    int arr[] = {10, 7, 8, 9, 1, 5};  
    int n = sizeof(arr) / sizeof(arr[0]);  
    quickSort(arr, 0, n - 1);  
    cout << "Sorted array: \n";  
    printArray(arr, n);  
    return 0;  
}  