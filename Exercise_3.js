class Node {
    constructor(data){
      this.data = data
      this.nextElement = null
    }
  }
    
  class LinkedList {
    constructor() {
      this.head = null
    }
    
    isEmpty() {
      return this.head === null
    }
      
    push(data) {
      let incomingNode = new Node(data)
      let existingNode = this.head
      incomingNode.nextElement = existingNode
      this.head = incomingNode
      
      return 'Added incoming node ' + JSON.stringify(this.head)
    }
      
    printMiddle() {
      if (this.isEmpty()) {
        return "Please add node elements to the list"
      } else {
        let slow = this.head
        let fast = this.head
        
        while(fast && fast.nextElement) {
          slow = slow.nextElement
          fast = fast.nextElement.nextElement
        }
        
        return slow
      }
    }
  }
    
  const myLinkedList = new LinkedList()
    
  //Pushing nodes
  console.log(myLinkedList.push(1))
  console.log(myLinkedList.push(2))
  console.log(myLinkedList.push(3))
  console.log(myLinkedList.push(4))
  
  // Print middle of the list
  console.log(myLinkedList.printMiddle())