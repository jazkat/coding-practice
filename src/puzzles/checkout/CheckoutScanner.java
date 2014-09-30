package puzzles.checkout;

import java.util.HashMap;
import java.util.Map;

/**
 * A class representing a Point of Sale system.
 */
public class CheckoutScanner {

    // System wide pricing
    private static Map<String, Double> unitPrices = new HashMap<>();
    private static Map<String, Pair<Integer, Double>> bulkPrices = new HashMap<>();

    // Transaction level info
    private Map<String, Integer> items;

    /**
     *  Start a new transaction.
     */
    public CheckoutScanner() {
        items = new HashMap<>();
    }

    /**
     * Set the standard price for purchasing an item.
     *
     * @param item the item that needs to be priced
     * @param price the amount charged for each purchase of this item
     */
    public static void setUnitPrice(String item, Double price) {
        unitPrices.put(item, price);
    }

    /**
     * Set a special price for buying items in bulk (ie. 3 for 1.00).
     * Additional items purchased will not receive the special rate.
     *
     * @param item the item that needs to be priced
     * @param count number of items required for this price rate
     * @param price the special rate for buying the required number of this item
     */
    public static void setVolumePrice(String item, int count, Double price) {
        bulkPrices.put(item, new Pair<>(count, price));
    }

    /**
     * Scan an item for purchase.
     *
     * @param item a single item in the transaction
     */
    public void scan(String item) {
        if (items.containsKey(item)) {
            items.put(item, items.get(item) + 1);
        } else {
            items.put(item, 1);
        }
    }

    /**
     * Calculate the total cost of the transaction.
     *
     * Currently this is designed to be called at the end of a transaction,
     * it is not optimized for calculating a running total after each scan.
     *
     * @return total cost of all scanned items
     */
    public Double getTotal() {
        Double total = 0.0;
        int count, bulkCount, bulkOrders, unitOrders;
        for (String item : items.keySet()) {
            count = items.get(item);
            if (bulkPrices.containsKey(item) && count >= bulkPrices.get(item).first()) {
                bulkCount = bulkPrices.get(item).first();
                bulkOrders = count / bulkCount;
                unitOrders = count % bulkCount;
                total += bulkOrders * bulkPrices.get(item).second();
                total += unitOrders * unitPrices.get(item);
            } else if (unitPrices.containsKey(item)) {
                total += count * unitPrices.get(item);
            } else {
                throw new IllegalArgumentException("" +
                        "Price check! Scanned item does not have an assigned price.");
            }
        }
        return total;
    }

    /**
     * Helper class for creating pairs
     */
    private static class Pair<A, B> {
        public final A first;
        public final B second;
        public Pair(A first, B second) {
            this.first = first;
            this.second = second;
        }
        public A first() {
            return first;
        }
        public B second() {
            return second;
        }
    }
}
