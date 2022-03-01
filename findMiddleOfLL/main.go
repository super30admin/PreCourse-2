package main

import (
	"fmt"
)

type Node struct {
	Val  int
	Next *Node
}

type LinkedList struct {
	head *Node
	tail *Node
	size int
}

func NewLinkedList() *LinkedList {
	return &LinkedList{
		head: nil,
		tail: nil,
		size: 0,
	}
}

// time: o(1)
// because we have tail we can append at the end with o(1) time
// space: o(1)
func (l *LinkedList) Push(x int) {
	newNode := &Node{Val: x}
	if l.head == nil {
		l.head = newNode
		l.tail = newNode
		l.size = 1
		return
	}
	l.tail.Next = newNode
	l.tail = newNode
	l.size++
}

// time: o(n)
// where n is the number of nodes in LL
// space: o(1)
func (l *LinkedList) PrintMiddle() {
	if l.head == nil {
		panic("Head is nil, there is no middle")
	}
	midPos := l.size / 2
	currentPos := 0
	current := l.head
	for currentPos != midPos {
		current = current.Next
		currentPos++
	}
	fmt.Println("Mid node: ", current.Val)
}

// time: o(n)
// where n is the number of nodes in LL
// space: o(1)
func (l *LinkedList) PrintMiddleWithoutMaintaingSize() {
	if l.head == nil {
		panic("Head is nil, there is no middle")
	}
	slow := l.head
	fast := l.head
	// if fast ptr moves 2 times faster than slow, then when fast has reached the end of the LL
	// slow was moving half the speed, therefore slow is half way of fast
	// if fast is at the end and slow is half way of fast - i.e slow is in the middle
	for fast != nil && fast.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
	}
	fmt.Println("Middle node is: ", slow.Val)
}

func main() {
	ll := NewLinkedList()
	ll.Push(1)
	ll.Push(2)
	ll.Push(3)
	ll.PrintMiddle()
	ll.PrintMiddleWithoutMaintaingSize()

	ll.Push(4)
	ll.PrintMiddle()
	ll.PrintMiddleWithoutMaintaingSize()
}
