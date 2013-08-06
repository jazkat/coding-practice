package puzzles

/**
 * Reverse an array of numbers.
 * Note: I have implemented two different ways to do this in Scala
 *  and briefly discuss the pros and cons of each.
 */
object ReverseArray {

  // Pros: In-place list reversal. Don't have to copy elements to a different container.
  // Cons: Must accept a mutable Seq as parameter. Side effects!! Not very functional.
  def reverseInPlace(list: scala.collection.mutable.Seq[Int]): Seq[Int] = {
    for (i <- 0 to list.length / 2){
      val j = list.length - i
      val tmp = list(i)
      list(i) = list(j)
      list(j) = tmp
    }
    list
  }
  
  // Pros: No side effects, no mutable data structures outside of the function definition.
  // Cons: A little more overhead due to conversions between mutable/immutable and traversal of entire list.
  def reverseCopy(list: Seq[Int]): Seq[Int] = {
    var reversed = scala.collection.mutable.Seq[Int]()
    for (i <- (list.length - 1) to 0){
      reversed :+ list(i)
    }
    reversed.toSeq // convert to immutable Seq
  }
}