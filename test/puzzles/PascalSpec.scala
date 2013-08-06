package puzzles

import org.scalatest.FlatSpec
import org.junit.Assert._
import puzzles.Pascal._

class PascalSpec extends FlatSpec {
  
  def checkExpected(height: Int, expected: (Int, Int) => Boolean): Boolean = {
    for (row <- 0 to height){
      for (col <- 0 to row){
        print(pascal(col, row) + " ")
        if (!expected(col, row)) return false
      }
      println()
    }
    return true
  }

  "Pascal's Triangle" should "have symmetrical rows" in {
    def symmetricRow(col: Int, row: Int): Boolean = {
      pascal(col, row) == pascal(row-col, row)
    }
    
    checkExpected(5, symmetricRow)
  }

//  "Pascal's Triangle" should "have rows whose sums increase exponentially" in {
//    def exponential(col: Int, row: Int): Boolean = {
//      //assertEquals(pascal)
//    }
//  }
  
}