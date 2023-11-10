#include<stdlib.h>
#include<stdio.h>

// Merges two subarrays of arr[].
// First subarray is arr[l..m]
// Second subarray is arr[m+1..r]
void merge(int arr[], int l, int m, int r)
{
    int i = l;
    int j = m+1;
    int k = l;
    int B[r+1];
    while (i <= m && j <= r){
        if (arr[i] < arr[j]){
            B[k++] = arr[i++];
        } else {
            B[k++] = arr[j++];
        }
    }
    while (i <= m){
        B[k++] = arr[i++];
    }
    while (j <= r){
        B[k++] = arr[j++];
    }
    for (int i=l; i<=r; i++){
        arr[i] = B[i];
    }
}

/* l is for left index and r is right index of the
   sub-array of arr to be sorted */
void mergeSort(int arr[], int l, int r)
{
    int p;
    for (p=2; p<=r+1; p=p*2){
        for (int i=0; i+p-1<r+1; i=i+p){
            int low = i;
            int high = i+p-1;
            int mid = (low+high)/2;
            merge(arr, low, mid, high);
        }
    }
    if (p/2 < r+1){
        merge(arr, 0, p/2-1, r);
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
    int arr[] = {12, 11, 13, 5, 6, 7};
    int arr_size = sizeof(arr)/sizeof(arr[0]);

    printf("Given array is \n");
    printArray(arr, arr_size);

    mergeSort(arr, 0, arr_size - 1);

    printf("\nSorted array is \n");
    printArray(arr, arr_size);
    return 0;
}