package puzzles

import org.scalatest.FlatSpec
import org.junit.Assert._
import puzzles.Pascal._

/**
 * Trying out ScalaTest for specification testing.
 * Not too impressed with it, the functionality is
 * very minimal and I still have to write raw assertions.
 */
class PascalSpec extends FlatSpec {
  
  def printAndCheckExpected(expected: Int => Boolean, height: Int = 5): Boolean = {
    for (row <- 0 to height){
      for (col <- 0 to row){
        print(pascal(col, row) + " ")
      }
      assert(expected(row))
      println()
    }
    println()
    return false
  }
  
  def symmetricRow(row: Int): Boolean = {
      for (col <- 0 to row / 2)
        if (pascal(col, row) != pascal(row-col, row)) return false
      return true
    }
  
  def exponentialRow(row: Int): Boolean = {
      var sum: Int = 0
      for (col <- 0 to row)
        sum += pascal(col, row)
      return sum == (scala.math.pow(2, row))
    }

  "Pascal's Triangle" should "have symmetric rows" in {
    printAndCheckExpected(symmetricRow)
  }

  "Pascal's Triangle" should "have rows whose sums increase exponentially" in {
    printAndCheckExpected(exponentialRow, 10)
  }
  
}