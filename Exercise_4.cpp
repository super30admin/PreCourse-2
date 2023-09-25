#include<stdlib.h>
#include<iostream>

// Merges two subarrays of arr[].
// First subarray is arr[l..m]
// Second subarray is arr[m+1..r]
void merge(int arr[], int l, int m, int r)
{
    //Your code here

    int n1=m-l+1, n2=r-m;
    int  x[n1], y[n2];
    for(int i=0;i<n1;i++)x[i] =arr[l+i];
    for(int j=0;j<n2;j++)y[j] =arr[m+1+j];
    int i=0,j=0,k=l;
    while(i<n1 && j<n2){
        if(x[i]<=y[j])arr[k++]=x[i++];
        else arr[k++]=y[j++];
    }
    while(i<n1)arr[k++] = x[i++];
    while(j<n2)arr[k++] = y[j++];

}

/* l is for left index and r is right index of the
   sub-array of arr to be sorted */
void mergeSort(int arr[], int l, int r)
{
    //Your code here
    if(l < r){
        int mid = l+(r-l)/2;
        mergeSort(arr,l,mid);
        mergeSort(arr,mid+1,r);
        merge(arr,l,mid,r);
    }
}

/* UTILITY FUNCTIONS */
/* Function to print an array */
void printArray(int A[], int size)
{
    int i;
    for (i=0; i < size; i++)
        printf("%d ", A[i]);
    printf("\n");
}

/* Driver program to test above functions */
int main()
{
    int arr[] = {12, 11, 13, 5, 6, 7, 3};
    int arr_size = sizeof(arr)/sizeof(arr[0]);

    printf("Given array is \n");
    printArray(arr, arr_size);

    mergeSort(arr, 0, arr_size - 1);

    printf("\nSorted array is \n");
    printArray(arr, arr_size);
    return 0;
}
