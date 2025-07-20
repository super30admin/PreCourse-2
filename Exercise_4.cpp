#include<stdlib.h> 
#include<stdio.h> 
//TC : O(n*logn)
//SC : O(n) 
// Merges two subarrays of arr[]. 
// First subarray is arr[l..m] 
// Second subarray is arr[m+1..r] 
void merge(int arr[], int l, int m, int r) 
{ 
    m=(l+r)/2;

    int len1 = m-l+1;
    int len2 = r-m;

    int *first = new int[len1];
    int *second =new int[len2];

    int k=l;
    for(int i=0;i<len1;i++){
        first[i]=arr[k++];
    }

    //copy values
    k=m+1;
    for(int i=0;i<len2;i++){
        second[i]=arr[k++];
    }

    //merge 2 sorted arrays
    int index1 = 0,index2=0;
    k=l;
    while(index1<len1 && index2 < len2){
        if(first[k] <second[k]){
            arr[k++]=first[index1++];
        }
        else arr[k++]=second[index2++];
    }
    while(index1<len1){
        arr[k++]=first[index1++]; 
    }
    while(index2<len2){
        arr[k++]=second[index2++ ]; 
    }

    delete []first;
    delete []second;
} 
  
/* l is for left index and r is right index of the 
   sub-array of arr to be sorted */
void mergeSort(int arr[], int l, int r) 
{ 
    if(l>=r) return ;
    int mid= (l+r)/2;
    mergeSort(arr,l,mid);
    mergeSort(arr,mid+1,r);

    merge(arr,l,mid,r);
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