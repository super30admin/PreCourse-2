//Time complexity: Since we are printing list after every insertion time complexity will be O(n^2). If we are only considering approach it will be O(n) as it is a single pass.
//Space complexity: O(n)
//Code ran successfully with the following output: 

// Only one element
// 14->15->NULL
// Middle element: 15
// 13->14->15->NULL
// Middle element: 14
// 12->13->14->15->NULL
// Middle element: 14
// 11->12->13->14->15->NULL
// Middle element: 13
// 10->11->12->13->14->15->NULL
// Middle element: 13
// 9->10->11->12->13->14->15->NULL
// Middle element: 12
// 8->9->10->11->12->13->14->15->NULL
// Middle element: 12
// 7->8->9->10->11->12->13->14->15->NULL
// Middle element: 11
// 6->7->8->9->10->11->12->13->14->15->NULL
// Middle element: 11
// 5->6->7->8->9->10->11->12->13->14->15->NULL
// Middle element: 10
// 4->5->6->7->8->9->10->11->12->13->14->15->NULL
// Middle element: 10
// 3->4->5->6->7->8->9->10->11->12->13->14->15->NULL
// Middle element: 9
// 2->3->4->5->6->7->8->9->10->11->12->13->14->15->NULL
// Middle element: 9
// 1->2->3->4->5->6->7->8->9->10->11->12->13->14->15->NULL
// Middle element: 8


// === Code Execution Successful ===

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
  struct Node *slow = head; 
  struct Node *fast = head; 
  while(fast != NULL && fast -> next != NULL){
        slow = slow -> next;
        fast = fast -> next -> next;
  }
  // Assumption that if only one element is present, there is NO middle element
  if(slow == fast){
    cout << "Only one element"<< endl;
  }
  else{cout<< "Middle element: "<<slow -> data << endl;}
  
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