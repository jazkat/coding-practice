package structs;

/*
 * An implementation of Binary Search Tree.
 * Every node has at most two children. The tree is configured
 * such that inorder traversal occurs in sorted order.
 * All elements to the left are less than the current
 * element and all elements to the right are greater than the
 * current element. Does not contain duplicates.
 */
public class BST<T extends Comparable<T>> {
	
	private Node<T> root;
	
	/*
	 * Returns true if BST contains this element, false otherwise.
	 */
	public boolean contains(T data){
		return containsHelper(root, data);
	}
	
	private boolean containsHelper(Node<T> current, T data){
		if (current == null) return false;
		if (current.data.compareTo(data) == 0) return true;
		else if (current.data.compareTo(data) > 0) return containsHelper(current.left, data);
		else return containsHelper(current.right, data);
	}
	
	/*
	 * Attempts to insert new element into the BST.
	 * If the BST already contains the element, returns false and does not insert a new element.
	 * Otherwise, inserts new element in the appropriate place and returns true.
	 */
	public boolean insert(T data){
		if (root == null){
			Node<T> elt = new Node<T>(data);
			root = elt;
			return true;
		}
		else {
			if (root.data.compareTo(data) > 0) return insertHelper(root, root.left, data, true);
			if (root.data.compareTo(data) < 0) return insertHelper(root, root.right, data, false);
			return false;
		}
	}
	
	private boolean insertHelper(Node<T> parent, Node<T> current, T data, boolean isLeft){
		if (current == null){
			Node<T> elt = new Node<T>(data);
			if (isLeft) parent.left = elt;
			else parent.right = elt;
			return true;
		} else {
			if (current.data.compareTo(data) > 0) return insertHelper(current, current.left, data, true);
			if (current.data.compareTo(data) < 0) return insertHelper(current, current.right, data, false);
			return false;
		}
	}
	
	// TODO
/*	public boolean remove(T data){
		if (root.data.compareTo(data) > 0) return removeHelper(root, root.left, data, true);
		else if (root.data.compareTo(data) < 0) return removeHelper(root, root.right, data, false);
		else {
			boolean result = removeHelper(null, root, false);
		}
	}
	
	private boolean removeHelper(Node<T> parent, Node<T> current, T data, boolean isLeft){
		if (current == null) return false;
		else if (current.data.compareTo(data) > 0) return removeHelper(current, current.left, data);
		else if (current.data.compareTo(data) < 0) return removeHelper(current, current.right, data);
		else { // remove this node
			if (current.left == null && current.right == null) return removeEltNoChildren(parent, current);
			else if (current.left == null || current.right == null) return removeEltOneChild(parent, current);
			else return removeEltTwoChildren(parent, current);
		}
	}*/
	
	/*
	 * Node structure that is used to represent
	 * an element in a Binary Search Tree.
	 */
	public static class Node<T> {
		private T data;
		private Node<T> left;
		private Node<T> right;
		
		public Node(T data){
			this.data = data;
		}
		
		public T getData(){
			return data;
		}
		
		public Node<T> getLeft(){
			return left;
		}
		
		public Node<T> getRight(){
			return right;
		}
	}
}
