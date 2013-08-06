package puzzles

 /**
   * Compute and print Pascal's Triangle.
   * http://en.wikipedia.org/wiki/Pascal's_triangle
   */
object Pascal {

  //For example, pascal(0,2)=1, pascal(1,2)=2 and pascal(1,3)=3
  /**
   * @param a column c
   * @param a row r
   * @returns the number at that spot in the triangle
   */
  def pascal(col: Int, row: Int): Int = {
    if (row == 0) return 1
    if (col == 0 || col == row) return 1
    else return pascal(col-1, row-1) + pascal(col, row-1) // improvements:  cache? tail-recursion?
  }
  
  def printPascal(height: Int) = {
    println("Pascal's Triangle")
    for (row <- 0 to height) {
      for (col <- 0 to row)
        print(pascal(col, row) + " ")
      println()
    }
  }
  
}