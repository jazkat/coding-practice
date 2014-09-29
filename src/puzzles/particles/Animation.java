package puzzles.particles;

import com.google.common.base.Preconditions;

import java.lang.Math;
import java.util.ArrayList;

public class Animation {

    public enum Direction {
        left  ('L'),
        right ('R');

        private char particleDirection;
        Direction(char particleDirection) {
            this.particleDirection = particleDirection;
        }

        public char getValue() {
            return particleDirection;
        }
    }

    // Animate particles moving in a tube
    public static String[] animate(int speed, String init) {
        Preconditions.checkArgument(speed >= 1 && speed <= 10, "Speed must be between 1 and 10 inclusive.");
        Preconditions.checkNotNull(init, "Init position string cannot be null.");
        Preconditions.checkArgument(!init.isEmpty() && init.length() <= 50,
                "Length of init position string must be between 1 and 50 chars inclusive.");

        // Impl Note:
        // Particle movement can be represented by shifting bits left or right.
        // Can use binary with bitwise operations to represent these arrays of particles.
        long leftBits = stringToBinary(init, Direction.left);
        long rightBits = stringToBinary(init, Direction.right);
        long chamber = leftBits | rightBits;

        int size = init.length();
        // mask enforces length of tube
        long mask = (long) Math.pow(2.0, size) - 1;
        ArrayList<String> result = new ArrayList<>();
        while (chamber > 0) {
            result.add(animateLine(chamber, size));
            leftBits <<= speed;
            rightBits >>= speed;
            chamber = (leftBits | rightBits) & mask;
        }
        result.add(animateLine(chamber, size));
        return result.toArray(new String[result.size()]);
    }

    protected static String animateLine(long chamber, int size) {
        StringBuilder line = new StringBuilder();
        while (chamber > 0) {
            // check whether odd to determine rightmost digit
            if (chamber % 2 == 1) {
                line.append("X");
            } else {
                line.append(".");
            }
            chamber /= 2;
        }
        while (line.length() < size) {
            line.append(".");
        }
        return line.reverse().toString();
    }

    // extract the particles of one direction from init as N-length binary,
    // where N is the number of positions (length) of init
    protected static long stringToBinary(String init, Direction direction) {
        int exponent = init.length() - 1;
        long value = 0L;
        for (int i = 0; i < init.length(); i++) {
            if (init.charAt(i) == direction.getValue()) {
                // record as 2 ** exponent
                value += Math.pow(2.0, exponent - i);
            }
        }
        return value;
    }
}
