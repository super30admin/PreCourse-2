
/*

Time Complexity : O(NlogN)
log N for splitting and O(N) for merging sub arrays
Space Complexity : O(N)
Creating new array to temporary store the array values 
and replace existing values in the main array with sorted elements.

*/

#include<iostream>

using namespace std;

/* UTILITY FUNCTIONS */
/* Function to print an array */
void printArray(int A[], int size) 
{ 
    int i; 
    for (i=0; i < size; i++) 
        printf("%d ", A[i]); 
    printf("\n"); 
} 

// Merges two subarrays of arr[]. 
// First subarray is arr[l..m] 
// Second subarray is arr[m+1..r] 
void merge(int arr[], int l, int m, int r) 
{ 
    //Your code here

    const int first_sub_len {m-l+1};
    const int sec_sub_len{r-m};

    int* first_sub = new int[first_sub_len];
    int* sec_sub = new int[sec_sub_len];

    for(int i{0};i<first_sub_len;++i)
        first_sub[i] = arr[l+i];
    
    // printArray(first_sub,first_sub_len);
    // cout<<endl;

    
    for(int i{0};i<sec_sub_len;++i)
        sec_sub[i] = arr[m+1+i];

    // printArray(sec_sub,sec_sub_len);
    // cout<<endl;
    
    int first_sub_id{0},sec_sub_id{0},main_sub_id{l};
    while(first_sub_id<first_sub_len && sec_sub_id<sec_sub_len)
    {
        if(first_sub[first_sub_id]>=sec_sub[sec_sub_id])
        {
            arr[main_sub_id++] = sec_sub[sec_sub_id++];
        }
        else if(first_sub[first_sub_id]<sec_sub[sec_sub_id])
        {
            arr[main_sub_id++] = first_sub[first_sub_id++];
        }
        else
        {
            arr[main_sub_id++] = first_sub[first_sub_id++];
            arr[main_sub_id++] = sec_sub[sec_sub_id++];

        }
    }

    while(first_sub_id<first_sub_len)
        arr[main_sub_id++] = first_sub[first_sub_id++];

    while(sec_sub_id<sec_sub_len)
        arr[main_sub_id++] = sec_sub[sec_sub_id++];

    // for(int i{l};i<=r;++i)
    //     cout<<arr[i]<<" ";
    // cout<<endl;

    delete[] first_sub;
    delete[] sec_sub;
} 
  
/* l is for left index and r is right index of the 
   sub-array of arr to be sorted */
void mergeSort(int arr[], int l, int r) 
{ 
    //Your code here
    if (l>=r)
        return;
    int m{(l+r)/2};
    mergeSort(arr,l,m);
    mergeSort(arr,m+1,r);
    merge(arr,l,m,r);
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