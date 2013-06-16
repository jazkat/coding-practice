public class ParenthesesPuzzle {
	public static boolean isBalanced(String source){
		if (source == null) return true;
		Stack<String> stack = new Stack<String>();
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
	}
}
