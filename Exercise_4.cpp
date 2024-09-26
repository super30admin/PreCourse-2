// Time Complexity :O(nlogn)
// Space Complexity : O(n)
// Did this code successfully run on Leetcode : N/A
// Any problem you faced while coding this : N/A


// Your code here along with comments explaining your approach



#include <iostream>
#include <vector>
using namespace std;

void merge(int* &arr, int low, int mid, int high){
    int b[high+1];
    int i=low, j=mid+1, k=low;
    //Compare each element and save it in a sorted manner
    while(i<=mid && j<=high){
        if(arr[i] < arr[j]){
            b[k]=arr[i];
            i++;
        }
        else{
           b[k]=arr[j];
            j++;
        }
        k++;
    }
    
    if(i<=mid ){
        while(i<=mid){
           b[k]=arr[i];
            i++;
            k++;
        }
    }
    else if(j<=high ){
        while(j<=high){
           b[k]=arr[j];
            j++;
            k++;
        }
    }
    i=low;
    while(i<=high){
        arr[i]=b[i];
        i++;
    }
}

void merge_sort(int* &arr, int low, int high){
    if(low<high){
        int mid = low +((high-low)/2);
        //Call upper half
        merge_sort(arr, mid+1, high);
        //Call lower half
        merge_sort(arr, low, mid);
        merge(arr, low, mid, high);
    }
}


int main(void){
    int arr[] = {770,  279,   844,   714,   687,   765,   888,   723,   807,   561,   270,   951,   778,   936,   600};
    int *arr_ptr = arr;
    merge_sort(arr_ptr, 0, (sizeof(arr)/sizeof(int))-1);
    int i=0;
    while(i<sizeof(arr)/sizeof(int)){
        cout<<arr[i]<<"\t";
        i++;
    }
    return 0;
}


