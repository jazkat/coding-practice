import static org.junit.Assert.*;
import org.junit.Test;
import static puzzles.ParenthesesPuzzle.*;

public class ParenthesesTest {

	@Test
	public void testThatBalancedStringPasses() {
		String s = "(if (any? x) sum (/1 x))";
		assertTrue(isBalanced(s));
	}
	
	@Test
	public void testThatEmptyStringPasses() {
		assertTrue(isBalanced(""));
	}
	
	@Test
	public void testThatUnbalancedStringFails1(){
		String s = ":-)";
		assertFalse(isBalanced(s));
	}
	
	@Test
	public void testThatUnbalancedStringFails2(){
		String s = "())(";
		assertFalse(isBalanced(s));
	}
	
	@Test
	public void testThatUnbalancedStringFails3(){
		String s = "(";
		assertFalse(isBalanced(s));
	}

}
