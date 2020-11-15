#include<stdlib.h> 
#include<stdio.h> 

// Merges two subarrays of arr[]. 
// First subarray is arr[l..m] 
// Second subarray is arr[m+1..r] 
void merge(int arr[], int l, int m, int r) 
{ 
    //Your code here

    int sub_n1 = m-l + 1;
    int sub_n2= r-m;


    //create sub arrays
    int arr1[sub_n1];
    int arr2[sub_n2];

    for(int i=0; i< sub_n1; i++){
        arr1[i]= arr[l+i];
    }

    for(int i=0; i< sub_n2; i++){
        arr2[i]= arr[m+1+i];
    }

    int i=0;
    int j= 0;
    int k=l;


    while(i < sub_n1 && j< sub_n2){
        if( arr1[i] <= arr2[j]){
            arr[k]=arr1[i];
            i++;
            k++;
        }
        else if ( arr1[i] > arr2[j]){
            arr[k] = arr2[j];
            j++;
            k++;
        }
        // else{
        //     arr[k]= arr[i];
        //     i++;
        //     j++;
        //     k++;
        // }
    }

    while( i< sub_n1){
        arr[k] = arr1[i];
        i++;
        k++;
    }

    while(j< sub_n2){
        arr[k]= arr2[j];
        j++;
        k++;
    }


} 
  
/* l is for left index and r is right index of the 
   sub-array of arr to be sorted */

//Time Complexity : O(nlogn)
//Space Complexity : O(n)
void mergeSort(int arr[], int l, int r) 
{ 
    printf("%d %d ", l , r);
    printf("\n");
    //Your code here
    if(l < r){
        int mid = (l+r)/2;
        mergeSort(arr, l, mid);
        mergeSort(arr, mid+1, r);
        merge (arr, l, mid, r);
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