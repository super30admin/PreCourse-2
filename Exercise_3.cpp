
// Time Complexity : O( n ) as iterating only once the entire linked list.
// Space Complexity : No extra space complexity other than provided linked list..
// Any problem you faced while coding this : None, knew the algo

// Your code here along with comments explaining your approach
/* Rabbit and tortoise algo or floyd something algo can be used for cycle detection as well*/

#include <iostream> 
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
  if( head == NULL ) {
     cout<< "Empty linked list";
  } else if ( head->next == NULL ){
     cout<<"Only one element, so no middle just printing that val " << head->data;
     cout<<endl;
  } else {
     // Atleast two elements case
     struct Node* slow = head;
     struct Node* fast = head->next;
     while( true ){
        if( fast == NULL || fast->next == NULL ) {
            break;
        }
        slow = slow->next;
        fast = fast->next->next;
     }
     cout<<"middle is "<<slow->data<<endl;
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
