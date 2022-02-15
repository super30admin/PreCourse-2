#include<iostream>
using namespace std;  
  
// A utility function to swap two elements  
void Swap(int arr[], int i, int j){
    int t=arr[i];
    arr[i]=arr[j];
    arr[j]=t;
} 
  
/* This function takes last element as pivot, places  
the pivot element at its correct position in sorted  
array, and places all smaller (smaller than pivot)  
to left of pivot and all greater elements to right  
of pivot */
int partition(int arr[], int l, int r){
    int pivot=arr[r];
    int i=l-1;
    for (int j=l; j<r; j++){
        if(arr[j]<pivot){
            i++;
            Swap(arr,i,j);
        } 
    }
    Swap(arr,i+1,r);
    return i+1;
} 
  
/* The main function that implements QuickSort  
arr[] --> Array to be sorted,  
low --> Starting index,  
high --> Ending index */
void Quicksort(int arr[],int l, int r){
    if(l<r){
        int pi=partition(arr,l,r);
        Quicksort(arr,l,pi-1);
        Quicksort(arr,pi+1,r);
    }
} 
  
/* Function to print an array */
void printarray(int arr[], int n){
    
    for(int i=0; i<n; i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;
} 
  
// Driver Code 
int main(){

    int arr[] = {10, 7, 8, 9, 1, 5}; 

    int n = sizeof(arr) / sizeof(arr[0]);

    Quicksort(arr,0,n-1);

    cout<<"Sorted array is: ";   

    printarray(arr,n);

    return 0;
}