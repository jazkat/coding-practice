package puzzles;

import static java.util.Arrays.asList;
import static org.junit.Assert.*;
import static puzzles.StringPermutations.*;

import java.util.ArrayList;
import java.util.List;

import org.junit.Test;

public class PermutationsTest {

	private void permsMatchesExpected(String testStr, List<String> expected){
		List<String> actual = permutations(testStr);
		
		// Compare without caring about order
		assertTrue("Permutations for " + testStr + " did not match expected.",
				expected.size() == actual.size() && actual.containsAll(expected));
	}

	@Test
	public void testThatCorrectPermutationsAreComputed() {
		permsMatchesExpected("ABC", asList("ABC", "ACB", "BAC", "BCA", "CAB", "CBA"));
	}
	
	@Test
	public void testThatPermutatedStringsHaveSameResult() {
		permsMatchesExpected("ABC", permutations("CBA"));
	}
	
	@Test
	public void testThatResultDoesNotContainDuplicates() {
		permsMatchesExpected("AAC", asList("AAC", "ACA", "CAA"));
	}
	
	@Test
	public void testThatPermCorrectForStringWithRepeatedSingleCharacter() {
		permsMatchesExpected("AAAA", asList("AAAA"));
	}
	
	@Test
	public void testThatPermCorrectForStringOfLengthOne() {
		permsMatchesExpected("Z", asList("Z"));
	}
	
	@Test
	public void testThatPermCorrectForEmptyString() {
		permsMatchesExpected("", asList(""));
	}
	
	@Test
	public void testThatHandleNullOk() {
		permsMatchesExpected(null, new ArrayList<String>());
	}

}
