package puzzles.checkout;

import static org.junit.Assert.assertEquals;

import org.junit.Test;
import org.junit.BeforeClass;


public class CheckoutScannerTest {

    @BeforeClass
    public static void setUp() {
        CheckoutScanner.setUnitPrice("A", 2.00);
        CheckoutScanner.setVolumePrice("A", 4, 7.00);
        CheckoutScanner.setUnitPrice("B", 12.00);
        CheckoutScanner.setUnitPrice("C", 1.25);
        CheckoutScanner.setVolumePrice("C", 6, 6.00);
        CheckoutScanner.setUnitPrice("D", 0.15);
    }

    // Helper method for scanning multiple items of length 1
    public static void scanItems(CheckoutScanner scanner, String items) {
        for (int i = 0; i < items.length(); i++) {
            scanner.scan("" + items.charAt(i));
        }
    }

    @Test
    public void scannerTest1() {
        CheckoutScanner scanner = new CheckoutScanner();
        scanner.scan("A");
        scanner.scan("A");
        Double expected = 4.00;
        assertEquals(expected, scanner.getTotal());
    }

    @Test
    public void scannerTest2() {
        CheckoutScanner scanner = new CheckoutScanner();
        scanItems(scanner, "ABCDABAA");
        Double expected = 32.40;
        assertEquals(expected, scanner.getTotal());
    }

    @Test
    public void scannerTest3() {
        CheckoutScanner scanner = new CheckoutScanner();
        scanItems(scanner, "CCCCCCC");
        Double expected = 7.25;
        assertEquals(expected, scanner.getTotal());
    }

    @Test
    public void scannerTest4() {
        CheckoutScanner scanner = new CheckoutScanner();
        scanItems(scanner, "ABCD");
        Double expected = 15.40;
        assertEquals(expected, scanner.getTotal());
    }

    @Test
    public void scannerTest5() {
        CheckoutScanner scanner = new CheckoutScanner();
        scanItems(scanner, "AAAAAAAAA");
        Double expected = 16.00;
        assertEquals(expected, scanner.getTotal());
    }

    @Test(expected = IllegalArgumentException.class)
    public void scannerTest6() {
        CheckoutScanner scanner = new CheckoutScanner();
        scanItems(scanner, "AAXCD");
        scanner.getTotal();
    }
}
