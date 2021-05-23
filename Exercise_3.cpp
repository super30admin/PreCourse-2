// Time Complexity: for printMiddle() : O(n), push(): O(1), printList(): O(n)
// Space Comlexity: O(1) for all functions, assuming making new nodes is not considered as using additional space
// Did this code successfully run on Leetcode : Yes
//--------------------------------------------------------------------------------------------------------------------------
// Any problem you faced while coding this : My doubt was if we can use the check (fast->next && fast->next->next) 
// rather than using (fast && fast->next) ? because for list having an even length we can choose 2 options from the middle 
//--------------------------------------------------------------------------------------------------------------------------
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
  struct Node *slow = head;
  struct Node *fast = head;

  if(head != NULL){
    while(fast != NULL && fast->next != NULL){
        fast = fast->next->next;
        slow = slow->next;
    }
    cout<<"The Middle Element is : "<<slow->data<<"\n\n";
  }
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
    for (int i=15; i>0; i--)  
    {  
        push(&head, i);  
        printList(head);  
        printMiddle(head);  
    }
  
    return 0;  
}  