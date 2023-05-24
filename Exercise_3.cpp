#include<iostream>  
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
    int n=0;
    Node* temp_1 = head; 
    Node* temp_2=head;
    while(temp_1!=NULL &&temp_1->next!=NULL){

            temp_2 = temp_2->next;
            temp_1 = temp_1->next->next;

    }

    cout<<"  "<<temp_2->data;
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