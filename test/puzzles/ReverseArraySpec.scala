package puzzles

import org.specs2.mutable._
import puzzles.ReverseArray._

/**
 * Using specs for specification testing.
 * Ahhh much better :)
 */
class ReverseArraySpec extends SpecificationWithJUnit {

  "Reverse In-Place" should {
    "reverse an array of odd length" in {
      val mutableSeq = scala.collection.mutable.Seq(0,1,2,3,4)
      reverseInPlace(mutableSeq)
      mutableSeq(0) mustEqual 4
      mutableSeq(1) mustEqual 3
      mutableSeq(2) mustEqual 2
      mutableSeq(3) mustEqual 1
      mutableSeq(4) mustEqual 0
    }
    
    "reverse an array of even length" in {
      val mutableSeq = scala.collection.mutable.Seq(0,1,2,3)
      reverseInPlace(mutableSeq)
      mutableSeq(0) mustEqual 3
      mutableSeq(1) mustEqual 2
      mutableSeq(2) mustEqual 1
      mutableSeq(3) mustEqual 0
    }
  }
}