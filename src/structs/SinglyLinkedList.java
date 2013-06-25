package structs;

/*
 * A very simple implementation
 * of a singly linked list.
 */
public class SinglyLinkedList {
	public Node head;
	
	public SinglyLinkedList(Node head){
		this.head = head;
	}
	
	/* Simple Node object that
	 * represents a node in a
	 * SinglyLinkedList.
	 */
	public static class Node{
		public Object data;
		public Node next;
	}
}
