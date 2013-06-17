/* ---------------------
 * Parentheses Balancing
 * ---------------------
 * Write a function which verifies parentheses are balanced in a string. 
 * Each open parentheses should have a corresponding close parentheses
 * and they should correspond correctly.
 */
package puzzles;

import java.util.Stack;

public class ParenthesesPuzzle {
	public static boolean isBalanced(String source){
		if (source == null) return true;
		Stack<Character> stack = new Stack<Character>();
		int i = 0;
		while (i < source.length()){
			if (source.charAt(i) == '(' ){
				stack.push( '(' );
			}
			else if (source.charAt(i) == ')' ){
				if (stack.empty()) return false; // unbalanced!
				else stack.pop();
			}
			i++;
		}
		if (stack.empty()) return true;
		else return false;
	}
}
