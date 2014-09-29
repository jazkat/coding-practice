/* ----------------
 * Reversing A List
 * ----------------
 * Write a program to reverse the direction of a singly linked list.
 */
package puzzles;

import puzzles.structs.SinglyLinkedList;
import puzzles.structs.SinglyLinkedList.Node;

public class ReverseLinkedList {
	public static SinglyLinkedList recursiveReverse(SinglyLinkedList myList){
		if (myList == null) return null;
		Node head = myList.head;
		if (head == null || head.next == null) return myList;
		return new SinglyLinkedList(recursiveReverseHelper(null, head));
	}
	
	private static Node recursiveReverseHelper(Node prev, Node curr){
		if (curr == null) return prev;
		Node next = curr.next;
		curr.next = prev;
		return recursiveReverseHelper(curr, next);
	}
	
	public static SinglyLinkedList iterativeReverse(SinglyLinkedList myList){
		if (myList == null) return null;
		Node head = myList.head;
		if (head == null || head.next == null) return myList;
		return new SinglyLinkedList(iterativeReverseHelper(null, head));
	}
	
	private static Node iterativeReverseHelper(Node prev, Node curr){
		Node next;
		while (curr != null){
			next = curr.next;
			curr.next = prev;
			prev = curr;
			curr = next;
		}
		return prev;
	}
}
