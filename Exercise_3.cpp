// Time Complexity : O(n/2)
// Space Complexity :

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
  Node* slow=new Node;
  Node* fast=new Node;
  slow=head;
  fast=head;
  while(fast!=NULL && fast->next!=NULL)
  {
      slow=slow->next;
      fast=fast->next->next;
  }
  cout<<"The middle is "<<slow->data<<endl;
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
        cout<<"->"<<ptr->data<<" ";  
        ptr = ptr->next;
    }  
    cout<<"NULL\n";  
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