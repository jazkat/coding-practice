/* ---------------------
 * String Permutations
 * ---------------------
 * Write a method to compute all permutations of a string.
 */
package puzzles;

import java.util.ArrayList;

public class StringPermutations {
	public static ArrayList<String> permutations(String s){
		  ArrayList<String> perms = new ArrayList<String>();
		  if (s != null) permHelper(s, "", perms);
		  return perms;
		}

	private static void permHelper(String s, String accum, ArrayList<String> perms){
		if (s.equals("") && !perms.contains(accum)) perms.add(accum);
		
		for (int i = 0; i < s.length(); i++){
		    permHelper(s.substring(0, i) + s.substring(i+1, s.length()),
		            	accum + s.charAt(i),
						perms);
		}
	}
}
