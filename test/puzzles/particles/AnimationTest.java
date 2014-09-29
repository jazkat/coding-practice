package puzzles.particles;

import static org.junit.Assert.assertArrayEquals;
import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class AnimationTest {

    @Test
    public void stringToBinaryWithEmptyInputTest() {
        String input = "";
        long result = Animation.stringToBinary(input, Animation.Direction.left);
        assertEquals(0L, result);
    }

    @Test
    public void stringToBinaryWithOneDirectionTest1() {
        String input = "..R....";
        long result = Animation.stringToBinary(input, Animation.Direction.left);
        assertEquals(0L, result);
    }

    @Test
    public void stringToBinaryWithOneDirectionTest2() {
        String input = "......R";
        long result = Animation.stringToBinary(input, Animation.Direction.right);
        assertEquals(1L, result);
    }

    @Test
    public void stringToBinaryTest1() {
        String input = "RR..LRL";
        long result = Animation.stringToBinary(input, Animation.Direction.left);
        long expected = 0b101;
        assertEquals(expected, result);
    }

    @Test
    public void stringToBinaryTest2() {
        String input = "RR..LRL";
        long result = Animation.stringToBinary(input, Animation.Direction.right);
        long expected = 0b1100010;
        assertEquals(expected, result);
    }

    @Test
    public void animateLineTest1() {
        long chamber = 0b10010110;
        String expected = "X..X.XX.";
        String result = Animation.animateLine(chamber, 8);
        assertEquals(expected, result);
    }

    @Test
    public void animateLineTest2() {
        long chamber = 0b0110;
        String expected = ".....XX.";
        String result = Animation.animateLine(chamber, 8);
        assertEquals(expected, result);
    }

    @Test
    public void animateLineTest3() {
        long chamber = 0L;
        String expected = "........";
        String result = Animation.animateLine(chamber, 8);
        assertEquals(expected, result);
    }

    @Test
    public void animateTest1() {
        String[] result = Animation.animate(2, "..R....");
        String[] expected =
                {"..X....",
                 "....X..",
                 "......X",
                 "......." };
        assertArrayEquals(expected, result);
    }

    @Test
    public void animateTest2() {
        String[] result = Animation.animate(3, "RR..LRL");
        String[] expected =
                {"XX..XXX",
                 ".X.XX..",
                 "X.....X",
                 "......."};
        assertArrayEquals(expected, result);
    }

    @Test
    public void animateTest3() {
        String[] result = Animation.animate(2, "LRLR.LRLR");
        String[] expected =
                {"XXXX.XXXX",
                 "X..X.X..X",
                 ".X.X.X.X.",
                 ".X.....X.",
                 "........."};
        assertArrayEquals(expected, result);
    }

    @Test
    public void animateTest4() {
        String[] result = Animation.animate(10, "RLRLRLRLRL");
        String[] expected =
                {"XXXXXXXXXX",
                 ".........."};
        assertArrayEquals(expected, result);
    }

    @Test
    public void animateTest5() {
        String[] result = Animation.animate(1, "...");
        String[] expected =
                {"..."};
        assertArrayEquals(expected, result);
    }

    @Test
    public void animateTest6() {
        String[] result = Animation.animate(1, "LRRL.LR.LRR.R.LRRL.");
        String[] expected =
                {"XXXX.XX.XXX.X.XXXX.",
                "..XXX..X..XX.X..XX.",
                ".X.XX.X.X..XX.XX.XX",
                "X.X.XX...X.XXXXX..X",
                ".X..XXX...X..XX.X..",
                "X..X..XX.X.XX.XX.X.",
                "..X....XX..XX..XX.X",
                ".X.....XXXX..X..XX.",
                "X.....X..XX...X..XX",
                ".....X..X.XX...X..X",
                "....X..X...XX...X..",
                "...X..X.....XX...X.",
                "..X..X.......XX...X",
                ".X..X.........XX...",
                "X..X...........XX..",
                "..X.............XX.",
                ".X...............XX",
                "X.................X",
                "..................."};
        assertArrayEquals(expected, result);
    }
}
