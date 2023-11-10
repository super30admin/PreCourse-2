// #include <bits/stdc++.h> 

// TC: O(nlogn) for best case, O(n^2) for worst case
// SC: O(1);(however recursive calling takes O(n) stack space)



#include<iostream>
#include<stack>
using namespace std;  



  
// A utility function to swap two elements  
void swap(int* a, int* b)  
{  
    //Your Code here 
    int temp = *a;
    *a = *b;
    *b = temp;
}  
  
/* This function takes last element as pivot, places  
the pivot element at its correct position in sorted  
array, and places all smaller (smaller than pivot)  
to left of pivot and all greater elements to right  
of pivot */
int partition (int arr[], int low, int high)  
{  
    //Your Code here 
    int pivot = arr[high];
    int j = high;int i = low-1;
    while(i<j)
    {
        do{
            i++;
        }while(arr[i]<pivot);
        do{
            j--;
        }while(arr[j]>pivot);
        if(i<j){
            swap(arr[j],arr[i]);
        }
    }
   // cout << "pivot is :"<< pivot << " and arr[high] is : "<< arr[high]<< endl;
    swap(arr[i],arr[high]);
    return i;
}  
  
/* The main function that implements QuickSort  
arr[] --> Array to be sorted,  
low --> Starting index,  
high --> Ending index */
void quickSort(int arr[], int low, int high)  
{ 
    if(low >=high) return; 
    int  p = partition(arr,low,high);
    quickSort(arr,low,p-1);
    quickSort(arr,p+1,high);

    //Your Code here 

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