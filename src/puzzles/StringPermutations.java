package puzzles;

import java.util.ArrayList;

public class StringPermutations {
	public ArrayList<String> permutations(String s){
		  ArrayList<String> perms = new ArrayList<String>();
		  permHelper(s, "", perms);
		  return perms;
		}

	private void permHelper(String s, String accum, ArrayList<String> perms){
		if (s.equals("")) perms.add(accum);
		
		for (int i = 0; i < s.length(); i++){
		    permHelper(s.substring(0, i) + s.substring(i+1, s.length()),
		            	accum + s.charAt(i),
						perms);
		}
	}
}
