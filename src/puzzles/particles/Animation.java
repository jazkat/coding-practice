package puzzles.particles;

import com.google.common.base.Preconditions;

import java.lang.Math;

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

    public static String animate(int speed, String init) {
        Preconditions.checkArgument(speed >= 1 && speed <= 10, "Speed must be between 1 and 10 inclusive.");
        Preconditions.checkNotNull(init, "Init position string cannot be null.");
        Preconditions.checkArgument(!init.isEmpty() && init.length() <= 50,
                "Length of init position string must be between 1 and 50 chars inclusive.");

        // We can use 2 arrays to easily model movement of L and R bound particles.
        // Particle movement can be represented by shifting left or right.
        // Can use binary and bitwise operations to represent these arrays of particles.
        long leftBits = 0b101010101;
        long rightBits = 0b10101010;
        return "";
    }


    protected static long stringToBinary(String init, Direction direction) {
        // extract the particles of one direction from init as N-length binary,
        // where N is the number of positions (length) of init
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
