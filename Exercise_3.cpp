/**
 * Time complexity:
 * The time complexity is O(N)
 * 
 */

/**
 * Space Complexity:
 * The space complexity is O(1) as we are not creating any extra space.
 */

/**
 * Approach:
 * We are using fast and slow pointers. The idea is slow pointer
 * moves by one step and fast pointer moves by two step. When the
 * fast pointer will reach at the end of the list, the slow
 * pointer will be at the middle of the list.
 */

//The code ran perfectly


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
  Node* slow = head;
  Node* fast = head;

  while(fast != nullptr && fast -> next != nullptr){
      slow = slow->next;
      fast = fast->next->next;
  }
  cout << "The middle is " << slow->val << endl;
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