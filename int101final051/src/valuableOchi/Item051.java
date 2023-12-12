package valuableOchi;

import utilOchi.Tool051;

public class Item051 {
    private final String name;
    private int amount;

    private Item051(String name, int amount) {
        this.name = name;
        this.amount = amount;
    }

    public static Item051 create(String name, int amount) {
        if (Tool051.isUsable051(name) && amount > 0) {
            return new Item051(name, amount);
        }
        return null;
    }

    public int add(Item051 item) {
        if (item == null) {
            throw new RuntimeException();
        }
        int sum = this.amount + item.amount;
        return sum;
    }

    public boolean isMatched(Item051 item) {
        if (this.name.equals(item.name)) {
            return true;
        }
        return false;
    }

    @Override
    public String toString() {
        return String.format("(name = %s , amount = %d", this.name, this.amount)+")";
    }

}
