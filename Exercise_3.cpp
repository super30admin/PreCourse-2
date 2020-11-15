// Time Complexity : O(N) where N is the size of the linked list
// Space Complexity : O(N) 
// Did this code successfully run on Leetcode :Yes
// Any problem you faced while coding this :None


// Your code here along with comments explaining your approach

#include<bits/stdc++.h>  
using namespace std;  
  
// Struct  
struct Node  
{  
    int data;  
    struct Node* next;  
};  
  
/* Function to get the middle of the linked list*/
void printMiddle(struct Node *head)  
{  
  //YourCode here
  //Use fast and slow pointer technique
  Node *sp = head, *fp = head;         //initialize two pointers. sp = slow pointer fp = fast pointer
  while(sp && fp && fp->next){         //check to make sure that the pointers do not go out of bound    
      sp = sp->next;                   //when the fp reaches end, sp reaches the middle. as speed of fp is 2 times sp    
      fp = fp->next->next;             //when the number of nodes are even, sp will point to the second node of the two middle nodes
                                       //where as the fp becomes null.    
  }
  cout<<"The middle element = "<<sp->data;  //return value of sp pointer
}  
  
// Function to add a new node  
void push(struct Node** head_ref, int new_data)  
{  
    struct Node* new_node = new Node;  
    new_node->data = new_data;  
    new_node->next = (*head_ref);  
    (*head_ref) = new_node;  
}  
  
// A utility function to print a given linked list  
void printList(struct Node *ptr)  
{  
    while (ptr != NULL)  
    {  
        printf("%d->", ptr->data);  
        ptr = ptr->next;  
    }  
    printf("NULL\n");  
}  
  
// Driver Code 
int main()  
{    
    struct Node* head = NULL;    
    for (int i=12; i>0; i--)  
    {  
        push(&head, i);  
        printList(head);  
        printMiddle(head);  
    }  
  
    return 0;  
}  